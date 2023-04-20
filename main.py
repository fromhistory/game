from funct import *

# A Hangman game
# Make this game for two players, so it connects to the database and pulls the score for the player (history). 
# Database should have the name of the player etc
# STORE DATA IN THE FILE, SO IT COULD BE GOOD FOR THE NEXT USE
# WHEEL OF FORTUNE: SENDS AN API CALL
# KEEP THE LEADERSBOARD
# LOOK UP DATA USING AN API CALL
# guess a word when you can only be wrong seven times. If you are not wrong you can keep playing
# I can have different levels based on the number of errors that I have


word = "freedom"

# Get to generate the display based on the length of a random word that I found using an API call
display = [" ",  " ", " ", " ", " ", " ", " "]

game_on = True
errors = 0

max_errors = 5
new_display = []

while game_on: 

    # Would you like to guess the whole word or a letter? 
         
    guess = make_guess(new_display)
    # Create logic for the case when you are making a mistake 
    new_display = put_letter(guess, word, display)

    if guess not in word: 
        print("You have made an error.")
        errors += 1

    print_board(new_display)

    if errors == max_errors:
        print("Game over! You reached the maximum number of errors!")
        game_on = False

    if " " not in new_display:
        print("You won! Great game!")
        game_on = False




