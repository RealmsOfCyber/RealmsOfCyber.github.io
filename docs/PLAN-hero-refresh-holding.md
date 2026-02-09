# Plan: Holding Page & Hero Refresh (ROCC26)

## Summary

- **Holding page**: Duplicate of the current 2026 view at URL **/holding** (no change to main index or 2026.html until you’re ready).
- **Hero refresh**: Applied only on the holding page: new headline, 2026 theme, hierarchy, optional new background and font; CTA kept with strong contrast.

---

## 0. Data and hero image structure (implemented)

### 0.1 Holding as a standalone “year”

- **Holding has its own data directory**: **`data/holding/`**, same layout as a year (e.g. `data/2026/`).
- Contents: `variables.py` (hero_image_path, hero_theme_line1/2, year=2026, URLs, etc.), plus `exhibitors.py`, `speakers.py`, `schedule.py`, `sponsors.py`, `testimonials.py`, `photo_highlights.py`, `tickets.py` (empty/minimal so the page renders like 2026).
- The generator loads holding via **`get_holding_data()`** (from `generator_helpers`), which uses **`import_from_data_dir("holding", module_name)`** so holding is a first-class page, not a one-off copy of 2026.

### 0.2 Hero image directory per year and holding

- **Per-year and per-holding hero directories** under **`site/assets/images/`**:
  - `site/assets/images/2024/hero/`
  - `site/assets/images/2025/hero/`
  - `site/assets/images/2026/hero/`
  - `site/assets/images/holding/hero/`
- Each directory can hold that page’s hero image(s) (e.g. `hero.jpg`). Holding uses a **different** hero image than 2026.
- **Config**: In `data/holding/variables.py`, **`hero_image_path`** is set to e.g. `"holding/hero/hero.jpg"` (path relative to `assets/images/`). Templates/CSS use `{{ base_path }}assets/images/{{ hero_image_path }}` for the holding hero; year pages can later use the same pattern with e.g. `2026/hero/hero.jpg`.

---

## 1. Holding page (URL /holding)

### 1.1 Output and URLs

- **Target URL**: `/holding` (and `/holding/`).
- **Output**: Generate **`site/holding/index.html`** so GitHub Pages serves it at `/holding` (and `/holding/`).
- **Content**: Same as current 2026 view (data from **`data/holding/`**; sections: About, Venue, FAQ, etc.) but with the new hero (see below). Rest of page unchanged.

### 1.2 Asset and link paths

- All pages today use **relative** paths: `assets/...`, `index.html`, `2025.html`, etc.
- From `site/holding/index.html`, assets and other HTML live one level up, so paths must be prefixed with **`../`**.
- **Approach**: **`base_path`** is set in the generator from page data:
  - **Root pages** (e.g. `site/index.html`, `site/2026.html`): `base_path = ""` (default in context).
  - **Holding page** (data from `data/holding/`): `base_path = "../"` and `is_holding_page = True` (set in `get_holding_data()`).
- **Generator**: `generate.py` calls **`get_holding_data()`**, **`render_page(holding_data)`**, and writes to **`site/holding/index.html`**. Context includes `base_path`, `is_holding_page`, `hero_image_path`, `hero_theme_line1`, `hero_theme_line2`.
- **Template changes**: Use **`{{ base_path }}`** for every asset and internal link:
  - `head.jinja`: `href="{{ base_path }}assets/css/theme.css"`, favicon, og:image, etc.
  - `top.jinja`: logo `src`, `href="{{ base_path }}index.html"`, Past Events `href="{{ base_path }}{{ past_year }}.html"`, etc.
  - `footer.jinja`: logo `src`, `href="{{ base_path }}{{ past_year }}.html"`.
  - Any other template that references `assets/` or `.html` (e.g. `speakers.jinja`, `highlights.jinja`) should use `{{ base_path }}` where needed.

---

## 2. Hero refresh (holding page only)

### 2.1 When to show the new hero

