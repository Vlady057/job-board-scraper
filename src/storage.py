import json


OUTPUT_FILE = "data/jobs.json"


def save_jobs(jobs, filename=None):
    if filename is None:
        filename = OUTPUT_FILE

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(jobs, file, ensure_ascii=False, indent=4)


def load_jobs(filename=None):
    if filename is None:
        filename = OUTPUT_FILE

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)