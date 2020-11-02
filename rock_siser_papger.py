import random
import sys

Re = 1
com = ['가위', '바위', '보']
while(Re == 1):
    rec = 0
    mine = 0
    comp = 0

    print('가위바위보 게임입니다.!')
    while mine not in['가위', '바위', '보']:
        mine = input('가위 / 바위 /보 중에 선택해주세요')
    comp = random.choice(com)
    print('너는',mine,'를 내었고, 컴퓨터는',comp, '를 내었네요')
    if(mine == comp):
        print('따라서 당신은 비겼습니다.')
    else:
        if(mine == '가위'):
            if(comp == '바위'):
                print('따라서 당신은 졌습니다.')
            if(comp == '보'):
                print('따라서 당신은 이겼습니다.')
        else:
            if(mine == '바위'):
                if(comp == '보'):
                    print('따라서 당신은 졌습니다.')
                if(comp == '가위'):
                    print('따라서 당신은 이겼습니다.')
            else:
                if(comp == '가위'):
                    print('따라서 당신은 졌습니다.')
                if(comp == '바위'):
                    print('따라서 당신은 이겼습니다.')

        while rec not in ['예','아니오']:
            rec = input('다시 시작 할 것입니까? (예, 아니오)')
            if(rec == '예'):
                re = 1
            else:
                print('프로그램을 종료합니다.')
                sys.exit()