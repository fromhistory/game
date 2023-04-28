import requests
from urllib.parse import unquote
from html import unescape
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('game.db')
cursor = conn.cursor()


def greeting():
    print("Hello. Welcome to the game! Are you a returning player? ")
    while True:
        user_identity = input("Reply Y for Yes and N for No.\n").lower()
        if user_identity not in ["y", "n"]:
            continue
        break
    return user_identity


def name():
    name = input("Please provide your first name: ").capitalize()
    return name

def check_name_in_db(name):
    pass



def get_question():
    while True:
        response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple&encode=url3986")
        response.raise_for_status()
        data = response.json()

        answer = unquote(data['results'][0]['correct_answer'].lower())
        question = unquote(data['results'][0]['question'])
        if ' ' not in answer and not any(char.isnumeric() for char in answer):
            print(question)
            print(answer)
            return answer

def word_or_letter():
    while True:
        print()
        decision = input("Would you like to guess the whole word or a letter? " 
            "Type W for word or L for letter.\n" 
            "Guessing the whole word will bring you a better score.\n").capitalize()
        
        if decision != "W" and decision != "L":
            print()
            print("You need to select either W or L.")
            continue
        break
    return decision


def generate_list_from_string(string):
    # Create an empty list to store the generated list
    generated_list = []

    # Iterate through each character in the string
    for char in string:
        # Append the character to the list
        generated_list.append(' ')

    # Return the generated list
    return generated_list


# Keep resending the request until the answer is one word

def correct_letter(guess, word):
    return guess in word

# Function asking for a guess
def make_guess(dashboard):
    while True:
        guess = input("Please guess a letter: \n").lower()
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


def total_score(score=0,super_score=0,number_of_tries=0):
    number_of_tries *=10
    score *=5
    return score + (super_score - number_of_tries)



def current_leader():
    while True:
        opinion = input("Would you like to see who is the current leader? For Yes type Y, for No type N. ").lower()
        if opinion not in ['y', 'n']:
            continue 
        break
    return opinion



#### DATABASE QUERIES 

def highest_score_leader(cursor):
    
     # Execute the query to select name with the highest score
    cursor.execute('SELECT name, MAX(score) as max_score FROM scores;')
    result = cursor.fetchone()  # Fetch the first row of the result
    if result:
        name = result[0]  # Get the name from the first column
        max_score = result[1]  # Get the max_score from the second column
        print(f"Name with the highest score: {name}")
        print(f"Highest score: {max_score}")
    else:
        print("No data found")



def update_database(cursor,user_identity, name, final_score):
        # Execute the INSERT INTO statement if it is a returning user 
    if user_identity == 'n':
        cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, final_score))
    elif user_identity == 'y':

        # function that pulls the data from the database and adds the current score to the data and updates the database
        cursor.execute("SELECT score FROM scores WHERE name = ?", (name,))

        row = cursor.fetchone()
        if row is not None:
            old_score = row[0]

        final_score += old_score

        cursor.execute("UPDATE scores SET score = ? WHERE name = ?", (final_score, name))