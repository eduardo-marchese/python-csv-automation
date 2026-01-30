import csv
from datetime import datetime
from pathlib import Path

# File paths
INPUT_FILE = Path("input/sample_input.csv")
OUTPUT_FILE = Path("output/cleaned_output.csv")

# Accepted input date formats
DATE_FORMATS = [
    "%Y-%m-%d",  # 2023-05-12
    "%d/%m/%Y",  # 12/11/2022
    "%Y/%m/%d",  # 2021/08/19
    "%d-%m-%Y",  # 07-09-2023
]


def clean_name(name: str) -> str:
    """Trim spaces and capitalize each word in a name."""
    return " ".join(word.capitalize() for word in name.strip().split())


def clean_email(email: str) -> str:
    """Normalize email to lowercase and remove extra spaces."""
    return email.strip().lower()


def clean_age(age: str) -> str:
    """Return age only if it is a valid integer, otherwise empty."""
    age = age.strip()
    return age if age.isdigit() else ""


def normalize_date(date_str: str) -> str:
    """
    Normalize multiple date formats to ISO (YYYY-MM-DD).
    Invalid or empty dates return an empty string.
    """
    date_str = date_str.strip()
    if not date_str:
        return ""

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return ""


def process_csv() -> None:
    """Read input CSV, clean data, and write normalized output CSV."""
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with INPUT_FILE.open(newline="", encoding="utf-8") as infile, \
         OUTPUT_FILE.open("w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:
            cleaned_row = {
                "name": clean_name(row["name"]),
                "email": clean_email(row["email"]),
                "age": clean_age(row["age"]),
                "country": row["country"].strip(),
                "signup_date": normalize_date(row["signup_date"]),
            }

            writer.writerow(cleaned_row)


if __name__ == "__main__":
    process_csv()
