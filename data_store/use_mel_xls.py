import openpyxl
from pprint import pprint

book = openpyxl.load_workbook("./melon_top_xls.xlsx")

# Sheet 1
sheet = book.worksheets[0]

data = []

for r in sheet.rows:
    data.append([ r[0].value, r[1].value, r[2].value, r[3].value ])

del data[0]    # header 제거
del data[50]
del data[50]
del data[100]

# pprint(data)
data = sorted(data, key=lambda x : x[3], reverse=True)

pprint(data)