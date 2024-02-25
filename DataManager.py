import pandas as pd

def read_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["name", "game_name", "game_number", "difficulty_level", "score"])


def write_data(filename, data):
    data.to_csv(filename, index=False)


read_data("data.csv")