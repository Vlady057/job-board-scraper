# Job Board Scraper

Python web scraper for collecting job listings from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) website.

The project uses **Playwright** for browser automation, separates scraping, parsing, and storage logic, and includes unit tests with **pytest**.

## Features

* Scrapes job listings using Playwright
* Extracts:

  * job title
  * company
  * location
* Filters jobs by keyword
* Saves all jobs to JSON
* Saves filtered jobs to a separate JSON file
* Uses a modular project structure
* Includes unit tests for parsing and storage
* Uses mock objects to test parsing without launching a browser

## Technologies

* Python 3
* Playwright
* pytest
* JSON

## Project Structure

```text
job-board-scraper/
│
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── parser.py
│   └── storage.py
│
├── tests/
│   ├── test_parser.py
│   └── test_storage.py
│
├── data/
│   ├── jobs.json
│   └── python_jobs.json
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Architecture

The project follows a simple separation of responsibilities:

```text
Website
   │
   ▼
scraper.py
   │
   │ Playwright
   ▼
parser.py
   │
   │ parsed job data
   ▼
storage.py
   │
   ▼
JSON files
```

### `scraper.py`

Responsible for browser automation and collecting job cards from the website.

### `parser.py`

Responsible for extracting job information and filtering jobs by keyword.

### `storage.py`

Responsible for saving and loading job data in JSON format.

### `tests/`

Contains unit tests for the parser and storage modules.

## Installation

Clone the repository:

```bash
git clone https://github.com/Vlady057/job-board-scraper.git
cd job-board-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Install the Playwright Chromium browser:

```powershell
playwright install chromium
```

## Usage

Run the scraper from the project root:

```powershell
python -m src.scraper
```

The scraper collects all available jobs and then filters jobs containing `python` in the job title.

Example output:

```text
Found jobs: 100
Python jobs: 10
Saved all jobs: 100
Saved Python jobs: 10
```

## Output

All collected jobs are saved to:

```text
data/jobs.json
```

Filtered Python jobs are saved to:

```text
data/python_jobs.json
```

Example job:

```json
{
    "title": "Python Developer",
    "company": "Example Company",
    "location": "Remote"
}
```

## Testing

Run all tests:

```powershell
python -m pytest -v
```

Expected result:

```text
tests/test_parser.py::test_parse_job PASSED
tests/test_parser.py::test_filter_jobs PASSED
tests/test_storage.py::test_save_jobs PASSED

3 passed
```

The tests cover:

* job data parsing
* keyword filtering
* JSON storage

The parser tests use mock objects instead of launching a real browser, keeping the tests fast and independent of the target website.

## Example Workflow

```text
1. Launch Playwright
        ↓
2. Open the job board
        ↓
3. Find job cards
        ↓
4. Parse title, company and location
        ↓
5. Store all jobs in a list
        ↓
6. Filter Python-related jobs
        ↓
7. Save results to JSON
        ↓
8. Run tests
```

## Repository

[GitHub — Vlady057/job-board-scraper](https://github.com/Vlady057/job-board-scraper)
