def correct_letter(guess, word):
    return guess in word


# Function asking for a guess
def make_guess(dashboard):
    while True:
        guess = input("Please guess a letter: \n")
        if not guess.isalpha():
            print("This is not a valid letter.")
            continue
        if guess in dashboard:
            print("This letter has already been guessed")
            continue
        break
    return guess


# Function to put the letter in a word: "freedom"
def put_letter(letter, word, display):
    for index, elem in enumerate(word):
        if elem == letter:
            display[index] = letter
    return display


def print_board(board):
    print("\n")
    print(board)
    print("\n")