- In the template (e.g. `top.jinja`), the new hero block is shown only when **`is_holding_page`** is true (and optionally when it’s the 2026 pre-event view, if you want the same hero on both holding and index later).
- For this phase: **only on the holding page**.

### 2.2 Content and hierarchy

**Order (top to bottom):**

1. **Event name**  
   - Single primary headline: **“ROCC26”**  
   - Remove “Save the Date” entirely.

2. **Theme (mandatory)**  
   - Wording:
     - **Line 1:** “Sovereignty in a Connected World:”
     - **Line 2:** “Where Reality Meets Resilience”
   - Styling:
     - Slightly smaller than the main “ROCC26” headline.
     - Subtitle: lighter font weight and/or reduced opacity so it reads as secondary.

3. **Date and location**  
   - Keep:
     - **Date:** “27 August 2026” (current variable is “27th August 2026”; adjust in `data/2026/variables.py` to “27 August 2026” if you want exact match to brief).
     - **Location:** “Brisbane Powerhouse, Brisbane, Australia”
   - Reduce visual prominence (smaller and/or lighter) so they are clearly secondary to headline and theme.

4. **Call to action**  
   - Keep the CTA: **“Join the ROCC mailing list”** (same URL as current `mailing_list_url`).
   - Ensure **strong contrast** against the new hero background (see CTA styling below).

### 2.3 Template structure (holding hero)

- In `top.jinja`, under the existing `{% if not is_post_event %}` block, add a branch for **`is_holding_page`** that renders:
  - One `<h1>`: “ROCC26”.
  - A theme block (e.g. two lines with the theme text and a shared class for styling).
  - Date and location in a smaller/lighter “meta” block.
  - CTA button.
- Optional: move the “Be notified when registration opens for ROCC26” line below the CTA and style it subtly, or keep as-is.

### 2.4 Styling

- **New CSS** (e.g. in `site/assets/css/theme.css` or a small override loaded only when needed):
  - **Hero theme block**: font-size smaller than `.hero-heading`; one line can be slightly larger, the “Where Reality Meets Resilience” line with lighter weight and/or lower opacity (e.g. `opacity: 0.9` or `font-weight: 400`).
  - **Date/location**: reduce `font-size` and weight/opacity so they sit below the theme in the hierarchy (reuse or extend `.hero-meta` with a modifier if useful).
  - **CTA**: `.btn-primary` (or a holding-specific class) with colours that contrast strongly on the new background (e.g. solid background and white or dark text; avoid low-contrast combinations). If the new background is dark, a light button; if light, a dark button.
- **Background**: New hero image (see §2.5). Use **`{{ base_path }}assets/images/{{ hero_image_path }}`** (from `data/holding/variables.py`). Applied only for the holding hero (e.g. class `.hero-carousel .carousel-item-holding` or inline style).

### 2.5 Background image

- Brief mentions a **background image (attached)**. In the repo, there is no attached file; you’ll need to add it.
- **Steps:**
  - Save the holding hero asset (e.g. `hero.jpg`) under **`site/assets/images/holding/hero/`** (see §0.2). Path is configured in **`data/holding/variables.py`** as **`hero_image_path = "holding/hero/hero.jpg"`** (relative to `assets/images/`).
  - In the template or CSS, set the holding hero slide to use **`{{ base_path }}assets/images/{{ hero_image_path }}`** (or a holding-specific CSS class that points to that path).
  - Ensure the overlay (e.g. `.hero-block-mask`) still gives readable text and good CTA contrast; adjust `rgba` if needed.
- **Year pages**: Each year has its own hero directory (e.g. `site/assets/images/2026/hero/`). You can later add `hero_image_path` to `data/2026/variables.py` and use the same pattern for year-specific hero images.

### 2.6 Font (optional)

- If you want a **different font** for the hero (or site-wide):
  - Change or add a font in `templates/head.jinja` (e.g. Google Fonts).
  - Apply the new font to `.hero-heading` and/or the theme block (e.g. a new class `.hero-theme`) so the holding hero feels refreshed without a full redesign.

