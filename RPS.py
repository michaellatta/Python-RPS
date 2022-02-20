#RPS.py
#Name: Michael Latta
#Date: 2022-02-13
#Assignment: Lab 3
import random

def main():
    wins = 0
    ties = 0
    losses = 0
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    playAgain = "Y"
    while playAgain == "Y":
      #Randomly choose the computer between 'R', 'P', or 'S'
      computer = random.choice(["R", "P", "S"])
      print(computer)

      #Prompt the user for their RPS selection
      player = input("Pick Rock, Paper, or Scissors (R,P,S): ")

      #Determine winner and state what happened to the user
      print("Computer chose " + computer)
      print("Player chose " + player)
      if player == "R" and computer == "R":
          print("Tie")
          ties = ties + 1

      if player == "R" and computer == "S":
        print("Player wins!")
        wins = wins + 1

      if player == "R" and computer == "P":
        print("Computer wins!")
        losses = losses + 1

      if player == "P" and computer == "P":
          print("Tie")
          ties = ties + 1

      if player == "P" and computer == "R":
        print("Player wins!")
        wins = wins + 1

      if player == "P" and computer == "S":
        print("Computer wins!")
        losses = losses + 1

      if player == "S" and computer == "S":
          print("Tie")
          ties = ties + 1

      if player == "S" and computer == "P":
        print("Player wins!")
        wins = wins + 1

      if player == "S" and computer == "R":
        print("Computer wins!")
        losses = losses + 1

      #Ask the user if they would like to play again.
      playAgain = input("Would you like to play again? (Y/N): ")

    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t\t", ties , "\t\t", losses)

main()
