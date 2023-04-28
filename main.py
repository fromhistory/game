from funct import *
import sqlite3
from art import *


# I can have different levels based on the number of errors that I have
 
print(lst_fonts[0])

user_identity = greeting()
first_name = name()


#if it is a returning user update his score 
# if it is a new user create a new row

answer = get_question()

# Get to generate the display based on the length of a random word that I found using an API call
display = generate_list_from_string(answer)
print(f"The answer has {len(display)} letters.")
print(display)


errors = 0
max_errors = 5
new_display = []
number_of_tries = 0
score = 0
super_score = 0

while True: 

    if errors == max_errors:
        print("Game over! You reached the maximum number of errors!")
        print(lst_fonts[2])
        break
        

    if " " not in new_display and len(new_display) > 0:
        print(f"You won! Great game, {name}")
        print(lst_fonts[1])
        break

    decision = word_or_letter()

    if decision == "W":

        answer_try = input("Please type the word: ").lower()
        number_of_tries += 1
        if answer_try == answer:
            print(f"Congratulations! You won the game, {name}!")
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
            print("You got it!")

        print_board(new_display)



final_score =total_score(score=score, super_score=super_score, number_of_tries=number_of_tries)
print(f"Your score in this game is: {final_score}")


# Connect to the SQLite database
conn = sqlite3.connect('game.db')
cursor = conn.cursor()

update_database(cursor, user_identity, first_name, final_score)

# Commit the changes and close the connection
conn.commit()

leader = current_leader()

if leader == 'y':
    highest_score_leader(cursor)
    
else:
    print("Okay then. We recorded you current result. Thanks for playing!")


conn.close()


