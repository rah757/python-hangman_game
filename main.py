import hangman_art
import random
import hangman_words
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
logo = hangman_art.logo
end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f'you already guessed {guess}, guess another word')
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter #update display array with guessed letter

    #if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, it is not in the word. Try another one. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #check if all letters guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
