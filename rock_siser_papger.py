"""
가위바위보 추가 제작
가위바위보 총 플레이 계산, 승리,패배,무승부 계산 추가
개발 프로그램 : VSCode
작성자 : 박치원
이메일 : iptablecommandcode@gmail.com
"""
import random
import sys

Re = 1
com = ['가위', '바위', '보']
    # 가위바위 카운트 전역 처리
counttot = 0
countwin = 0
countlose = 0
countdraw = 0

while(Re == 1):
    rec = 0
    mine = 0
    comp = 0
    

    print('가위바위보 게임입니다.!')
    # 가위바위보 글자 입력 하지 않을시
    while mine not in['가위', '바위', '보']:
        mine = input('가위 / 바위 /보 중에 선택해주세요')
    
    #컴퓨터 가위바위보 랜덤
    comp = random.choice(com)
    # 총 가위바위보 카운트
    counttot += 1

    print('너는',mine,'를 내었고, 컴퓨터는',comp, '를 내었네요')
    if(mine == comp):
        print('따라서 당신은 비겼습니다.')
        countdraw += 1
    else:
        if(mine == '가위'):
            if(comp == '바위'):
                print('따라서 당신은 졌습니다.')
                countlose += 1
            if(comp == '보'):
                print('따라서 당신은 이겼습니다.')
                countwin += 1
        else:
            if(mine == '바위'):
                if(comp == '보'):
                    print('따라서 당신은 졌습니다.')
                    countlose += 1
                if(comp == '가위'):
                    print('따라서 당신은 이겼습니다.')
                    countwin += 1
            else:
                if(comp == '가위'):
                    print('따라서 당신은 졌습니다.')
                    countlose += 1
                if(comp == '바위'):
                    print('따라서 당신은 이겼습니다.')
                    countwin += 1

        while rec not in ['예','아니오']:
            rec = input('다시 시작 할 것입니까? (예, 아니오)')
            if(rec == '예'):
                re = 1
            else:
                print('프로그램을 종료합니다.')
                print('당신은 총',counttot,'번 하였고 승리는 총',countwin,'패배는 총',countlose,'무승부는 총',countdraw)
                sys.exit()