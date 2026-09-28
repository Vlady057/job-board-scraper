import json

from src import storage


def test_save_jobs(tmp_path, monkeypatch):
    jobs = [
        {
            "title": "Python Developer",
            "company": "Test Company",
            "location": "Chisinau",
        }
    ]

    output_file = tmp_path / "jobs.json"

    monkeypatch.setattr(storage, "OUTPUT_FILE", str(output_file))

    storage.save_jobs(jobs)

    with open(output_file, "r", encoding="utf-8") as file:
        saved_jobs = json.load(file)

    assert saved_jobs == jobs