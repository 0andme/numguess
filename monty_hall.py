from random import shuffle,choice

repeat_num=10000
doors=[0,0,1]
user_choice=0
no_change_win=0
change_win=0



for i in range(repeat_num):
    shuffle(doors)
    user_choice=choice(doors)
    if(user_choice==1):
        no_change_win+=1
    # 사용자가 문을 변경
    else:
        change_win+=1

print(f"반복 횟수 : {repeat_num} / 문 변경시 이길 확률 : {change_win/repeat_num*100}/ 문 미 변경시 이길 확률: {no_change_win/repeat_num*100}")