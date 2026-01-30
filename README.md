# Python CSV Automation – Data Cleaning Script

## Overview
This project demonstrates a real-world Python automation task: cleaning and normalizing CSV data exported from business systems (CRM, ERP, spreadsheets).

The script processes inconsistent input data and produces a clean, standardized output file without introducing artificial values.

This type of task is common in backend maintenance, automation jobs, and data preparation pipelines.

---

## Features
- Trims and normalizes text fields
- Capitalizes names correctly
- Normalizes email addresses to lowercase
- Validates numeric fields safely
- Handles multiple date formats
- Ignores invalid or missing values without breaking the dataset
- Outputs clean data in ISO format (YYYY-MM-DD)

---

## Input Data
The input file simulates a real customer export containing common data quality issues:
- Extra spaces
- Inconsistent email casing
- Missing or invalid ages
- Multiple date formats
- Invalid or empty dates

**File:** `input/sample_input.csv`

---

## Output Data
The output file contains cleaned and normalized data while preserving original business information.

- Valid dates are converted to ISO format
- Invalid or malformed values are left empty
- No assumptions or fabricated values are introduced

**File:** `output/cleaned_output.csv`

---

## Project Structure
```
python-csv-automation/
├── input/
│   └── sample_input.csv
├── output/
│   └── cleaned_output.csv
├── src/
│   └── clean_csv.py
├── requirements.txt
└── README.md
```

---

## Requirements
- Python 3.8+
- No external libraries required (standard library only)

---

## How to Run
1. Clone the repository
2. Ensure Python 3.8+ is installed
3. From the project root, run:

```bash
python src/clean_csv.py
```

The cleaned CSV file will be generated in the `output/` directory.

---

## Use Cases
- Data cleanup and normalization
- Backend maintenance tasks
- Automation scripts for small businesses
- Preparing datasets for import into other systems

---

## Notes
This project is intentionally simple and dependency-free to demonstrate maintainable, production-friendly scripting practices.

