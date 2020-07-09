from random import randint
import pprint
"""
https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON
Result for quiz: 22/25. I did not know what a Tuple was.
list1 = [1,2,3] -> mutable (changeable, no fixed length)
list1[0] = 5
tuple1 = (1,2,3) -> immutable, fixed length

REVERSE STRINGS - Few different ways to go about it in Python
https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""

#create a list of play options
#[scissors, paper, rock]
hand_list = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

#Work on this with free time
hand_list_backwards = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

title = ["""

______           _       ______                       _____      _                        
| ___ \         | |      | ___ \                     /  ___|    (_)                       
| |_/ /___   ___| | __   | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ___ 
|    // _ \ / __| |/ /   |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__/ __|
| |\ \ (_) | (__|   < _  | | | (_| | |_) |  __/ |_   /\__/ / (__| \__ \__ \ (_) | |  \__ \
\_| \_\___/ \___|_|\_( ) \_|  \__,_| .__/ \___|_( )  \____/ \___|_|___/___/\___/|_|  |___/
                     |/            | |          |/                                        
                                   |_|                                                    

"""
]
#assign a random play to the computer




print("Welcome to Rock Paper Scissors!")
name = input("What is your name? ")
player_score = 0
bot_score = 0

game_over = False

options = ["rock", "paper", "scissors"]
def choice(options):
  for i in options:
    print(i  + ",", end=" ")

bot = options[randint(0, 2)]

def player_lose(name, bot):
  print("You Lose!")
  print(f"{name} chose " + player_move + " Bot chose " + bot)
  bot = options[randint(0, 2)]
  print(f"Your score: {player_score}")
  print(f"Opponent score: {bot_score}")

def player_win(score, bot):
  print(string_to_ascii[player_move])
  score += 1
  print( f"{name} wins!")
  print("Player chose " + player_move + " Bot chose " + bot)
  bot = options[randint(0, 2)]
"""
def replay(b_score,score, ascii, player_move):
  print(string_to_ascii[player_move])
  b_score += 1
  player_lose(name, bot)
  replay = input("Would you like to play again? (y/n) ")
  if replay == "y":
    b_score = 0
    score = 0
    return True
  else:
    b_score = 0
    score = 0
    return False
replay(bot_score, player_score, string_to_ascii, player_move)
"""

string_to_ascii = {
"rock" : hand_list[0],
"paper" : hand_list[1],
"scissors" : hand_list[2]
}
#print(string_to_ascii["rock"])
#create a while loop that keeps game going
#store user hand choice in a new variable
# if user choice is equal to bot choice, print out "TIE!"
#elif user choice is Rock...
  #if bot is paper...
  #else...
#elif user choice is Paper...
  #if bot choice is scissors...
  #else...
#elif user choice is Scissors...
  #if bot choice is rock...
  #else...
#Also, create a variable that users can input to break out of loop and quit the game
#HINT: Make sure that bot does not continue having the same/original choice the entire game while in the while loop. Think about what you need to do here. 


while game_over == False:
  player_move = input("What is your move? ")
  #player_move = hand_list[int(player_move)]
  print("")
  choice(options)
  #call RPS function to do the same thing
  if player_move == bot:
    print("Tie! Player chose " + player_move + " Bot chose " + bot)
    print(string_to_ascii[player_move])
    bot = options[randint(0, 2)]
  else: 
    if player_move == "rock":
      if bot == "paper":
        print(string_to_ascii[player_move])
        bot_score += 1
        player_lose(name, bot)
        replay = input("Would you like to play again? (y/n) ")
        if replay == "y":
          bot_score = 0
          player_score = 0
        else:
          game_over = True
          bot_score = 0
          player_score = 0
      else:
        player_win(player_score, bot)
    if player_move == "paper":
      if bot == "scissors":
        print(string_to_ascii[player_move])
        bot_score += 1
        player_lose(name, bot)
        replay = input("Would you like to play again? (y/n) ")
        if replay == "y":
          bot_score = 0
          player_score = 0
        else:
          game_over = True
          bot_score = 0
          player_score = 0
      else:
        player_win(player_score, bot)
    if player_move == "scissors":
      if bot == "rock":
        print(string_to_ascii[player_move])
        bot_score += 1
        player_lose(name, bot)
        replay = input("Would you like to play again? (y/n) ")
        if replay == "y":
          bot_score = 0
          player_score = 0
        else:
          game_over = True
          bot_score = 0
          player_score = 0
      else:
        player_win(player_score, bot)

      

