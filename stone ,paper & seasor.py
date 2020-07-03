# stone, paper and SCISSOR
import math
import random

print("STONE , PAPER & SCISSOR GAME")
a  = ["STONE","PAPER","SCISSOR"]
 
for i in range(3):
    print(f"TYPE {i} "+ a[i])
e = 0
usr_p = int(0)
com_p = int(0)
while e < 10 :
    print(f"you can play for {10-e} times")


    usr = int(input("ENTER YOUR CHOICE:\n"))
    com = random.choice(a)
    print(com)

    if usr == 0:
        if com == "STONE":
            print("Tie !")
        elif com == "PAPER":
            print("YOU LOSE")
            com_p = com_p +1
        else:
            print("YOU WIN .")
            usr_p = usr_p +1
    elif usr == 1 :
        if com == "STONE":
            print("YOU WIN.")       
            usr_p = usr_p +1 
        elif com == "PAPER":
            print("Tie !")
        else:
            print("YOU LOSE !!")
            com_p = com_p +1
    elif usr == 2:
        if com == "STONE":
            print("YOU LOSE !!")
            com_p = com_p +1
        elif com == "PAPER":
            print("YOU WIN !")
            usr_p = usr_p +1
        else:
            print("TIE !")
    else:
        print("~~~~~~~invalid Error !~~~~~~~~")
        e = e-1
    
    if usr_p > com_p:
        print(f"YOU WIN !! Your score is {usr_p}")
    else:
        print(f"you lose !! your score is {usr_p} and com score is {com_p}")


    
    e = e + 1


