from openpyxl import Workbook

wb = Workbook()

ws1 = wb.active

ws1.title="첫번째 Sheet"
ws1["A1"] = "Hello World"
ws1["B2"] = "파이썬을 이용한 엑셀 데이터 삽입"

print(ws1["A1"].value)
print(ws1["B2"].value)

wb.save("D:\\new.excel.xlsx")