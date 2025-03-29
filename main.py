import random

def choose_word():
    word = ["university", "player", "hangman", "congratulation", "pakistan"]
    return random.choice(word)

def display_words(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + ""
        else:
            result += "_"
    return result.strip()

def Hangman():
    word = choose_word()
    guessed_letter = set()
    max_attempt = 7
    incorrect_guessed = 0

    print("Let's Start the game")

    while incorrect_guessed < max_attempt:
        print("\n" + display_words(word, guessed_letter ))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a valid number! ")

        if guess in guessed_letter:
            print("You already guessed the letter.")

        guessed_letter.add(guess)

        if guess not in word:
            incorrect_guessed += 1
            print(f"Incorrect guess. You have {max_attempt - incorrect_guessed} attempts remaining")

        if set(word).issubset(guessed_letter):
            print("Congratulation! You have guessed the word", word)

    print("The Game has ended.")

if __name__ == "__main__":
    Hangman()











