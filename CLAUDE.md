# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spendly is a Flask-based expense tracking web application. This is a student project built with Python/Flask, SQLite, and vanilla JavaScript.

## Tech Stack

- **Backend**: Flask 3.1.3 with Werkzeug
- **Database**: SQLite (via `database/db.py`)
- **Frontend**: Jinja2 templates, vanilla JavaScript, CSS
- **Testing**: pytest with pytest-flask

## Commands

```bash
# Run the application
python app.py

# Run tests
pytest

# Install dependencies
pip install -r requirements.txt
```

## Architecture

```
expense-tracker/
├── app.py              # Flask app with route definitions
├── database/
│   ├── __init__.py
│   └── db.py           # Database utilities (get_db, init_db, seed_db)
├── static/
│   ├── css/
│   │   ├── style.css   # Main stylesheet
│   │   └── landing.css # Landing page styles
│   └── js/
│       └── main.js     # Frontend JavaScript
├── templates/
│   ├── base.html       # Base template with navbar/footer
│   ├── *.html          # one template per page
└── requirements.txt
```

**Where things belong:**
- New routes: `app.py` only, no  blueprints
- DB logic: `database/db.py ` only, never inline in routes
- New pages: new `.html` file extending `base.html`
- Page-specific styles: new `.css` file,not inline `<style>` tags

---
## Code style
- Python: PEP 8,snake_case for all variables and functions
- Templates: Jinja2 with `url_for()` for every internal link - never hardcode URLs
- Route functions: one responsibility only - fetch data, render template,done
- DB queries: always use parameterized queries(`?` placeholder) - never f-stings in SQL
- Error handling: use `abort()` for HTTP errors, not bare `return "error string" `

## Tech constraints
- **Flask only** - no FastAPI, no Django, no other web frameworks
- **SQLite only** - no PostgreSQL, no SQLAlchemy ORM, no external DB
- **Vanilla JS only** - no React, no jQuery, no npm package
- **No new pip packages** - work within `requirements.txt` as-is unless explicitly told otherwise
- Python 3.10+ assumed - f-strings and `match` statements are fine

## Key Files

- `app.py`: Main Flask application with routes for landing, auth (login/register/logout), profile, and expense CRUD operations. Currently many routes return placeholder strings as students implement features incrementally.

- `database/db.py`: Database layer where students implement:
  - `get_db()` - SQLite connection with row_factory and foreign keys enabled
  - `init_db()` - Creates tables using CREATE TABLE IF NOT EXISTS
  - `seed_db()` - Inserts sample development data

- `static/js/main.js`: Frontend JavaScript for interactive features (modal on landing page, form handling)

## Commands
```bash
#Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run dev server(port 5001)
python app.py

# Run all tests
pytest

# Run a specific test file
pytest tests/test_foo.py

# Run a specific test by name
pytest -k "test_name"

# Run tests with output visible
pytest -s
```

---
## Implemented vs stub routes
|Route|Status
|`Get /` | Implemented - renders `landing.html` |
|`Get /register` | Implemented - renders `register.html` |
|`Get /login` | Implemented - renders `login.html` |
|`Get /logout` | Stub - Step 3 |
|`Get /profile` | Stub - Step 4 |
|`Get /expenses/add` | Stub - Step 7 |
|`Get /expenses/<id>/edit` | Stub - Step 8 |
|`Get /expenses/<id>/delete` | Stub - Step 9 |


## Development Notes

- The app runs on port 5001 in debug mode
- Routes follow a simple function-based pattern: `@app.route("/path")`
- Templates extend `base.html` which provides navbar, footer, and block structure
- The project uses a custom design system with CSS variables defined in `style.css`
