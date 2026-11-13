# Excel Report Automation Starter

A starter learning template for automating a repetitive monthly
Excel-style report: take a plain CSV of rows (date, department,
category, amount) and produce the summary tables you would normally
build by hand in a spreadsheet — totals by category, totals by
department, and a monthly total. It is a learning template with
fictional sample data only. It is not a production tool, it makes
no claim about any real organisation, and it contains no real
company data and no invented metrics.

## What it is

- `docs/report-automation-guide.md` — the guide: what a report
  automation does, how to shape the source data, the checks to
  run before trusting a summary, and how to turn the output into
  a spreadsheet.
- `excel-report-automation-starter.csv` — a small fictional
  sample data file: made-up rows for one sample month, so you
  can run the script and see the shape of the output.
- `scripts/report-summary.py` — a starter Python script that
  reads a CSV in the sample shape and prints the summary tables.
  Labelled a starter learning template; it is not a production
  tool.

## How to use

1. Read `docs/report-automation-guide.md` first — it explains
   the source-data shape and the checks to run.
2. Run the script on the sample data:

```bash
python3 scripts/report-summary.py excel-report-automation-starter.csv
```

3. Copy the printed tables into a spreadsheet, or save the
   output to a text file and paste it into a report:

```bash
python3 scripts/report-summary.py excel-report-automation-starter.csv > monthly-summary.txt
```

4. Try the script on your own copy of the CSV shape (your own
   rows, your own month) and compare the totals with a manual
   spreadsheet sum before trusting them.

## What the sample output looks like

Running the script on the sample file gives, for the sample
month (12 fictional rows):

- Total: 1,880.00 across 12 rows
- Largest category: Hardware (960.00)
- Largest department: Support (1,270.00)

Those numbers come from the fictional sample rows in the CSV,
not from any real organisation. Recount them yourself with the
script — that is the point of the exercise.

## Sample / Demo notice

All departments, categories, dates, and amounts in this repo
are fictional samples for learning. The diagram in
`docs/diagram.png` is a locally generated illustration labelled
"Sample / Demo" — it is not a screenshot of a real system, and
this template does not claim any production use.

## License

MIT — see `LICENSE`.
