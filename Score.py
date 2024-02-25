from MemoryGame import is_win
# from Live import difficulty_level

def calculate_score(difficulty):
    from Live import difficulty_level
    from MemoryGame import is_win  # Import locally to avoid circular import
    if is_win:
        score = (difficulty_level * 3) + 5
        print(f"Your score is: {score}")
        return score
    return 0

if __name__ == "__main__":
    calculate_score()
