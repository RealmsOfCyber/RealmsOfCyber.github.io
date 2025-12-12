"""
Helper functions for site generation.
Consolidates event utilities, year data loading, and template rendering.
"""

import sys
import importlib.util
from pathlib import Path
from datetime import datetime, date
from jinja2 import Environment, FileSystemLoader

# ============================================================================
# Event Utilities
# ============================================================================

today = date.today()

def is_post_event(event_date_str):
    """
    Check if current date is after the event date.
    This allows us to show the "after event" content if the event date has passed.
    """
    if not event_date_str:
        return False
    try:
        event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
        return today > event_date
    except:
        return False


# ============================================================================
# Year Data Loading
# ============================================================================

def import_from_year_dir(year, module_name):
    """Import a module from a year-specific directory."""
    # Year directories are in data/{year}/
    base_path = Path(__file__).parent
    year_dir = base_path / "data" / str(year)
    module_path = year_dir / f"{module_name}.py"
    
    if not module_path.exists():
        return None
    
    spec = importlib.util.spec_from_file_location(f"{module_name}_{year}", module_path)
    if spec is None or spec.loader is None:
        return None
    
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"{module_name}_{year}"] = module
    spec.loader.exec_module(module)
    return module

def get_current_year_data(current_year):
    """Load all data for the current year from its directory."""
    try:
        speakers_module = import_from_year_dir(current_year, "speakers")
        schedule_module = import_from_year_dir(current_year, "schedule")
        variables_module = import_from_year_dir(current_year, "variables")
        tickets_module = import_from_year_dir(current_year, "tickets")
        sponsors_module = import_from_year_dir(current_year, "sponsors")
        exhibitors_module = import_from_year_dir(current_year, "exhibitors")
        testimonials_module = import_from_year_dir(current_year, "testimonials")
        photo_highlights_module = import_from_year_dir(current_year, "photo_highlights")
        
        return {
            "speakers": speakers_module.speakers if speakers_module else [],
            "mc": getattr(speakers_module, 'mc', []) if speakers_module else [],
            "schedule": schedule_module.schedule if schedule_module else [],
            "schedule2": schedule_module.schedule2 if schedule_module else [],
            "schedules": getattr(schedule_module, 'schedules', []) if schedule_module else [],
            "sponsors": sponsors_module.sponsors if sponsors_module else {},
            "exhibitors": exhibitors_module.exhibitors if exhibitors_module else [],
            "testimonials": getattr(testimonials_module, 'testimonials', []) if testimonials_module else [],
            "photo_highlights": getattr(photo_highlights_module, 'photo_highlights', []) if photo_highlights_module else [],
            "year": getattr(variables_module, 'year', current_year) if variables_module else current_year,
            "date": getattr(variables_module, 'date', "TBD") if variables_module else "TBD",
            "event_date": getattr(variables_module, 'event_date', None) if variables_module else None,
            # tickets_on_sale is calculated dynamically based on event_date
            "ticket_url": getattr(tickets_module, 'ticket_url', "") if tickets_module else "",
            "ticket_1_name": getattr(tickets_module, 'ticket_1_name', "") if tickets_module else "",
            "ticket_1_price": getattr(tickets_module, 'ticket_1_price', 0) if tickets_module else 0,
            "ticket_1_description": getattr(tickets_module, 'ticket_1_description', "") if tickets_module else "",
            "ticket_1_url_fragment": getattr(tickets_module, 'ticket_1_url_fragment', "") if tickets_module else "",
            "ticket_2_name": getattr(tickets_module, 'ticket_2_name', "") if tickets_module else "",
            "ticket_2_price": getattr(tickets_module, 'ticket_2_price', 0) if tickets_module else 0,
            "ticket_2_description": getattr(tickets_module, 'ticket_2_description', "") if tickets_module else "",
            "ticket_2_url_fragment": getattr(tickets_module, 'ticket_2_url_fragment', "") if tickets_module else "",
            "ticket_3_name": getattr(tickets_module, 'ticket_3_name', "") if tickets_module else "",
            "ticket_3_price": getattr(tickets_module, 'ticket_3_price', 0) if tickets_module else 0,
            "ticket_3_description": getattr(tickets_module, 'ticket_3_description', "") if tickets_module else "",
            "ticket_3_url_fragment": getattr(tickets_module, 'ticket_3_url_fragment', "") if tickets_module else "",
            "become_a_sponsor_url": getattr(variables_module, 'become_a_sponsor_url', "") if variables_module else "",
            "mailing_list_url": getattr(variables_module, 'mailing_list_url', "") if variables_module else "",
            "call_for_presenters_url": getattr(variables_module, 'call_for_presenters_url', "") if variables_module else "",
            "contact_us_url": getattr(variables_module, 'contact_us_url', "") if variables_module else "",
            "humanitix_contact_url": getattr(variables_module, 'humanitix_contact_url', "") if variables_module else "",
            "sponsor_blurb": getattr(variables_module, 'sponsor_blurb', "") if variables_module else "",
            "exhibitor_blurb": getattr(variables_module, 'exhibitor_blurb', None) if variables_module else None,
        }
    except Exception as e:
        print(f"Warning: Could not load current year ({current_year}) data: {e}")
        return {
            "speakers": [],
            "mc": [],
            "schedule": [],
            "schedule2": [],
            "schedules": [],
            "sponsors": {},
            "exhibitors": [],
            "testimonials": [],
            "photo_highlights": [],
            "year": current_year,
            "date": "TBD",
            "event_date": None,
            "ticket_url": "",
            "ticket_1_name": "", "ticket_1_price": 0, "ticket_1_description": "", "ticket_1_url_fragment": "",
            "ticket_2_name": "", "ticket_2_price": 0, "ticket_2_description": "", "ticket_2_url_fragment": "",
            "ticket_3_name": "", "ticket_3_price": 0, "ticket_3_description": "", "ticket_3_url_fragment": "",
            "become_a_sponsor_url": "",
            "mailing_list_url": "",
            "call_for_presenters_url": "",
            "contact_us_url": "",
            "humanitix_contact_url": "",
            "sponsor_blurb": "",
            "exhibitor_blurb": None,
        }

