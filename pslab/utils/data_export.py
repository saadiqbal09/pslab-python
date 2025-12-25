import csv
import json

def export_to_csv(data, filename):
    """
    data: list of dictionaries
    """
    if not data:
        return

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def export_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
