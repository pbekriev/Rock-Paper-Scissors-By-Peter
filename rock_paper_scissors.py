import random

print("======================================================\n"
      "                        RULES\n"
      " * Rock wins against scissors.\n"
      " * Scissors win against paper.\n"
      " * Paper wins against rock.\n"
      "======================================================")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
played_games = 0
player_victories = 0
computer_victories = 0
command = True

number_of_games = input("Choose how many games to play.\n"
                        "If you choose 0 you will play until write \"stop\".\n"
                        "At any time you can type stop and the game will end.\n"
                        "Number of games:")
if number_of_games.isdigit():
    if int(number_of_games) > 0:
        print(f"You chose {number_of_games} games! Good luck!")
    elif int(number_of_games) == 0:
        print("You chose 0 and you will play until you write \"stop\". Good luck!")
    else:
        raise SystemExit("Invalid Input. Try again...")
else:
    raise SystemExit("Invalid Input. Try again...")
while command:

    computer_move = ""
    print("======================================================")
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    elif player_move == "stop":
        break
    else:
        print("Invalid Input. Try again...")
        continue
    computer_random_choice = random.randint(1, 3)

    if computer_random_choice == 1:
        computer_move = rock
    elif computer_random_choice == 2:
        computer_move = paper
    else:
        computer_move = scissors

    played_games += 1

    print(f"Game:{played_games}")
    print(f"You chose {player_move}.")
    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_victories += 1
        print(f"You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        computer_victories += 1
        print("You lost!")

    print(f"Result: You = {player_victories} Computer = {computer_victories}")
    if played_games == int(number_of_games):
        command = False
