import random
import Live
from DataManager import read_data


def generate_number():
    global secret_number
    data = read_data("data.csv")
    difficulty = data.iloc[-1]["difficulty_level"]
    secret_number = int(random.uniform(0, int(difficulty)))
    print(secret_number)
    return secret_number


def get_guss_from_user():
    while True:
        data = read_data("data.csv")
        difficulty = data.iloc[-1]["difficulty_level"]
        user_guss = int(input(f"please make a guess between 0 to {difficulty}: "))
        if not 0 <= user_guss <= int(difficulty):
            print(f"number is not in the range, please select a number between 0 - {difficulty} ")
        else:
            return user_guss


def compare_results(secret_number,user_guss):
    data = read_data("data.csv")
    difficulty = data.iloc[-1]["difficulty_level"]
    if secret_number == user_guss:
        return "TRUE"
    else:
        return "FALSE"


def play_gg():
    data = read_data("data.csv")
    difficulty = data.iloc[-1]["difficulty_level"]
    secret_number_difficulty = generate_number()
    user_guss = get_guss_from_user()
    result = compare_results(secret_number_difficulty, user_guss)
    print(result)
    exit()


if __name__ == "__main__":
    play_gg()  # Pass the chosen difficulty to the play_gg function

# Call play_gg with the chosen difficulty
# user_difficulty = difficulty
# result = play_gg(user_difficulty)

# The program will exit after printing the result

