import random

print("🎮 Welcome to the Hangman Game")

hangman = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/           '''

print(hangman)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# List of random words
random_words = [
    "apple",
    "chair",
    "river",
    "clock",
    "pencil",
    "ocean",
    "house",
    "train",
    "bread",
    "plant"
]

# Matching hints for each word (same index)
random_hints = [
    "A red or green fruit that keeps doctors away",
    "You sit on it",
    "A natural flowing water body",
    "Tells you the time",
    "Used for writing",
    "Big body of salty water",
    "Place where people live",
    "Runs on tracks and carries people",
    "You toast it for breakfast",
    "Grows in soil and needs water"
]

# ✅ Generate a random index for word & hint
index = random.randint(0, len(random_words) - 1)
generate_word = random_words[index]
generate_hint = random_hints[index]

# Show hint & word length
print(f"Hint: {generate_hint}")
print(f"Length of the word is {len(generate_word)}.")

# Create blank spaces
blank_space = ["_"] * len(generate_word)

# Game variables
guessed_letters = []
max_attempt = 6
wrong_attempt = 0

# Game loop
while wrong_attempt < max_attempt and "_" in blank_space:
    user_input = input("Guess the letter based on blank spaces: ").lower()

    # Already guessed
    if user_input in guessed_letters:
        print("⚠️ You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(user_input)

    # Correct guess
    if user_input in generate_word:
        for i in range(len(generate_word)):
            if generate_word[i] == user_input:
                blank_space[i] = user_input
        print("✅ Correct guess!")
    else:
        wrong_attempt += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempt - wrong_attempt}")
        print(stages[wrong_attempt])

    print("Current word:", " ".join(blank_space))

# Game result
if "_" not in blank_space:
    print("\n🎉 Congratulations! You guessed the word:", generate_word)
else:
    print("\n💀 Game Over! The word was:", generate_word)
