# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''Emit the table headings'''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''Emit single row of data'''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''Emit a table in plain-text format'''

    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<td>{h}</td>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(format):
    if format == 'txt':
        formatter = TextTableFormatter()
    elif format == 'csv':
        formatter = CSVTableFormatter()
    elif format == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'unsupported format {format}')
    return formatter

def print_table(objects, attributes, formatter):
    formatter.headings(attributes)
    for o in objects:
        rowdata = [str(getattr(o, a)) for a in attributes]
        formatter.row(rowdata)