import random

print("welcome to my Game!")
print("Game name is Rock, Paper ,Scissor")
user_points=0
computer_points=0

options=["rock","paper","scissor"]
answer=input("Do u want to play?: ").lower()

while(1):
    if (answer == "yes"):
        User_select = input("enter u r choice Rock or Paper or Scissors or Q to quit: ").lower()
        if (User_select=="q"):
            break
        elif(User_select=="rock" or "paper" or "scissor"):
            print("You are choice is ", User_select)
        else:
            print("please enter correct choice the correct one")
            continue
        computer_select = random.randint(0, 2)
        if (User_select == "rock" and options[computer_select] == "paper"):
            print("COMPUTER WON!")
            computer_points += 1
        elif (User_select == "rock" and options[computer_select] == "scissor"):
            print("YOU WON!")
            user_points += 1
        elif (User_select == "ROCK" and options[computer_select] == "rock"):
            print("DRAW")
        elif (User_select == "paper" and options[computer_select] == "scissor"):
            print("COMPUTER WON")
            computer_points += 1
        elif (User_select == "paper" and options[computer_select] == "rock"):
            print("YOU WON")
            user_points += 1
        elif (User_select == "paper" and options[computer_select] == "paper"):
            print("DRAW")
        elif (User_select == "scissor" and options[computer_select] == "rock"):
            print("COMPUTER WON")
            computer_points += 1
        elif (User_select == "scissor" and options[computer_select] == "paper"):
            print("YOU WON")
            user_points += 1
        else:
            print("DRAW")

    else:
        break
if (user_points > computer_points):
    print("YOU WON")
else:
     print("COMPUTER WON")




