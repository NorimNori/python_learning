import random

def guessing_game():
    # Generar un número del 1 al 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    player_number = input("Choose your Player Number, theres only 456 spots: ")

    # Introduccion al juego.
    print("\n△ ⬤ ◼ Welcome to the Number Guessing Game! ◼ ⬤ △")
    print(f"Player {player_number}, you must guess a number between 1 and 100.")
    print("The stakes are high. Only one can win.")
    print("△ ⬤ ◼ Let the game begin! ◼ ⬤ △\n")

    while not guessed:
        # Solicitar un número del 1 al 100.
        guess = input(f"Player {player_number}, enter a number between 1 and 100: ")

      # Verificar que la entrada sea un número y no una letra.
        if guess.isdigit():
            guess = int(guess) # Lo estamos pasando de texto a entero.
            attempts += 1

            if guess < secret_number:
                # Cuando se ingresa un numero menor.
                print(f"⬤ The secret number is higher than {guess}. △ Think carefully.")
            elif guess > secret_number:
                # Cuando se ingresa un numero mayor.
                print(f"◼ The secret number is lower than {guess}. ⬤ Don't lose focus.")
            else:
                # Cuando se ingresa el numero correcto.
                print(
                    f"△ ⬤ ◼ Congratulations, Player {player_number}! ◼ ⬤ △\n"
                    f"You've won the game. The secret number was {guess}, and you succeeded in {attempts} attempts."
                )
                guessed = True
        else:
            print(f"◼ Invalid input, Player {player_number}! ⬤ Please enter a valid number. △ Your time is running out.\n")


guessing_game()
