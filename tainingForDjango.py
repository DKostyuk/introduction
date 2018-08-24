import openpyxl

wb = openpyxl.load_workbook(filename='./address_add_01.xlsx')
# print(wb.get_sheet_names())
anotherSheet = wb.active
# anotherSheet
# print(anotherSheet)
# Retrieve the value of a certain cell
a = anotherSheet['A1'].value
print(a)

# Select element 'B2' of your sheet
c = anotherSheet['B2']
print(c)

# Retrieve the row number of your element
c1 = c.row
print('# Retrieve the row number of your element  ', c1)

# Retrieve the column letter of your element
c2 = c.column
print(c2)

# Retrieve the coordinates of the cell
c3 = c.coordinate
print(c3)

data = anotherSheet.values
data = list(data)
print('data   ', data)


# inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
# c = []
# for line in inFile:
#     a = line.split()
#     a[2] = int(a[2])
#     a[3] = int(a[3])
#     c.append(a)
# for j in range(9, 12):
#     k = 0
#     s = 0
#     f = []
#     for i in range(len(c)):
#         if c[i][2] == j:
#             f.append(c[i][3])
#     print(max(f), end=' ', file=outFile)
# inFile.close()
# outFile.close()
