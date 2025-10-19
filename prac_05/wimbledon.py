"""
Emails
Estimate: 30 minutes
Actual:    minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data file and print details."""
    records = load_records(FILENAME)


def load_records(filename):
    """Load records from file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
