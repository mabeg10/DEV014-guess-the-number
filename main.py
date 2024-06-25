import random

def player_guess_player(secret_number, input_func=input, output_func=print):
    attempts = 0 # Inicializa el contador de intentos a 0
    # Bucle infinito hasta que el jugador adivine el número correcto
    while True:
        try:
            guess = int(input_func("Introduce tu adivinanza: "))
            attempts += 1
            if guess < secret_number:
                output_func("Demasiado bajo. Intenta de nuevo.")
            elif guess > secret_number:
                output_func("Demasiado alto. Intenta de nuevo.")
            else:
                output_func(f"¡Felicidades! Has adivinado el número en {attempts} intentos.")
                return attempts  # Termina el bucle y la función, regresando el número de intentos
        except ValueError:
            output_func("Por favor, introduce un número válido.")

def main():
    # Genera un número secreto aleatorio entre 1 y 100
    secret_number = random.randint(1, 100)
    print("Estoy pensando en un número entre 1 y 100.")
    
    # Inicia el juego
    player_guess_player(secret_number)

if __name__ == "__main__":
    main()
