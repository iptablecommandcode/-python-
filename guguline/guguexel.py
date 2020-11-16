from openpyxl import Workbook

wb = Workbook()

ws1 = wb.active

ws1.title="Park ChiWon"

for i in range(2,10):
    ASCII_String = chr(i+63)
    for j in range(1,10):
        guguLine = ""
        guguLine = guguLine + str("%2d X %2d = %2d\n"%(i,j,j*i))
        ws1["{}{}".format(str(ASCII_String),j)] = guguLine

wb.save("D:\\new.excel.xlsx")