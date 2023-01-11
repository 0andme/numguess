from random import shuffle,choice

repeat_num=5
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
    user_choice=choice(doors)
    if(user_choice==1):
        change_win+=1
    
