"""
Main site generation script.
Orchestrates data loading, template rendering, and file writing.
"""

from datetime import date
from generator_helpers import get_current_year_data, discover_available_years, render_page, render_thanks_page

# Get current year from system date
current_year = date.today().year

# Load current year data
current_data = get_current_year_data(current_year)

# Generate main index page
print(f"Generating index page for year {current_year}...")
index_html = render_page(current_data)
with open("site/index.html", "w") as f:
    f.write(index_html)

# Generate thanks page
print(f"Generating thanks page for year {current_year}...")
thanks_html = render_thanks_page(current_data)
with open("site/thanks.html", "w") as f:
    f.write(thanks_html)

# Generate archive pages for all available years (including current year for archive view)
available_years = discover_available_years()
for archive_year in available_years:
    print(f"Generating archive page for {archive_year}...")
    archive_data = get_current_year_data(archive_year)
    archive_html = render_page(archive_data, is_year_page=True)
    with open(f"site/{archive_year}.html", "w") as f:
        f.write(archive_html)

print("✓ Site generation complete!")
