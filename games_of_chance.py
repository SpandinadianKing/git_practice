#run in games1 env
#random package installed there

#imports random module
import random

#sets default starting value
money = 100

#sets random int variable
num = random.randint(1,10)

#default return variable
#game_over = print("Thanks for playing!")

#function to have player choose a game
#def choose_game(

#money = 100
#Flipping a coin, call heads/tails
print("You currently have $" + str(money))
guess = input("Please choose Heads or Tails! ").lower()
bet = int(input("Please place a bet! "))

def coin_flip(guess, bet):
  num = random.randint(1,10)
  money = 100
  if guess == "heads" and num % 2 == 0:
    winnings = bet * 2
    money += winnings
    print("     ")
    print("It landed on Heads! You win $" + str(winnings) + "!!")
    print("You now have $" + str(money) + "!!")
  elif guess == "heads" and num % 2 != 0:
    winnings = bet * 3
    money -= winnings
    print("     ")
    print("Sorry! It landed on Tails! You lost $" + str(winnings) + "!!")
    print("You now have $" + str(money) + ".")
  elif guess == "tails" and num % 2 != 0:
    winnings = bet * 2
    money += winnings
    print("     ")
    print("It landed on Tails! You win $" + str(winnings) + "!!")
    print("You now have $" + str(money) + "!!")
  elif guess == "tails" and num % 2 == 0:
    winnings = bet * 3
    money -= winnings
    print("     ")
    print("Sorry! It landed on Heads! You lost $" + str(winnings) + "!!")
    print("You now have $" + str(money) + ".")
  return print("Thanks for playing!!")
 
coin_flip(guess, bet)
        