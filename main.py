from funct import *
import sqlite3
from art import *

# Connect to the SQLite database
conn = sqlite3.connect('game.db')
cursor = conn.cursor()

# Define variables
errors = 0
max_errors = 5
new_display = []
number_of_tries = 0
score = 0
super_score = 0
silent_count = 0


# Display the greeting 
print(lst_fonts[0])

# Display the rules of the game
box(text)

# Ask if it is a new or returning user
user_identity = greeting()

# Verify the claim that it is a returning user. If not a returning user, get the name.
if user_identity == 'y':
    first_name = get_valid_name(cursor)
elif user_identity == 'n':
    first_name = get_name()


# Get a random question from the online trivia database 
answer = get_question()

# Generate a display based on the length of an answer 
display = generate_list_from_string(answer)
print(f"The answer has {len(display)} letters.")
print(display)

# Game cycle

while True: 

    if errors == max_errors:
        print("Game over! You reached the maximum number of errors!")
        #print Acsii art saying game over
        print(lst_fonts[2])
        break

    if " " not in new_display and len(new_display) > 0:
        print(f"You won! Great game, {first_name}")
        #print Ascii art congratulating the winner
        print(lst_fonts[1])
        break

    # Ask user if they want to guess a word or a letter

    decision = word_or_letter()

    if decision == "W":

        answer_try = input("Please type the word: ").lower()
        number_of_tries += 1
        if answer_try == answer:
            print(f"Congratulations! You won the game, {first_name}!")
            print(lst_fonts[1])
            if number_of_tries == 1:
                super_score = 110
            else:
                super_score = 100
            break
        print()
        print("That's incorrect. We will remove ten points from your final score. You have also lost one try.")
        errors += 1
        continue
        
    else:
        guess = make_guess(new_display)
        new_display = put_letter(guess, answer, display)

        if guess not in answer: 
            print("Sorry, this letter is not in the word.")
            errors += 1
        else:
            score += 1
            silent_count += 1
            print("You got it!")

        print_board(new_display)

# Calculate the final score

final_score =total_score(score=score, super_score=super_score, number_of_tries=number_of_tries, silent_count=silent_count)
print(f"Your score in this game is: {final_score}")


# Update the database. If it is a new user, create a new row with data.
# If it is a returning user, update the score
update_database(cursor, user_identity, first_name, final_score)

# Commit the changes and close the connection
conn.commit()


# Find who has the highest the score in the database
leader = current_leader()

if leader == 'y':
    highest_score_leader(cursor)
else:
    print("Okay then. We recorded you current result. Thanks for playing!")

conn.close()


