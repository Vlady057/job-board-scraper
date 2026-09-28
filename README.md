
# Job Board Scraper

A Python web scraping project that collects job listings from a demo job board using **Playwright**, parses selected fields, filters jobs by keyword, and saves the results to JSON.

## Features

* Browser automation with Playwright
* Extraction of specific job fields:

  * Job title
  * Company
  * Location
* Keyword-based job filtering
* JSON data storage
* Separate output for all jobs and filtered jobs
* Automated tests with pytest

## Project Structure

```text
job-board-scraper/
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── parser.py
│   └── storage.py
│
├── data/
│   ├── jobs.json
│   └── python_jobs.json
│
├── tests/
│   ├── test_parser.py
│   └── test_storage.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies

* Python 3.13
* Playwright
* pytest
* JSON

## How It Works

The scraper opens the job board with Playwright and extracts the required information from each job listing.

```text
Job Board
    ↓
Playwright
    ↓
Extract job data
    ↓
Parse title, company and location
    ↓
Save all jobs
    ↓
Filter by keyword
    ↓
Save filtered jobs
```

The project currently collects 100 job listings and filters them by the keyword `python`.

## Output

All scraped jobs are saved to:

```text
data/jobs.json
```

Python-related jobs are saved separately to:

```text
data/python_jobs.json
```

Example:

```json
{
    "title": "Senior Python Developer",
    "company": "Payne, Roberts and Davis",
    "location": "Stevens Point, WI"
}
```

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the Playwright browser:

```bash
python -m playwright install chromium
```

## Usage

Run the scraper:

```powershell
python src\scraper.py
```

Example output:

```text
Found jobs: 100
Python jobs: 10
Saved all jobs: 100
Saved Python jobs: 10
```

## Testing

Run the test suite:

```powershell
python -m pytest -v
```

Current test coverage includes:

* Job data parsing
* Keyword filtering
* JSON storage

Example:

```text
tests/test_parser.py::test_parse_job PASSED
tests/test_parser.py::test_filter_jobs PASSED
tests/test_storage.py::test_save_jobs PASSED

3 passed
```

## Purpose

This project demonstrates practical experience with:

* Web scraping
* Browser automation
* HTML element selection
* Data parsing and filtering
* JSON data processing
* Automated testing with pytest
* Structuring a Python scraping project
