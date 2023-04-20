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



answer = get_question()

# Get to generate the display based on the length of a random word that I found using an API call
display = generate_list_from_string(answer)
print(f"The answer has {len(display)} letters.")
print(display)

game_on = True
errors = 0

max_errors = 5
new_display = []

while game_on: 


    def word_or_letter():
        while True:
            print()
            decision = input("Would you like to guess the whole word or a letter? " 
                "Type W for word or L for letter.\n" 
                "Guessing the whole word will bring you a better score.\n")
            if decision !='W' or decision != "L":
                print()
                print("You need to select either W or L.")
                continue
            break
        return decision




    word_or_letter()

         
    guess = make_guess(new_display)
    new_display = put_letter(guess, answer, display)

    if guess not in answer: 
        print("You have made an error.")
        errors += 1
    else:
        print("You got it!")

    print_board(new_display)

    if errors == max_errors:
        print("Game over! You reached the maximum number of errors!")
        game_on = False

    if " " not in new_display:
        print("You won! Great game!")
        game_on = False




