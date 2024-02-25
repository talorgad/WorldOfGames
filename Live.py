import pandas as pd
import MemoryGame
from DataManager import read_data, write_data
import importlib

def welcome():
    name = input("Hello! What is your name? ")
    print(f"Welcome to the games, {name}!")
    return name

def choose_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        try:
            chosen_game = int(input("Enter your choice: "))
            if 1 <= chosen_game <= 3:
                return int(chosen_game)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_difficulty():
    print("Please choose game difficulty from 1 to 5:")

    while True:
        try:
            difficulty_level = int(input("Enter your choice: "))
            if 1 <= difficulty_level <= 5:
                return int(difficulty_level)
            else:
                print("Invalid choice. Please try a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def update_data(name, game_name, game_number, difficulty_level, score):
    data = {
        "name": [name],
        "game_name": [game_name],
        "game_number": [game_number],
        "difficulty_level": [difficulty_level],
        "score": [score]
    }
    # Read existing data (create empty DataFrame if file doesn't exist)
    existing_data = read_data("data.csv")
    # Append new data to existing DataFrame
    new_data = pd.DataFrame(data)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    # Write updated data to CSV
    write_data("data.csv", combined_data)

def run_game(chosen_game, chosen_difficulty):
    game_modules = {
        1: "MemoryGame",
        2: "GuessGame",
        3: "CurrencyRoulette"
    }
    game_module = game_modules[chosen_game]

    try:
        game_file = importlib.import_module(game_module)
        if hasattr(game_file, "play_mg" if chosen_game == 1 else "play_gg" if chosen_game == 2 else "play_cr"):
            # Game file has the appropriate play function
            game_file.play_mg() if chosen_game == 1 else game_file.play_gg() if chosen_game == 2 else game_file.play_cr()
        else:
            print(f"Game module '{game_module}' does not have a 'play_{game_file.lower()}' function!")
    except ImportError:
        print(f"Error importing game module '{game_module}'!")

def main():
    name = welcome()
    chosen_game = choose_game()
    game_name = {1: "MemoryGame", 2: "GuessGame", 3: "CurrencyRoulette"}[chosen_game]
    game_number = chosen_game
    difficulty_level = choose_difficulty()
    score = MemoryGame.save_score()

    update_data(name, game_name, game_number, difficulty_level, score)

    run_game(chosen_game, difficulty_level)

if __name__ == "__main__":
    main()
