import random
from colorama import Fore, Back, Style

print(Fore.BLUE + "======================================================\n"
      "                        RULES\n"
      " * Rock wins against scissors.\n"
      " * Scissors win against paper.\n"
      " * Paper wins against rock.\n"
      "Choose how many games to play.\n"
      "If you choose 0 you will play until write \"stop\".\n"
      "At any time you can type stop and the game will end.\n"
      "======================================================")

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

while True:  # Main Program

    played_games = 0
    player_victories = 0
    computer_victories = 0

    while True:  # Check correct input

        number_of_games = input(Fore.RESET + "Number of games: ")

        if number_of_games.isdigit():
            break
        print(Fore.RED + "Invalid input. Try again...")

    if int(number_of_games) > 0:
        print(f"You chose {number_of_games} games! Good luck!")
    elif int(number_of_games) == 0:
        print("You chose 0 and you will play until you write \"stop\".\n"
              "Good luck!")
    else:
        print(Fore.RED + "Invalid input. Try again...")
        continue

    while True:  # The Game

        computer_move = ""
        print(Fore.BLUE + "======================================================")
        player_move = input(Fore.CYAN + "Choose [r]ock, [p]aper or [s]cissors: ")

        if player_move == "r":
            player_move = rock
        elif player_move == "p":
            player_move = paper
        elif player_move == "s":
            player_move = scissors
        elif player_move == "stop":
            break
        else:
            print(Fore.RED + "Invalid Input. Try again...")
            continue

        computer_random_choice = random.randint(1, 3)

        if computer_random_choice == 1:
            computer_move = rock
        elif computer_random_choice == 2:
            computer_move = paper
        else:
            computer_move = scissors

        played_games += 1

        print(Fore.RESET + f"Game:{played_games}")
        print(f"You chose {player_move}.")
        print(f"The computer chose {computer_move}.")

        # The logic

        if (player_move == rock and computer_move == scissors) or \
                (player_move == paper and computer_move == rock) or \
                (player_move == scissors and computer_move == paper):
            player_victories += 1
            print(Fore.GREEN + "You win!")
        elif player_move == computer_move:
            print(Fore.YELLOW + "Draw!")
        else:
            computer_victories += 1
            print(Fore.RED + "You lost!")

        print(Fore.RESET + f"Result: You = {player_victories} Computer = {computer_victories}")

        if played_games == int(number_of_games):
            break

    if player_victories > computer_victories:
        print(Fore.GREEN + "==================YOU WIN THE GAME!===================")
    elif player_victories < computer_victories:
        print(Fore.RED + "==================YOU LOST THE GAME!==================")
    else:
        print(Fore.YELLOW + "======================DRAW GAME!======================")

    while True:  # Check for restart
        new_game_ask = input(Fore.CYAN + "Do you want new game? (y/n): ")
        if new_game_ask in ("y", "n"):
            break
        print(Fore.RED + "Invalid input. Try again...")

    if new_game_ask == "y":
        continue
    else:
        print(Fore.BLUE + "====================== GOODBYE =======================")
        break
