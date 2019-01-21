import openpyxl
import csv, codecs
import time

book = openpyxl.Workbook()
sheet = book.active
sheet.title = "sheet 1"

book.save("./meltop100.xlsx")

data = []
fp = codecs.open("./melon_top.csv", "r", "euc-kr")

reader = csv.reader(fp, delimiter = ",", quotechar = '"')
for line in reader:
    data.append([line[0], line[1], line[2], line[3], line[4]])

header = data[0]

columns = "ABCDE"

for i in range(len(header)):
    sheet["{}1".format(columns[i])] = header[i]
    sheet["{}102".format(columns[i])] = data[101][i]

for i in range(1, len(data) - 1):
    sheet["A{}".format(i + 1)] = int(data[i][0])

for i in range(1, len(data)):
    sheet["B{}".format(i + 1)] = data[i][1]
    sheet["C{}".format(i + 1)] = data[i][2]
    sheet["D{}".format(i + 1)] = int(data[i][3])
    sheet["E{}".format(i + 1)] = int(data[i][4])

book.save("./meltop100.xlsx")