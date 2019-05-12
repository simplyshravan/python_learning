import xlsxwriter

 # Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()

 # Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

 # Add a number format for cells with money.
money = workbook.add_format({'num_format': '$#,##0'})

#Setting width of columns to 12                        
worksheet.set_column('B:K', 12)

#setting height of row
worksheet.set_row(0, 18)
worksheet.set_row(1, 24)
                             
#defining Merge format for merged cells
merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'font_name':'Arial',
    'font_size':'14'})

merge_format2 = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'font_name':'Arial',
    'font_size':'18'})
bottom_border=workbook.add_format({
        'bottom':1})

#merging cells with text and format

#Row 4 headers example
worksheet.write('B4', 'Carrier Name', bold)
worksheet.write('G4', 'Date', bold)
worksheet.write('C4','', bottom_border)
worksheet.write('D4','', bottom_border)
worksheet.write('E4','', bottom_border)
worksheet.write('F4','', bottom_border)
worksheet.write('H4','', bottom_border)
worksheet.write('I4','', bottom_border)

#setting width of columns
worksheet.set_column('B:B', 14)
worksheet.set_column('C:C', 17)
worksheet.set_column('D:D', 10)
worksheet.set_column('E:E', 10)
worksheet.set_column('F:F', 13)
worksheet.set_column('G:G', 35)
worksheet.set_column('H:H', 11.5)
worksheet.set_column('I:I', 12)
worksheet.set_column('J:J', 14)
worksheet.set_column('K:K', 14)
worksheet.set_column('L:L', 24)


all_border=workbook.add_format({
        'bold': 1,
        'border':1,
        'text_wrap':1,
        'align': 'center',
        'valign': 'bottom'})
#adding Data headers 




 # Some data we want to write to the worksheet.
expenses = (
     ['Rent', 1000],
     ['Gas',   100],
     ['Food',  300],
     ['Gym',    50],
 )

 # Start from the first cell below the headers.
row = 7
col = 1

 # Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost, money)
    row += 1

 # Write a total using a formula.
worksheet.write(row, 0, 'Total',       bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()