---

## 3. Implementation checklist

### Phase A: Holding page (duplicate 2026 at /holding)

- [x] **Data and hero dirs**
  - [x] Create **`data/holding/`** with `variables.py` (hero_image_path, hero_theme_line1/2, year=2026, base_path, URLs) and same content files as 2026 (empty).
  - [x] Create hero image dirs: **`site/assets/images/2024/hero/`**, **`2025/hero/`**, **`2026/hero/`**, **`holding/hero/`** (each with `.gitkeep`; holding has a short README).
- [x] **Generator**
  - [x] Add **`import_from_data_dir(slug, module_name)`** and **`get_holding_data()`** in `generator_helpers.py`.
  - [x] Add `base_path`, `is_holding_page`, `hero_image_path`, `hero_theme_line1`, `hero_theme_line2` to render context (defaults for non-holding).
  - [x] In `generate.py`, create **`site/holding/`** and render holding data to **`site/holding/index.html`**.
- [ ] **Templates**
  - [ ] `head.jinja`: use `{{ base_path }}` for all asset and favicon links.
  - [ ] `top.jinja`: use `{{ base_path }}` for logo, Home, Past Events, and any other internal links; use `is_holding_page` and hero variables for holding hero block.
  - [ ] `footer.jinja`: use `{{ base_path }}` for logo and past-event links.
  - [ ] Other templates: fix any `assets/` or `.html` links that must work from `holding/index.html` (e.g. speakers, highlights).
- [ ] **Verify**: Open `/holding` and confirm layout, assets, and navigation (Home, Past Events, About, etc.) work.

### Phase B: Hero refresh on holding only

- [ ] **Content**
  - [ ] In `top.jinja`, add holding-specific hero branch: “ROCC26” headline, theme two-liner, date/location, CTA.
  - [ ] Optionally set `next_event_date` to “27 August 2026” in `data/2026/variables.py` and use it for the date line.
- [ ] **Styling**
  - [ ] Add/update CSS: theme block smaller and subtitle lighter; date/location secondary; CTA high contrast.
  - [ ] Add holding hero background class and point it to the new image.
- [ ] **Asset**
  - [ ] Add the new hero background image to `site/assets/images/` and wire it in CSS.
- [ ] **Optional**
  - [ ] New font in `head.jinja` and applied to hero/theme if desired.
- [ ] **Verify**: Check hierarchy (1. ROCC26, 2. Theme, 3. Date/location, 4. CTA), contrast, and readability on desktop and mobile.

### Phase C: Later (when ready)

- [ ] If the design is approved, you can switch the **main index** (and optionally `2026.html`) to use the same hero by setting `is_holding_page=True` for the main 2026 render or by merging the holding hero block into the main “pre-event” branch and toggling via a variable (e.g. `use_2026_hero`).

---

## 4. Files to touch (reference)

| Area              | Files |
|-------------------|--------|
| Generator         | `generate.py`, `generator_helpers.py` |
| Data (holding)    | **`data/holding/`** — `variables.py`, `exhibitors.py`, `speakers.py`, `schedule.py`, `sponsors.py`, `testimonials.py`, `photo_highlights.py`, `tickets.py` |
| Hero image dirs   | **`site/assets/images/2024/hero/`**, **`2025/hero/`**, **`2026/hero/`**, **`holding/hero/`** (hero image per year/holding) |
| Hero / layout     | `templates/top.jinja` |
| Assets & links    | `templates/head.jinja`, `templates/footer.jinja`, and any template with `assets/` or `.html` |
| Styling           | `site/assets/css/theme.css` (or SCSS source if you recompile) |
| Data (optional)   | `data/2026/variables.py` (optional date wording; holding uses `data/holding/variables.py`) |

---

## 5. Date wording note

- Current variable: **“27th August 2026”**.
- Brief: **“27 August 2026”**.
- Either keep “27th” or change `next_event_date` in `data/2026/variables.py` to “27 August 2026” for consistency with the brief.
