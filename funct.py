import requests
from urllib.parse import unquote
from html import unescape

def get_question():
    while True:
        response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple&encode=url3986")
        response.raise_for_status()
        data = response.json()

        answer = unquote(data['results'][0]['correct_answer'].lower())
        question = unquote(data['results'][0]['question'])
        if ' ' not in answer and answer.isalpha:
            print(question)
            print(answer)
            return answer


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
