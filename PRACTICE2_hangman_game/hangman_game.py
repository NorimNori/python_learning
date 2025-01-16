import random

# Seleccion al azar de palabras.
# La expresion "-> str" nos asegura que la funcion devuelva un string.
def get_secret_word() -> str:
    words = ['mexico', 'spain', 'belgium', 'chile', 'japan', 'denmark', 'canada', 'italy', 'germany', 'argentina', 'united states', 'ireland', 'france', 'russia', 'colombia']
    # Escoge una palabra al azar de la lista "words".
    return random.choice(words)

# Funcion para actualizar y mostrar el progreso del juego.
def show_progress(secret_word, guessed_letters):
    progress = ''
    for letter in secret_word:
        if letter in guessed_letters:
            progress += letter
        else:
            progress += '_'
    return progress

# Funcion para ejecutar el juego.
def squid_game_hangman():
    secret_word = get_secret_word()
    guessed_letters = []
    attempts = 7
    game_finished = False

    player_number = input("Choose your Player Number, theres only 456 spots: ")
    
    # Presentacion del juego.
    print("△ ⬤ ◼ Welcome to Squid Game: Hangman Edition! △ ⬤ ◼ \n")
    print("The rules are simple: guess the secret word before your wrong attempts run out.\n")
    print(f"You start with {attempts} attempts. Good luck, player {player_number}!\n")
    print(show_progress(secret_word, guessed_letters))
    
    # Si el juego no ha terminado y aun hay intentos.
    while not game_finished and attempts > 0:
        guess = input("△ Enter a single letter to make your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\n◼ Invalid input! Please enter a single valid letter. Think carefully.")
        elif guess in guessed_letters:
            print("△  You've already guessed or use that letter. Don't lose focus.")
        else:
            guessed_letters.append(guess)

            if guess in secret_word:
                print(f"\n⬤ Correct! The letter '{guess}' is in the word.")
            else:
                attempts -= 1
                print(f"\n⬤ Wrong! The letter '{guess}' is not in the word. Your time is running out.\n")
                print(f"△ Remaining attempts: {attempts}")

        current_progress = show_progress(secret_word, guessed_letters)
        print(f"🔸 Current word progress: {current_progress}")

        if '_' not in current_progress:
            game_finished = True
            print(f"\n⭕ Congratulations, player {player_number}! You survived. The word was: {secret_word.capitalize()}.")
    
    if attempts == 0:
        print(f"\n❌ Game Over, player {player_number}! You've been eliminated.")
        print(f"The correct word was: {secret_word.capitalize()}.")


squid_game_hangman()
