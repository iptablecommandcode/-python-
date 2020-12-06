"""
생일 입력후 성별 나이 표시
개발 프로그램 : VSCode
작성자 : 박치원
이메일 : iptablecommandcode@gmail.com
"""
import sys
from datetime import datetime
from easygui import*

# 변수(메뉴,최종 나이,종료)
check = 1
Age = 0
StopMessage = ""

# 처음 시작
print("주민등록번호에서 성별과 나이를 나타내는 숫자를 출력하는 프로그램 입니다.\n")
print("종료하시려면 n을 입력하세요.")

Pin_No = input("주민 번호 13자리를 입력하십시오.")

# 종료
if StopMessage == 'n':
    sys.exit()

# 메뉴 만들기
while check == 1:
    # 주민번호 성별 자리수 검색
    if len(Pin_No) > 13:
        msgbox("13자리가 초과 입니다.")
        Pin_No = input("주민 번호 13자리를 입력하십시오.")

    elif len(Pin_No) > 13:
        msgbox("13자리가 미만 입니다.")
        Pin_No = input("주민 번호 13자리를 입력하십시오.")
        
    elif len(Pin_No) == 13:
        #나이 계산
        Age = int(Pin_No) / 100000000000
        Age = int(Age)

        # 성별 자리수 계산
        Gender =  int(Pin_No) % 10000000 / 1000000
        Gender = int(Gender)

        #출생 년도 계산(19xx,20xx)

        if Gender == 1:
            Age = Age + 1900
        if Gender == 2:
            Age = Age + 1900
        if Gender == 3:
            Age = Age + 2000
        if Gender == 4:
            Age = Age + 2000

        # 나이 계산
        Age = int(datetime.today().strftime("%Y")) - Age

        # 성별 총 출력
        if Gender == 1:
            msgbox("나이는 {} 살 입니다.\n성별은 남성 입니다.".format(Age))
        if Gender == 2:
            msgbox("나이는 {} 살 입니다.\n성별은 여성 입니다.".format(Age))
        if Gender == 3:
            msgbox("나이는 {} 살 입니다.\n성별은 남성 입니다.".format(Age))
        if Gender == 4:
            msgbox("나이는 {} 살 입니다.\n성별은 여성 입니다.".format(Age))
            
        check = 0