# randint 기능 import
from random import randint

# 랜덤값 생성
answer=randint(1,100)

# 사용자로부터 이름 입력 받기 
user_name=input('이름을 입력해주세요>')

# 사용자 환영 인사 출력
print(f"안녕하세요 {user_name}님")

