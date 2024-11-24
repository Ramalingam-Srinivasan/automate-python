from openpyxl import load_workbook
from openpyxl.chart import BarChart,Reference


wb= load_workbook('requirement/pivot_table.xlsx')
sheet = wb['report']
barchart = BarChart()
data = Reference(sheet,2,2,13,15)
categories = Reference(sheet,1,1,1,15)
barchart.add_data(data,titles_from_data=True)
barchart.set_categories(categories)
sheet.add_chart(barchart,'O2')
#barchart.title('salesDetails')
#barchart.style(5)
wb.save('requirement/barchart.xlsx')