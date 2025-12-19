# ROCC25 Data

This directory contains the archived data for Realms of Cyber Conference 2025 (ROCC25).

## Files

- `speakers.py` - All speakers from ROCC25
- `schedule.py` - Main schedule and OT schedule from ROCC25
- `sponsors.py` - Sponsors from ROCC25
- `exhibitors.py` - Exhibitors from ROCC25
- `variables.py` - Year-specific variables (date, etc.) for ROCC25

## Usage

This data is automatically loaded by `year_data.py` when generating archive pages. The 2025 archive page (`2025.html`) uses this data.

## Future Years

When preparing for ROCC26:
1. The root-level files (`speakers.py`, `schedule.py`, etc.) will be updated with 2026 data
2. Before updating, copy the current 2026 data to a `2026/` directory (similar to this one)
3. Update `year_data.py` to include the new year


