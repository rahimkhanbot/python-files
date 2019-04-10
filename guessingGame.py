
"""
secret = 'baby'
guess = ''
guess_count = 0
guess_limit = 3
guess_limit_indicator = 3
no_guesses = False

while guess != secret and not(no_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the secret word: ")
        guess_count += 1
        guess_limit_indicator -=1

        print("you have " +str(guess_limit_indicator) +"left")
    else:
        no_guesses = True

if no_guesses:
    print('you are out of guesses')
else:
    print("You win")
"""

secret_word = "baby"
guess = ""
guess_count = 0
guess_limit = 3
chance_left = 3
out_of_guesses = False


def chance_print():
    if chance_left == 1:
        print('')
        print("Not at all, Its your last chance")
        print("Hint: Became mom and dad")

    elif chance_left == 2:
        print('')
        print(f"No, you have only {chance_left} left")
        print("Hint: innocent and new")

    else:
        print(f"you have only {chance_left} left")
        print("Hint: little and cute")


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        chance_print()
        guess = input("Enter the secret word: ")
        guess_count +=1
        chance_left -=1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("you are out of guesses")

else:
    print("you win")

