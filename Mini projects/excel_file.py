from openpyxl import Workbook

workbook = Workbook()
current_sheet = workbook.active

current_sheet['A1'] = '1'
current_sheet['A2'] = 'Python'
current_sheet['B1'] = '2'
current_sheet['B2'] = 'SOftUni'
current_sheet['C1'] = '3'
current_sheet['C3'] = 'Programing'

workbook.save(filename='../conditional_statements_lecture/example_exel.xlsx')
