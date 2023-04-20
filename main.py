# A Hangman game


# Make this game for two players, so it connects to the database and pulls the score for the player (history)


# STORE DATA IN THE FILE, SO IT COULD BE GOOD FOR THE NEXT USE
# WHEEL OF FORTUNE: SENDS AN API CALL
# KEEP THE LEADERSBOARD
# LOOK UP DATA USING AN API CALL

# guess a word when you can only be wrong seven times. If you are not wrong you can keep playing

word = "freedom"

# function to check if the guessed letter is in the word

def correct_letter(guess, word):
    return guess in word


# Function asking for a guess
def make_guess():
    while True:
        guess = input("Please guess a letter: \n")
        if not guess.isalpha():
            continue
        break
    return guess

# Get to generate the display based on the length of a random word that I found using an API call
display = [" ",  " ", " ", " ", " ", " ", " "]

# Function to put the letter in a word: "freedom"
def put_letter(letter, word, display):
    for index, elem in enumerate(word):
        if elem == letter:
            display[index] = letter
    return display


# The GAME logic

game_on = True

while game_on: 

    guess = make_guess()

    new_display = put_letter(guess, word, display)

    print(new_display)

    if " " not in new_display:
        game_on = False

