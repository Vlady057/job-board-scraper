import json

from src import storage


def test_save_jobs(tmp_path, monkeypatch):
    output_file = tmp_path / "jobs.json"

    monkeypatch.setattr(
        storage,
        "OUTPUT_FILE",
        str(output_file)
    )

    jobs = [
        {
            "title": "Python Developer",
            "company": "Test Company",
            "location": "Remote"
        }
    ]

    storage.save_jobs(jobs)

    with open(output_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == jobs