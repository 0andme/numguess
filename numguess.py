# randint 기능 import
from random import randint
from time import sleep


# 게임 기회 지정
user_chance=10

# 랜덤값 생성
answer=randint(1,100)
print(f'{answer}')

def game_open():
    """
    game_open
    사용자로부터 이름을 입력받고 환영인사를 출력 
    return user_name
    """
    # 사용자로부터 이름 입력 받기
    user_name=input('이름을 입력해주세요>')
    # 사용자 환영 인사 출력
    print(f"안녕하세요 {user_name}님")
    return user_name


def game_start(answer):
    """
    game_start
    총 10번의 기회 동안
    사용자에게 예측값을 받고
    결과를 리턴 
    """
    # 총 10번 수행
    for i in range(user_chance):
        # 사용자로부터 예측값 입력 받기
        user_guess=int(input(f'{user_chance-i}번째 기회: 1부터 100사이의 정답을 추측해주세요 >'))
        if(user_guess==answer):
            return True 
        elif user_guess>answer:
            print(f'{user_guess}는 정답보다 큰 수입니다')
        else: 
            print(f'{user_guess}는 정답보다 작은 수입니다')
    
    return False

def game_end(user_name,res):
    """
    game_end
    게임결과에 따른 메시지 출력
    """
    if res:
        print(f'{user_name}님, 축하드립니다 정답 {answer}를 맞추셨습니다')
    else:
        print(f"{user_chance}번의 기회가 있었지만 정답{answer}를 맞추지 못했습니다")

user_name=game_open()
res=game_start(answer)
game_end(user_name,res)


