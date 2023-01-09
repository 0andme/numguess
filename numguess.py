# randint 기능 import
from random import randint

# 랜덤값 생성
answer=randint(1,100)

# 사용자로부터 이름 입력 받기 
user_name=input('이름을 입력해주세요>')

# 사용자 환영 인사 출력
print(f"안녕하세요 {user_name}님")

# 사용자로부터 예측값 입력 받기
user_guess=int(input('1부터 100사이의 정답을 추측해주세요 >'))

# 결과 출력 
print(f"정답은 바로 {answer}였습니다!!")
print(f"{user_name}님의 예측값 {user_guess}는 과연 정답과 일치했을까요? {user_guess==answer}")

