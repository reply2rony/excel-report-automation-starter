#!/usr/bin/env python3
"""Starter learning template: summarise a monthly report CSV.

Usage:
    python3 scripts/report-summary.py excel-report-automation-starter.csv

Reads a CSV with columns: date, department, category, amount, note.
Prints the total, the totals grouped by category, and the totals
grouped by department. Sample data only; it is not a production
tool. Always check the totals against a manual spreadsheet sum
before using them in a real report.
"""
import argparse
import csv
import sys
from collections import defaultdict


def load_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"date", "department", "category", "amount"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            print(f"CSV must have columns: {', '.join(sorted(required))}")
            raise SystemExit(1)
        for line_no, row in enumerate(reader, start=2):
            try:
                amount = float(row["amount"])
            except (TypeError, ValueError):
                print(f"Line {line_no}: amount '{row['amount']}' is not a number.")
                raise SystemExit(1)
            rows.append({
                "date": row["date"].strip(),
                "department": row["department"].strip(),
                "category": row["category"].strip(),
                "amount": amount,
            })
    return rows


def summarise(rows):
    by_category = defaultdict(float)
    by_department = defaultdict(float)
    for row in rows:
        by_category[row["category"]] += row["amount"]
        by_department[row["department"]] += row["amount"]
    return by_category, by_department


def print_table(title, groups):
    print(title)
    for name in sorted(groups, key=lambda k: groups[k], reverse=True):
        print(f"  {name:<15} {groups[name]:>10.2f}")
    print()


def main():
    ap = argparse.ArgumentParser(description="Summarise a monthly report CSV.")
    ap.add_argument("csv_file", help="path to the CSV file to summarise")
    args = ap.parse_args()

    try:
        rows = load_rows(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        raise SystemExit(1)

    if not rows:
        print("No data rows found in the CSV.")
        raise SystemExit(1)

    total = sum(r["amount"] for r in rows)
    by_category, by_department = summarise(rows)

    print(f"Rows: {len(rows)}")
    print(f"Total: {total:.2f}")
    print()
    print_table("By category:", by_category)
    print_table("By department:", by_department)

    largest_category = max(by_category, key=by_category.get)
    largest_department = max(by_department, key=by_department.get)
    print(f"Largest category: {largest_category} ({by_category[largest_category]:.2f})")
    print(f"Largest department: {largest_department} ({by_department[largest_department]:.2f})")
    print()
    print("Check before using: recount these totals in a spreadsheet.")
    print("A script total is only as good as the rows fed into it.")


if __name__ == "__main__":
    main()
