import random

user=input("Let's play a game of rock, paper, scissors! Please enter your choice: ")
userActions=["rock","paper","scissors"]
computerActions=random.choice(userActions)
print(f"\nYou chose {user},the computer chose {computerActions}.\n")

if user == computerActions:
      print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
      if computerActions == "scissors":
        print("Rock smashes scissors! Congrats, you win! :)")
      else:
        print("Paper covers rock! Sorry, you lose :(")
elif user == "paper":
      if computerActions == "rock":
        print("Paper covers rock! Congrats, you win! :)")
      else:
        print("Scissors cuts paper! Sorry, you lose :(")
elif user == "scissors":
      if computerActions == "paper":
          print("Scissors cuts paper! Congrats, you win! :)")
      else:
          print("Rock smashes scissors! Sorry, you lose :(")