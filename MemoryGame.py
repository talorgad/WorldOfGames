import time
import Live
import Utils
from DataManager import read_data, write_data

random_list = []  # Global variables
guss_list = []
is_win = False

def generate_sequence():
    global random_list
    import random
    # Get difficulty level from data.csv
    data = read_data("data.csv")
    difficulty = data.iloc[-1]["difficulty_level"]  # Get difficulty from the latest row

    random_list = []
    for i in range(int(difficulty)):
        n = random.randint(1, 101)
        random_list.append(n)
    print(random_list)
    time.sleep(int(difficulty))
    Utils.clear_console()
    return random_list

def get_list_from_user():
    global guss_list

    # Get difficulty level from data.csv
    difficulty = read_data("data.csv").iloc[-1]["difficulty_level"]

    input_list = input(f"Please guess {difficulty} numbers separated by space \n")
    guss_list = input_list.split()
    for i in range(len(guss_list)):
        guss_list[i] = int(guss_list[i])



def is_list_equal():
    global is_win  # Use the global is_win variable
    if random_list == guss_list:
        print("correct!! you are the winner!!!!")
        is_win = True
    else:
        print("wrong answer... you lost")
        is_win = False

def save_score():
    global is_win
    if is_win:
        score = (int(read_data("data.csv").iloc[-1]["difficulty_level"] * 3) + 5)
        print(f"Your score is: {score}")

        # Update data.csv with score
        data = read_data("data.csv")
        data.loc[len(data) - 1, "score"] = score  # Add score to the latest row
        print(data)
        write_data("data.csv", data)
        # Update data.csv with score (pass actual score value)
        Live.update_data('name', 'game_name', 'game_number', 'difficulty_level', 'score')


        return int(score)

def play_mg():
    global is_win
    is_win = False
    random_list = generate_sequence()
    get_list_from_user()
    is_list_equal()

    if is_win:
        save_score()  # Call save_score if the player wins
        print("Congratulations on winning the game!")
        return True
    else:
        print("Would you like to play again? (Y/N)")
        response = input()

        if response.upper() == "Y":
            return play_mg()
            # return False  # Indicate that the player doesn't want to play again immediately
        else:
            print("Thank you, goodbye")
            return True  # Indicate that the player won't play again


if __name__ == "__main__":
    play_mg() # No need to pass difficulty as it's retrieved from data.csv
