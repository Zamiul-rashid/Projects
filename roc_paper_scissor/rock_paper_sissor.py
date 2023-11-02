def rps():
    import random 
    options = ["rock","paper","scissor"]
    user = None 
    computer = random.choice(options)
    while user not in options:
        user = (input("Please enter between rock,paper,scissor ")).lower()
    print("Computers Choice ",computer)
    print("Players Choice ",user)
    if user == computer :
        return("It's a Tie")
    if user == "rock" and computer == "paper":
        return("Computer Wins")
    if user == "rock" and computer == "scissor":
        return("Player wins ")
    if user == "paper" and computer == "rock":
        return("Player wins ")
    if user == "paper" and computer == "scissor":
        return("Computer wins")
    if user == "scissor" and computer == "paper":
        return("Player wins")
    if user == "scissor" and computer == "rock":
        return("Computer wins")
def playgame():
    while True:
        user = input("If you want to play Rock Paper Scissors, type Y. To quit, type N: ").upper()
        if user == "Y":
            print(rps())
            break
        elif user == "N":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please type Y or N.")
def playgame2():
    while True:
        print("Restarting the code again ")
        print(rps())
        break
playgame()
play_again = True
while play_again:
    user_input = input("Do you want to play again? (Y/N): ").upper()
    if user_input == "Y":
        playgame2()
        play_again=True
    if user_input == "N":
        print("Thanks for playing. Please come back again.")
        break

    