def discover_available_years():
    """
    Discover all available year directories by scanning the data/ directory.
    Returns a list of years that have data directories.
    """
    base_path = Path(__file__).parent
    data_dir = base_path / "data"
    years = []
    
    if not data_dir.exists():
        return years
    
    for item in data_dir.iterdir():
        if item.is_dir() and item.name.isdigit():
            # Check if it has a variables.py file (indicates it's a valid year directory)
            if (item / "variables.py").exists():
                years.append(int(item.name))
    return sorted(years)

# ============================================================================
# Template Rendering
# ============================================================================

# Load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader('templates'))
index_template = env.get_template('index.jinja')
thanks_template = env.get_template('thanks.jinja')

def render_page(year_data, is_year_page=False):
    """
    Render a page using the `index.jinja` template with the provided year data.
    The template automatically handles pre/post event variations based on is_post_event.
    
    Args:
        year_data: Dictionary containing year-specific data
        is_year_page: If True, this is an archive/year-specific page (not the main index)
    """
    event_date = year_data.get("event_date")
    is_post = is_post_event(event_date)
    
    # Calculate schedule enable flags (only show if schedules have content)
    enable_main = len(year_data.get("schedule", [])) > 0
    enable_ot = len(year_data.get("schedule2", [])) > 0
    has_schedules = len(year_data.get("schedules", [])) > 0
    
    # Tickets are on sale if event hasn't passed yet
    tickets_on_sale = not is_post
    
    context = {
        "year": year_data.get("year"),
        "next_year": year_data.get("year", 0) + 1,
        "date": year_data.get("date", "TBD"),
        "become_a_sponsor_url": year_data.get("become_a_sponsor_url", ""),
        "mailing_list_url": year_data.get("mailing_list_url", ""),
        "call_for_presenters_url": year_data.get("call_for_presenters_url", ""),
        "contact_us_url": year_data.get("contact_us_url", ""),
        "humanitix_contact_url": year_data.get("humanitix_contact_url", ""),
        "sponsors": year_data.get("sponsors", {}),
        "exhibitors": year_data.get("exhibitors", []),
        "speakers": year_data.get("speakers", []),
        "mc": year_data.get("mc", []),
        "testimonials": year_data.get("testimonials", []),
        "photo_highlights": year_data.get("photo_highlights", []),
        "sponsor_blurb": year_data.get("sponsor_blurb", ""),
        "exhibitor_blurb": year_data.get("exhibitor_blurb", None),
        "tickets_on_sale": tickets_on_sale,
        "ticket_url": year_data.get("ticket_url", ""),
        "ticket_1_name": year_data.get("ticket_1_name", ""),
        "ticket_1_price": year_data.get("ticket_1_price", 0),
        "ticket_1_description": year_data.get("ticket_1_description", ""),
        "ticket_1_url_fragment": year_data.get("ticket_1_url_fragment", ""),
        "ticket_2_name": year_data.get("ticket_2_name", ""),
        "ticket_2_price": year_data.get("ticket_2_price", 0),
        "ticket_2_description": year_data.get("ticket_2_description", ""),
        "ticket_2_url_fragment": year_data.get("ticket_2_url_fragment", ""),
        "ticket_3_name": year_data.get("ticket_3_name", ""),
        "ticket_3_price": year_data.get("ticket_3_price", 0),
        "ticket_3_description": year_data.get("ticket_3_description", ""),
        "ticket_3_url_fragment": year_data.get("ticket_3_url_fragment", ""),
        "enable_main_schedule": enable_main,
        "enable_ot_schedule": enable_ot,
        "has_schedules": has_schedules,
        "schedules": year_data.get("schedules", []),
        "schedule": year_data.get("schedule", []),
        "schedule2": year_data.get("schedule2", []),
        "is_post_event": is_post,
        "is_year_page": is_year_page,
    }
    
    return index_template.render(**context)

def render_thanks_page(year_data):
    """
    Render the thanks.html page using the thanks template with the provided year data.
    """
    context = {
        "year": year_data.get("year"),
        "date": year_data.get("date", "TBD"),
        "ticket_url": year_data.get("ticket_url", ""),
    }
    
    return thanks_template.render(**context)

