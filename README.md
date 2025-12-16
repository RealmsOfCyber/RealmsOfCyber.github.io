# RealmsOfCyber.github.io
This git repo generates the website https://www.realmsofcyber.com/

## Setup

Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Generate the Site

Run the site generation script:

```bash
python3 generate.py
```

This will:
- Automatically detect the current year from your system date
- Generate `site/index.html` for the current year
- Generate `site/thanks.html` for the current year
- Generate archive pages (e.g., `site/2025.html`) for all available years

The generated HTML files will be written to the `site/` directory.

## Run Locally

After generating the site, you can view it locally using Python's built-in HTTP server to serve from the root directory:

```bash
python3 -m http.server --directory site 8000
```

Then open your browser to: `http://localhost:8000`

## Pushing to Production

The site is automatically deployed to GitHub Pages when you push changes to the `main` branch.

The GitHub Actions workflow (`.github/workflows/static.yml`) will automatically:
- Install dependencies
- Generate the site
- Deploy to GitHub Pages

The site will be live at https://www.realmsofcyber.com/ within a few minutes after the workflow completes.

You can also manually trigger the deployment from the GitHub Actions tab in the repository.


## Project Structure

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