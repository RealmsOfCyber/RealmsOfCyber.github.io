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

def process_speakers_data(speakers_data):
    """Extract presenters and mcs from speakers data structure."""
    if isinstance(speakers_data, dict):
        # New structure: { "presenters": [], "mcs": [] }
        return {
            "speakers": speakers_data.get("presenters", []),
            "mc": speakers_data.get("mcs", [])
        }
    else:
        # Legacy structure: separate speakers and mc variables
        return {
            "speakers": speakers_data if speakers_data else [],
            "mc": []
        }

def add_schedule_logos(schedule_list):
    """Add realm icons to schedule items (for 2025+ format)."""
    schedule_ret = []
    for schedule_item in schedule_list:
        if "speaker" not in schedule_item.keys():
            schedule_ret.append(schedule_item)
            continue
        realm = schedule_item.get("realm", "")
        realm_icon_map = {
            "Space": "fa-satellite",
            "Cognitive": "fa-brain",
            "Land": "fa-truck",
            "Land/Air": "fa-truck",
            "Sea": "fa-ship",
            "Air": "fa-plane-departure",
            "Biological": "fa-dna",
            "Multi": "fa-earth-americas",
        }
        schedule_item["logo"] = realm_icon_map.get(realm, "NONE")
        schedule_ret.append(schedule_item)
    return schedule_ret

def process_schedules_data(schedules_data, year):
    """Process schedules data and convert to template format."""
    if isinstance(schedules_data, dict):
        # New structure: { "schedule_1": { "name": "...", "title": "...", "items": [] }, ... }
        processed_schedules = []
        
        for schedule_key, schedule_data in schedules_data.items():
            # Handle both new structure (dict with name/title/items) and legacy (just a list)
            if isinstance(schedule_data, dict):
                schedule_items = schedule_data.get("items", [])
                schedule_name = schedule_data.get("name", schedule_key)
                schedule_title = schedule_data.get("title", schedule_key.replace("_", " ").title())
                schedule_subtitle = schedule_data.get("subtitle", None)
                schedule_date = schedule_data.get("date", None)
            else:
                # Legacy: just a list of items
                schedule_items = schedule_data
                schedule_name = schedule_key
                schedule_title = schedule_key.replace("_", " ").title()
                schedule_subtitle = None
                schedule_date = None
            
            if not schedule_items:
                continue
                
            # Add realm icons to schedule items
            converted_items = add_schedule_logos(schedule_items)
            
            processed_schedules.append({
                "id": schedule_name,
                "title": schedule_title,
                "subtitle": schedule_subtitle,
                "date": schedule_date,
                "items": converted_items
            })
        
        return processed_schedules
    else:
        # Legacy structure: already processed
        return schedules_data if schedules_data else []

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
        
        # Process speakers data
        speakers_raw = getattr(speakers_module, 'speakers', {}) if speakers_module else {}
        speakers_processed = process_speakers_data(speakers_raw)
        
        # Process schedules data
        schedules_raw = getattr(schedule_module, 'schedules', {}) if schedule_module else {}
        year = getattr(variables_module, 'year', current_year) if variables_module else current_year
        schedules_processed = process_schedules_data(schedules_raw, year)
        
        return {
            "speakers": speakers_processed["speakers"],
            "mc": speakers_processed["mc"],
            "schedule": schedules_raw.get("schedule_1", {}).get("items", []) if isinstance(schedules_raw, dict) and isinstance(schedules_raw.get("schedule_1"), dict) else (schedules_raw.get("schedule_1", []) if isinstance(schedules_raw, dict) else []),
            "schedule2": schedules_raw.get("schedule_2", {}).get("items", []) if isinstance(schedules_raw, dict) and isinstance(schedules_raw.get("schedule_2"), dict) else (schedules_raw.get("schedule_2", []) if isinstance(schedules_raw, dict) else []),
            "schedules": schedules_processed,
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
            "next_event_date": getattr(variables_module, 'next_event_date', "") if variables_module else "",
            "production": getattr(variables_module, 'production', True) if variables_module else True,
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
            "next_event_date": "",
            "production": True,
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
    Pre-event year pages (e.g. 2026) show Save-the-date and hide speakers/schedule/sponsors/exhibitors.
    
    Args:
        year_data: Dictionary containing year-specific data
        is_year_page: If True, this is an archive/year-specific page (not the main index)
    """
    event_date = year_data.get("event_date")
    is_post = is_post_event(event_date)
    
    # Calculate schedule enable flags (only show if schedules have content)
    enable_main = len(year_data.get("schedule", [])) > 0
    enable_ot = len(year_data.get("schedule2", [])) > 0
    # has_schedules should be True if either schedule, schedule2, or schedules has content
    has_schedules = (len(year_data.get("schedule", [])) > 0 or 
                     len(year_data.get("schedule2", [])) > 0 or 
                     len(year_data.get("schedules", [])) > 0)
    
    # Tickets are on sale if event hasn't passed yet AND we have ticket data
    has_ticket_data = bool(year_data.get("ticket_url")) or any([
        year_data.get("ticket_1_name"), 
        year_data.get("ticket_2_name"), 
        year_data.get("ticket_3_name")
    ])
    tickets_on_sale = not is_post and has_ticket_data
    
    # Get available years for footer - show all years except the current page's year
    available_years = discover_available_years()
    current_page_year = year_data.get("year")
    past_years = [y for y in available_years if y != current_page_year]
    
    # Format year as ROCC25, ROCC26, etc. (last 2 digits)
    year_int = year_data.get("year", 0)
    rocc_year = f"ROCC{str(year_int)[-2:]}" if year_int > 0 else "ROCC"
    next_year_int = year_int + 1
    rocc_next_year = f"ROCC{str(next_year_int)[-2:]}" if next_year_int > 0 else "ROCC"
    
    context = {
        "year": year_data.get("year"),
        "rocc_year": rocc_year,
        "next_year": next_year_int,
        "rocc_next_year": rocc_next_year,
        "available_years": sorted(available_years, reverse=True),  # All available years for footer
        "past_years": sorted(past_years, reverse=True),  # Most recent first
        "date": year_data.get("date", "TBD"),
        "become_a_sponsor_url": year_data.get("become_a_sponsor_url", ""),
        "mailing_list_url": year_data.get("mailing_list_url", ""),
        "call_for_presenters_url": year_data.get("call_for_presenters_url", ""),
        "contact_us_url": year_data.get("contact_us_url", ""),
        "humanitix_contact_url": year_data.get("humanitix_contact_url", ""),
        "sponsors": year_data.get("sponsors", {}),
        "exhibitors": year_data.get("exhibitors", []),
        "has_sponsors": any(len(year_data.get("sponsors", {}).get(tier, [])) > 0 for tier in ["Platinum", "Gold", "Silver", "Bronze"]),
        "has_exhibitors": len(year_data.get("exhibitors", [])) > 0,
        "has_speakers": len(year_data.get("speakers", [])) > 0,
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
        "next_event_date": year_data.get("next_event_date", ""),
        "production": year_data.get("production", True),
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

