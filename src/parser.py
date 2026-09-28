def parse_job(card):
    title = card.locator("h2.title").inner_text().strip()
    company = card.locator("h3.company").inner_text().strip()
    location = card.locator("p.location").inner_text().strip()

    return {
        "title": title,
        "company": company,
        "location": location
    }


def filter_jobs(jobs, keyword):
    keyword = keyword.lower()

    return [
        job
        for job in jobs
        if keyword in job["title"].lower()
    ]