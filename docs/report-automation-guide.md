# Excel Report Automation — Starter Guide

A starter guide to automating a repetitive monthly report: the
kind of report an IT team builds by hand every month in a
spreadsheet — a list of rows (date, department, category,
amount), then totals by category and by department. This guide
explains the shape of the work and the checks to run. All
examples are fictional samples for learning. This template does
not describe any real organisation, real figures, or production
use.

## What report automation is

The same report, built the same way, every month: collect the
rows, group them, add them up, and present the totals. Doing it
by hand is slow and error-prone — a missed row or a wrong cell
reference changes the total silently. A small script does the
same grouping and adding every time, from the same input file,
so the result is repeatable. The script in this repo,
`scripts/report-summary.py`, is a starter example of exactly
that: it reads a CSV and prints the totals by category and by
department.

## The source data shape

The script expects a CSV with these columns:

| Column | Meaning | Example (fictional) |
|--------|---------|---------------------|
| date | The date of the row | 2026-11-03 |
| department | Which team the row belongs to | Support |
| category | What kind of row it is | Hardware |
| amount | The value, in your currency | 240.00 |
| note | A short human note (optional) | Sample row — replacement keyboard set |

Keep the shape fixed: same column names, same order, one row
per item, amounts as plain numbers with no currency symbols or
thousand separators. A spreadsheet export usually needs a quick
tidy-up to reach this shape — that tidy-up is part of the work,
and it is worth a checklist of its own.

## The monthly workflow

1. **Collect** — gather the month's rows into one CSV in the
   shape above. One file per month, named by month, so nothing
   gets mixed across months.
2. **Check the input** — before running anything, eyeball the
   CSV: are all rows from the right month? Are amounts numbers,
   not text? Are there duplicate rows (the same row pasted
   twice)? Duplicates are the most common cause of a wrong
   total.
3. **Run** — run the script on the file:
   `python3 scripts/report-summary.py excel-report-automation-starter.csv`
4. **Cross-check** — recount the total in a spreadsheet with a
   plain SUM over the amount column. The script total and the
   spreadsheet total must match exactly. If they do not, the
   input file is wrong, not the arithmetic.
5. **Present** — paste the printed tables into the report, or
   rebuild the same tables in the spreadsheet from the checked
   CSV. Keep the CSV with the report so the numbers can be
   re-derived later.

## Checks that catch real mistakes

- **Row count first.** Count the rows in the CSV before and
  after any tidy-up. If the count changes, find out why before
  running the script.
- **Totals by two cuts.** Group by category and by department.
  Both cuts must add up to the same grand total. In the sample
  data: Hardware 960.00 + Software 570.00 + Services 350.00 =
  1,880.00, and Support 1,270.00 + Operations 610.00 = 1,880.00.
  If the two cuts disagree, a row is miscategorised or missing.
- **Largest item sanity check.** Look at the largest single
  amount and the largest group. Do they make sense for the
  month? A single row bigger than a whole category usually
  means a typo (an extra zero).
- **Keep the source file.** Never edit the totals by hand after
  the script runs. If a number is wrong, fix the source CSV and
  re-run — that way the report can always be rebuilt from the
  same input.

## From script output to spreadsheet

The script prints plain text, which is deliberate: it is easy
to check and easy to paste. In a real workflow, the next step
is to put the same tables into a spreadsheet — either by
pasting the printed tables, or by using a spreadsheet's own
pivot-table feature on the same CSV. Either way, the CSV is
the single source of truth, and the checks above still apply:
the spreadsheet pivot total must equal the script total.

## What this template does not do

- It does not read Excel files directly — it reads plain CSV,
  which any spreadsheet can export.
- It does not handle multiple currencies, tax, or exchange
  rates — those belong in the source data, agreed before the
  report is built.
- It does not send, email, or publish the report. That step is
  separate and belongs to your own workflow.

## Sample / Demo notice

All departments, categories, dates, and amounts in this repo
are fictional samples for learning. The diagram in
`docs/diagram.png` is a locally generated illustration labelled
"Sample / Demo" — it is not a screenshot of a real system, and
this template does not claim any production use.
