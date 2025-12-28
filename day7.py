import random
from hang_man_word_list import word_list
from hang_man_art import stages
from hang_man_art import logo

print(logo)

lives = 6
chosen_word = random.choice(word_list)

placeholder = ''
for i in chosen_word:
    placeholder += '_'
print('WORD TO GUESS: ',placeholder)

game_over = False
correct_answer = []

while not game_over:
    print(f'---------------{lives}|6|LIVES LEFT---------------')
    guess = input('guess a word :').lower()

    if guess in correct_answer:
        print(f"Guessed letter {guess}")

    display = ''
    for letter  in chosen_word:
        if letter == guess:
            display += letter
            correct_answer.append(guess)
        elif letter in correct_answer:
            display += letter
        else:
            display += '_'
    print('word to guess:-'+display)

    if guess not in correct_answer:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.you lose a life!")

        if lives == 0:
            game_over = True
            print(f"---------------{chosen_word} YOU LOSE!!---------------")

    if '_' not in display:
        game_over = True
        print("---------------YOU WIN!---------------")


    print(stages[lives])