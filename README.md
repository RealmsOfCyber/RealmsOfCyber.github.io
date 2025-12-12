# RealmsOfCyber.github.io
This git repo generates the website https://www.realmsofcyber.com/

## Variable Templating

/
├── generate.py              ← Main entry point
├── generator_helpers.py     ← Helper functions
├── data/                    ← All year-specific data
│   └── 2025/                ← Year data directory
│       ├── speakers.py
│       ├── schedule.py
│       ├── variables.py
│       └── ...
├── templates/               ← Jinja templates
└── site/                    ← Generated HTML

### Year-Based Structure
The site uses a year-based architecture where `current_year` is automatically detected from the system date in `generate.py`. All data and assets are organized by year in `{year}/` directories (e.g., `2025/`, `2026/`).

Each year directory contains:
- **Data files**: `speakers.py`, `schedule.py`, `sponsors.py`, `exhibitors.py`, `variables.py`, `testimonials.py` (optional, used for `post_event`), `photo_highlights.py` (optional, used for `post_event`)
- **Assets**: Images organized in `site/assets/images/{year}/` with subdirectories for `speakers/`, `sponsors/`, `exhibitors/`, `highlights/`, and `venue/`

Archive pages (e.g., `2025.html`) automatically load data from their year-specific directory, show `post-event` content if `event_date` has passed, and display testimonials when available. The footer includes links to past conferences.

### Speaker and Sponsor Images
- Crop the speaker photo to a 1x1 aspect ratio using any tool. eg. https://www.photoresizer.com/
- **Images are year-specific**: 
- For 2025: `site/assets/images/2025/speakers/`, `site/assets/images/2025/sponsors/`, etc.
- For 2026: `site/assets/images/2026/speakers/`, `site/assets/images/2026/sponsors/`, etc.