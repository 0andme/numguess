# randint 기능 import
from random import randint
from time import sleep

# 랜덤값 생성
answer=randint(1,100)
print(f'{answer}')

# 사용자로부터 이름 입력 받기 
user_name=input('이름을 입력해주세요>')

# 사용자 환영 인사 출력
print(f"안녕하세요 {user_name}님")

# 사용자로부터 예측값 입력 받기
user_guess=int(input('1부터 100사이의 정답을 추측해주세요 >'))

# 결과 출력 
# 사용자의 예측값과 정답 비교
print(f"당신은 {user_guess}를 골랐습니다")

if user_guess==answer:
    print('----------------------------------------------')
    sleep(1)
    print('----------------------------------------------')
    sleep(1)
    print('----------------------------------------------')
    sleep(1)
    print(f'{user_name}님, 축하드립니다 정답 {answer}를 맞추셨습니다')
elif user_guess>answer:
    print(f'{user_guess}는 정답보다 큰 수입니다')
else: 
    print(f'{user_guess}는 정답보다 작은 수입니다')



