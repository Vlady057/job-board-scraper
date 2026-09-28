from playwright.sync_api import sync_playwright

from parser import parse_job, filter_jobs
from storage import save_jobs


URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)

        cards = page.locator("div.card-content")
        jobs = []

        for i in range(cards.count()):
            job = parse_job(cards.nth(i))
            jobs.append(job)

        browser.close()

    return jobs


if __name__ == "__main__":
    jobs = scrape_jobs()

    print(f"Found jobs: {len(jobs)}")

    save_jobs(jobs, "data/jobs.json")

    python_jobs = filter_jobs(jobs, "python")

    print(f"Python jobs: {len(python_jobs)}")

    save_jobs(python_jobs, "data/python_jobs.json")

    print(f"Saved all jobs: {len(jobs)}")
    print(f"Saved Python jobs: {len(python_jobs)}")