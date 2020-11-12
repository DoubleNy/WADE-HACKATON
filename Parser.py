import xlrd
from xlrd.sheet import ctype_text

class Parser:
    def __init__(self):
        self.parsed_sheets = dict()
        self.parsed_sheets_names = []

    def get_parsed(self):
        return self.parsed_sheets_names, self.parsed_sheets

    def parse(self, file):
        workbook = xlrd.open_workbook(file, encoding_override='cp1252')

        self.parsed_sheets_names = workbook.sheet_names()

        for sheet_number in range(0, len(self.parsed_sheets_names)):
            sheet = workbook.sheet_by_name(self.parsed_sheets_names[sheet_number])

            start_row = 2
            num_cols = sheet.ncols
            fields = []
            for col_idx in range(0, num_cols):
                cell_obj = sheet.cell(start_row, col_idx)
                fields.append(cell_obj.value)

            # print(fields)
            # print(num_cols)
            new_parsed_sheet = []

            for row_idx in range(start_row + 1, sheet.nrows):
                new_obj = dict()
                for col_idx in range(0, num_cols):  # Iterate through columns
                    cell_obj = sheet.cell(row_idx, col_idx)
                    new_obj[fields[col_idx]] = (cell_obj.value, cell_obj.ctype)
                new_parsed_sheet.append(new_obj)

            self.parsed_sheets[self.parsed_sheets_names[sheet_number]] = new_parsed_sheet
