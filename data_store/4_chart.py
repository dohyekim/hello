 # 상위 Top10의 `좋아요 수`는 BarChart로, `좋아요 차이 수`는 ScatterChart로 세번째 시트에 작성하시오.
import openpyxl
from openpyxl.chart import (
    Reference,
    BarChart,
    Series,
    ScatterChart
)

book = openpyxl.load_workbook("./meltop100.xlsx")
sheet3 = book.create_sheet()
sheet3.title = "Sheet 3"

rows = []
n = 0
with open("./melon_top.csv", mode = "r", encoding="euc-kr") as file:
    for line in file:
        if n == 0:
            rows.append([line.split(',')[1], line.split(',')[3], line.split(',')[4]])
            n = n + 1
            continue
        else:
            rows.append([line.split(',')[1], int(line.split(',')[3]), int(line.split(',')[4])])

        if len(rows) == 11:
            break



for row in rows:
    sheet3.append(row)

data = Reference(sheet3, min_col=2, 
		min_row=1, max_col=2, max_row=10)
categ = Reference(sheet3, min_col=1,
				 min_row=1, max_row=10)

chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categ)

chart.legend = None  
chart.varyColors = True
chart.title = "좋아요"
sheet3.add_chart(chart, "C13")

book.save("./meltop100.xlsx")

chart = ScatterChart()
chart.style = 13
chart.x_axis.title = 'Title'
chart.y_axis.title = 'Like'

xvalues = Reference(sheet3, min_col=1,
			 min_row=2, max_row=10)

values = Reference(sheet3, 
            min_col=3, 
            min_row=1, 
            max_row=10)
series = Series(values, xvalues, 
            title_from_data=True)
chart.series.append(series)

sheet3.add_chart(chart, "K13")
book.save("./meltop100.xlsx")