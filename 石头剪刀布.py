import random
player=int(input("石头输入0，剪刀输入1，布输入2"))
computer=random.randint(0,2)
if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print("You are win")
elif (player==computer):
    print("You are deuce!")
else:
    print("You are lost.")

