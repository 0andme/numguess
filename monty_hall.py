from random import shuffle,choice

repeat_num=5
doors=[0,0,1]
user_choice=0
no_chane_win=0
change_win=0



for i in range(repeat_num):
    shuffle(doors)
    user_choice=choice(doors)
