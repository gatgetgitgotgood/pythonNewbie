'''
1. my_bank.txt파일을 불러와 현재 통장 잔액을 불러오는 함수 --> load_account()
2.  금액을 입력 받아 계속 저금을 하는 프로그램을 만들어보자.  --> save(balance)
    저축을 하는 함수 save(balance)는 현재 잔액(balance)를 인수로 받고
    저축액 amount을 입력받아 현재잔액(balance)를 amount만큼 증가
    amount 입력에 -1을 입력하면 적금 종료

	↓ 실행화면 ↓
    얼마를 저축하시겠습니까?(종료는 –1): 200
    지금까지의 저축액은 200입니다.
    얼마를 저축하시겠습니까?(종료는 –1): 50
    지금까지의 저축액은 250입니다.
    얼마를 저축하시겠습니까?(종료는 –1): -1
    프로그램을 종료합니다.
3. my_bank.txt에 현재 시작과 저축액을 기록함 -->write_account(balance)
'''
import datetime

def load_account():
    with open('./my_bank.txt','r') as f:
        return int(list(f)[-1].split(':')[-1].strip())

def save(balance):
    chk=balance
    while True:
        amount=int(input('얼마를 적금하시겠습니까?(종료:-1)'))
        if amount==-1:
            print('프로그램을 종료합니다.')
            break
        balance += amount #왜 elif나 else로 이 블럭이 안 끝나지
        print(f'지금까지 저축액은 {balance}원입니다.')
    if chk==balance:
        print('적금을 하나도 하지 않았습니다')
        
    else:
        print(f'통장에 적금액{balance}을 기록하였습니다.')
        write_account(balance)

def write_account(balance):
    # 현재 날짜와 시간을 가져옵니다.
    current = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('./my_bank.txt','a') as f:
        f.write(f'{current} balance:{balance}\n')

        
    
if __name__=='__main__':
    balance=load_account() #통장 불러와서 현재 잔액 불러오기
    print('현재 잔액:',balance) #현재 잔액 확인
    # save(balance) #적금하고 적금끝나면 통장 기록
