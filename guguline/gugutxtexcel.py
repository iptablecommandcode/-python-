from openpyxl import Workbook

# 변수선언 초기화
guguLine = ""

wb = Workbook()

ws1 = wb.active

ws1.title="Park ChiWon"

# 구구단 반복문
for i in range(2,10):
    # file
    f = open("D:\{}단.txt".format(i),'w')
    guguLine = guguLine + ("# %5d단 #\n"%i)
    f.write(guguLine)

    guguLine = ""
    ASCII_String = chr(i+63)

    for j in range(1,10):
        guguLine = ""
        # excel
        guguLine = guguLine + str("%2d X %2d = %2d\n"%(i,j,j*i))
        f.write(guguLine)
        ws1["{}{}".format(str(ASCII_String),j)] = guguLine
        
# 반복문 실행후 파일 저장과 종료
f.close()
wb.save("D:\\new.excel.xlsx")