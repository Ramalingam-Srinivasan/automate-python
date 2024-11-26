from openpyxl.worksheet import worksheet
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


#loading workbook and selecting the active working sheet
wb = load_workbook('requirement/sales_record.xlsx')
ws: worksheet = wb['record']

#setting the min and max columns and rows to work
min_column = ws.min_column
max_column = ws.max_column
min_row = ws.min_row
max_row = ws.max_row
#ws['A11'] = '=SUM(A2:A10)'



for i in range(min_column,max_column+1):
   # print(i)
   #getting the column letter using below attribute get_column_letter
   letter = get_column_letter(i)
   # applying formulae to the  cell
   ws[f'{letter}{max_row+1}'] = f'=SUM({letter}{min_row+1}:{letter}{max_row})'
   #applying rupee sign to the sum valued cell
   ws[f'{letter}{max_row + 1}'].style = 'Currency'

#saving the worksheet and workbook
wb.save('requirement/my_report.xlsx')



