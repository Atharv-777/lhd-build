import random
import sys

#Function for checking player's move and computer's move and updating score
def checkClash(player, computer, point, flag):
    if(player == 4):   
        sys.exit("You exited from game.")
    else:
        if((computer == "rock" and player == 2) or (computer == "paper" and player == 3) or (computer == "scissor" and player == 1)):
            point += 1
            flag = True
        if((computer == "rock" and player == 3) or (computer == "paper" and player == 1) or (computer == "scissor" and player == 2)):
            flag = False
        return flag, point


#Instructions of games
print("This is Rock, Paper & Scissor game")
print("\nInstructions")
print("A. Player have to enter one of the following commands : ")
print("----1 for rock")
print("----2 for paper")
print("----3 for scissor")
print("----4 for exit")
print("C. Move will be shown in (player's move : computer) format.")
print("D. Please only enter these commands ----> 1,2, 3 or 4.")

steps = ['rock', 'paper', 'scissor']
point = 0
flag = True

while(flag != False):
    player = int(input('\nEnter your command : '))
    computer = random.choice(steps)
    flag, point = checkClash(player, computer, point, flag)
    print(steps[player-1], " : ", computer)
    print("Your points are : ", point)