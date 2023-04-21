from funct import *
import sqlite3

# A Hangman game
# Make this game for two players, so it connects to the database and pulls the score for the player (history). 
# Database should have the name of the player etc
# STORE DATA IN THE FILE, SO IT COULD BE GOOD FOR THE NEXT USE

# KEEP THE LEADERSBOARD

# guess a word when you can only be wrong seven times. If you are not wrong you can keep playing
# I can have different levels based on the number of errors that I have

def greeting():
    name = input("Hello. Welcome to the game! What is your name?\n")
    return name


name = greeting()

answer = get_question()

# Get to generate the display based on the length of a random word that I found using an API call
display = generate_list_from_string(answer)
print(f"The answer has {len(display)} letters.")
print(display)

game_on = True
errors = 0

max_errors = 5
new_display = []
number_of_tries = -1
score = 0
super_score = 0

while game_on: 

    decision = word_or_letter()

    if decision == "W":

        answer_try = input("Please type the word: ").lower()
        number_of_tries += 1
        if answer_try == answer:
            print(f"Congratulations! You won the game, {name}!")
            super_score = 100
            game_on = False
        continue
        
    else:
        guess = make_guess(new_display)
        new_display = put_letter(guess, answer, display)

        if guess not in answer: 
            print("You have made an error.")
            errors += 1
        else:
            score += 1
            print("You got it!")

        print_board(new_display)

        if errors == max_errors:
            print("Game over! You reached the maximum number of errors!")
            game_on = False

        if " " not in new_display:
            print(f"You won! Great game, {name}")
            game_on = False


final_score =total_score(score=score, super_score=super_score, number_of_tries=number_of_tries)
print(final_score)


# Connect to the SQLite database
conn = sqlite3.connect('game.db')
cursor = conn.cursor()


# Execute the INSERT INTO statement
cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, final_score))

# Commit the changes and close the connection
conn.commit()
conn.close()


