import unittest
from unittest.mock import patch
from main import generate_secret_number, get_user_guess, evaluate_guess, player_guess, computer_guess, play_turns

class TestMainCode(unittest.TestCase):

    def test_generate_secret_number(self):
        secret_number = generate_secret_number()
        self.assertTrue(1 <= secret_number <= 100)

    @patch('builtins.input', side_effect=['10'])
    def test_get_user_guess_valid_input(self, mock_input):
        guess = get_user_guess(mock_input)
        self.assertEqual(guess, 10)

    @patch('builtins.input', side_effect=['a', '10'])
    @patch('builtins.print')
    def test_get_user_guess_invalid_input(self, mock_print, mock_input):
        guess = get_user_guess(mock_input)
        self.assertEqual(guess, 10)
        mock_print.assert_called_with("Por favor, introduce un número válido.")

    def test_evaluate_guess_low(self):
        result = evaluate_guess(50, 25)
        self.assertEqual(result, "Demasiado bajo. Intenta de nuevo.")

    def test_evaluate_guess_high(self):
        result = evaluate_guess(50, 75)
        self.assertEqual(result, "Demasiado alto. Intenta de nuevo.")

    def test_evaluate_guess_correct(self):
        result = evaluate_guess(50, 50)
        self.assertEqual(result, "correcto")

    @patch('builtins.input', side_effect=['10'])
    @patch('builtins.print')
    def test_player_guess(self, mock_print, mock_input):
        secret_number = 30
        guess, result = player_guess(secret_number, input_func=mock_input, output_func=mock_print)
        self.assertEqual(guess, 10)
        self.assertEqual(result, "Demasiado bajo. Intenta de nuevo.")
        mock_print.assert_any_call("Tu adivinanza es Demasiado bajo. Intenta de nuevo..")

    @patch('builtins.print')
    def test_computer_guess(self, mock_print):
        secret_number = 30
        guess, result = computer_guess(secret_number, min_value=1, max_value=100, output_func=mock_print)
        self.assertTrue(1 <= guess <= 100)
        self.assertIn(result, ["Demasiado bajo. Intenta de nuevo.", "Demasiado alto. Intenta de nuevo.", "correcto"])
        if result == "Demasiado bajo. Intenta de nuevo.":
            self.assertTrue(guess < secret_number)
        elif result == "Demasiado alto. Intenta de nuevo.":
            self.assertTrue(guess > secret_number)

    @patch('builtins.input', side_effect=['10', '20', '30'])
    @patch('builtins.print')
    def test_play_turns_player_wins(self, mock_print, mock_input):
        secret_number = 30
        with patch('main.computer_guess', return_value=(25, "Demasiado bajo. Intenta de nuevo.")):
            play_turns(secret_number, input_func=mock_input, output_func=mock_print)
        mock_print.assert_any_call("¡La jugadora ha adivinado el número en 3 intentos!")
        mock_print.assert_any_call("Las adivinanzas de la jugadora fueron: [10, 20, 30]")

    @patch('builtins.input', side_effect=['10', '20', '30'])
    @patch('builtins.print')
    def test_play_turns_computer_wins(self, mock_print, mock_input):
        secret_number = 25
        with patch('main.computer_guess', side_effect=[(15, "Demasiado bajo. Intenta de nuevo."), (25, "correcto")]):
            play_turns(secret_number, input_func=mock_input, output_func=mock_print)
        mock_print.assert_any_call("¡El ordenador ha adivinado el número en 4 intentos!")
        mock_print.assert_any_call("Las adivinanzas del ordenador fueron: [15, 25]")

if __name__ == '__main__':
    unittest.main()
