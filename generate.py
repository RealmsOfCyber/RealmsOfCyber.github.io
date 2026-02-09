"""
Main site generation script.
Orchestrates data loading, template rendering, and file writing.
Each year (2024, 2025, 2026) and holding (slug 9999) has its own data (data/{slug}/) and view (views/{slug}.jinja).
"""

from pathlib import Path

from generator_helpers import (
    get_data_for_slug,
    discover_available_years,
    render_view,
    render_thanks_page,
    HOLDING_YEAR,
)

# Current year: index and thanks use this slug; archives generated for all available years
current_year = 2026
available_years = discover_available_years()
current_data = get_data_for_slug(current_year)

# If current year has no highlights, load from previous year for the index
if not current_data.get("photo_highlights") and not current_data.get("testimonials"):
    previous_year = current_year - 1
    if previous_year in available_years:
        previous_data = get_data_for_slug(previous_year)
        current_data = dict(current_data)
        current_data["photo_highlights"] = previous_data.get("photo_highlights", [])
        current_data["testimonials"] = previous_data.get("testimonials", [])
        current_data["highlights_year"] = previous_year

# Generate main index page (current year's view, not an archive page)
print(f"Generating index page (view {current_year})...")
index_html = render_view(current_year, current_data, is_year_page=False)
with open("site/index.html", "w") as f:
    f.write(index_html)

# Generate thanks page
print(f"Generating thanks page for year {current_year}...")
thanks_html = render_thanks_page(current_data)
with open("site/thanks.html", "w") as f:
    f.write(thanks_html)

# Generate archive pages: each year has its own view template
for archive_year in available_years:
    print(f"Generating archive page for {archive_year} (view {archive_year})...")
    archive_data = get_data_for_slug(archive_year)
    archive_html = render_view(archive_year, archive_data, is_year_page=True)
    with open(f"site/{archive_year}.html", "w") as f:
        f.write(archive_html)

# Holding (slug 9999): own data and view; output to /holding.html, /holding/index.html, and /9999.html
print("Generating holding page (view 9999)...")
holding_data_root = get_data_for_slug(HOLDING_YEAR)
holding_data_root = dict(holding_data_root, base_path="")
holding_html_root = render_view(HOLDING_YEAR, holding_data_root, is_year_page=False, base_path_override="")
with open("site/holding.html", "w") as f:
    f.write(holding_html_root)
with open("site/9999.html", "w") as f:
    f.write(holding_html_root)
holding_dir = Path("site/holding")
holding_dir.mkdir(parents=True, exist_ok=True)
holding_data_dir = get_data_for_slug(HOLDING_YEAR)  # default base_path "../"
holding_html_dir = render_view(HOLDING_YEAR, holding_data_dir, is_year_page=False)
with open(holding_dir / "index.html", "w") as f:
    f.write(holding_html_dir)

print("✓ Site generation complete!")
