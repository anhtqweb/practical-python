# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimeter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError("select arguments require column headers")
    
    if isinstance(file, str):
        raise RuntimeError("File path is passed in instead of file object")

    rows = csv.reader(file, delimiter=delimeter)

    if has_headers:
        headers = next(rows)

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    
    records = []
    for rowno, row in enumerate(rows):
        if not row:
            continue

        try:
            if indices:
                row = [row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {rowno}: Could not convert {row}')
                print(f'Row {rowno}: Reason {e}')

    return records