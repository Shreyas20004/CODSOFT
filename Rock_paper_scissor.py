import random

options=("rock","paper","scissor")
player = None
running = True

while running == True :
    Computer = random.choice(options)
    while player not in options :
        player = input("Enter a choice (rock,paper,scissor):")

    print(f"Player:{player}")
    print(f"Computer:{Computer}")
    if player == Computer:
        print("It's a draw!")

    if player == "rock" and Computer =="scissor":
        print("You win!")

    elif player == "rock" and Computer == "paper":
        print("You lose!")

    elif player == "paper" and Computer == "rock":
        print("You win!")
        
    elif player == "paper" and Computer == "scissor":
        print("You lose.")
        
    elif player == "scissor" and Computer == "paper":
        print("You win!")
        
    elif player == "scissor" and Computer == "rock":
        print("You lose.") 
    
    player = None
        
    if not input("Play again?:(y/n):").lower() == "y":
        running = False
    
print("Thanks")
