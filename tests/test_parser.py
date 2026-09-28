import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from parser import parse_job, filter_jobs


class MockLocator:
    def __init__(self, text):
        self.text = text

    def inner_text(self):
        return self.text


class MockCard:
    def locator(self, selector):
        data = {
            "h2.title": "Python Developer",
            "h3.company": "Test Company",
            "p.location": "Remote"
        }

        return MockLocator(data[selector])


def test_parse_job():
    job = parse_job(
        card=MockCard()
    )

    assert job["title"] == "Python Developer"
    assert job["company"] == "Test Company"
    assert job["location"] == "Remote"


def test_filter_jobs():
    jobs = [
        {
            "title": "Python Developer",
            "company": "Company A",
            "location": "Remote"
        },
        {
            "title": "Java Developer",
            "company": "Company B",
            "location": "New York"
        },
        {
            "title": "Senior Python Engineer",
            "company": "Company C",
            "location": "London"
        }
    ]

    result = filter_jobs(jobs, "python")

    assert len(result) == 2
    assert result[0]["title"] == "Python Developer"
    assert result[1]["title"] == "Senior Python Engineer"