import random

# Hangman stages (ASCII visuals)
stages = [
    r'''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# Word options for guessing
word_list = ['apple', 'hangman', 'ball', 'krishna', 'banana', 'monkey',
             'ironman', 'batman', 'superman', 'computer', 'laptop',
             'smartphone', 'mobile', 'fridge', 'cooler', 'television',
             'notebook', 'headphones']

guess_word = random.choice(word_list)
word_length = len(guess_word)
display = ["_"] * word_length
lives = len(stages) - 1
game_over = False

print("Welcome to Hangman!")
print("Guess the word by entering one letter at a time.")
print(f"You have {lives} lives. Good luck!")
print(" ".join(display))
print(stages[0])

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed '{guess}'. Try a different letter.")
    elif guess in guess_word:
        for position in range(word_length):
            if guess_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    print(" ".join(display))
    print(stages[len(stages) - lives - 1])

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word!")
        game_over = True
    elif lives == 0:
        print("💀 You ran out of lives. Game Over!")
        print(f"The word was: '{guess_word}'")
        game_over = True
