import random

def generate_secret_number(min_value=1, max_value=100):
    """Genera un número secreto entre min_value y max_value"""
    return random.randint(min_value, max_value)

def get_user_guess(input_func=input):
    """Obtiene la adivinanza del usuario"""
    while True:
        try:
            guess = int(input_func("Introduce tu adivinanza: "))
            return guess
        except ValueError:
            print("Por favor, introduce un número válido.")

def evaluate_guess(secret_number, guess):
    """Evalúa la adivinanza comparándola con el número secreto"""
    if guess < secret_number:
        return "Demasiado bajo. Intenta de nuevo."
    elif guess > secret_number:
        return "Demasiado alto. Intenta de nuevo."
    else:
        return "correcto"

def player_guess(secret_number, input_func=input, output_func=print):
    """Realiza la adivinanza del jugador"""
    guess = get_user_guess(input_func)
    result = evaluate_guess(secret_number, guess)
    output_func(f"Tu adivinanza es {result}.")
    return guess, result

def computer_guess(secret_number, min_value=1, max_value=100, output_func=print):
    """Realiza la adivinanza de la computadora"""
    guess = random.randint(min_value, max_value)
    output_func(f"El ordenador adivina: {guess}")
    result = evaluate_guess(secret_number, guess)
    output_func(f"La adivinanza del ordenador es {result}.")
    return guess, result

def play_turns(secret_number, input_func=input, output_func=print):
    """Alterna los turnos entre la jugadora y la computadora hasta que alguien gane"""
    attempts = 0
    player_guesses = []
    computer_guesses = []
    min_value, max_value = 1, 100
    round_num = 1

    while True:
        output_func(f"\n--- Round {round_num} ---")

        # Turno de la jugadora
        output_func("Turno de la jugadora:")
        guess, result = player_guess(secret_number, input_func, output_func)
        player_guesses.append(guess)
        attempts += 1
        if result == "correcto":
            output_func(f"¡La jugadora ha adivinado el número en {attempts} intentos!")
            output_func(f"Las adivinanzas de la jugadora fueron: {player_guesses}")
            return
        
        # Turno del ordenador
        output_func("Turno del ordenador:")
        guess, result = computer_guess(secret_number, min_value, max_value, output_func)
        computer_guesses.append(guess)
        attempts += 1
        if result == "correcto":
            output_func(f"¡El ordenador ha adivinado el número en {attempts} intentos!")
            output_func(f"Las adivinanzas del ordenador fueron: {computer_guesses}")
            return
        elif result == "Demasiado bajo. Intenta de nuevo.":
            min_value = guess + 1
        elif result == "Demasiado alto. Intenta de nuevo.":
            max_value = guess - 1
        
        round_num += 1

def play_game(input_func=input, output_func=print):
    """Inicia y gestiona el juego"""
    secret_number = generate_secret_number()
    output_func("Estoy pensando en un número entre 1 y 100.")
    play_turns(secret_number, input_func, output_func)
    return input_func("¿Quieres jugar de nuevo? (sí/no): ").strip().lower() == "sí"

def main():
    """Función principal del juego"""
    while True:
        if not play_game():
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
