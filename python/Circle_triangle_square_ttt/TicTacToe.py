import random # Dodany import dla losowego AI

def pobierz_liczbe(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Nieprawidłowa liczba. Spróbuj ponownie.")

class TicTacToe:
    def __init__(self):
        self.user_sign = 'O'
        self.cpu_sign = 'X'
        self.the_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self):
        print(self.the_board[0] + '|' + self.the_board[1] + '|' + self.the_board[2])
        print('-+-+-')
        print(self.the_board[3] + '|' + self.the_board[4] + '|' + self.the_board[5])
        print('-+-+-')
        print(self.the_board[6] + '|' + self.the_board[7] + '|' + self.the_board[8])
        print()

    def _ai_move(self):
        # Mądrzejsze AI losujące wolne pole
        available_moves = [i for i, spot in enumerate(self.the_board) if spot == ' ']
        if available_moves:
            random_move = random.choice(available_moves)
            self.the_board[random_move] = self.cpu_sign

    def _user_move(self, field_number):
        self.the_board[field_number] = self.user_sign

    def who_win(self):
        result = []

        result.append(self.the_board[0] + self.the_board[1] + self.the_board[2])
        result.append(self.the_board[3] + self.the_board[4] + self.the_board[5])
        result.append(self.the_board[6] + self.the_board[7] + self.the_board[8])
        result.append(self.the_board[0] + self.the_board[3] + self.the_board[6])
        result.append(self.the_board[1] + self.the_board[4] + self.the_board[7])
        result.append(self.the_board[2] + self.the_board[5] + self.the_board[8])
        result.append(self.the_board[0] + self.the_board[4] + self.the_board[8])
        result.append(self.the_board[2] + self.the_board[4] + self.the_board[6])
        if 'XXX' in result:
            return self.cpu_sign
        if 'OOO' in result:
            return self.user_sign
            
        # Opcjonalne sprawdzenie remisu
        if ' ' not in self.the_board:
            return 'Remis'

        return None

    def move(self, field_number):
        if field_number >= len(self.the_board) or field_number < 0:
            return False

        if self.the_board[field_number] == self.cpu_sign:
            return False
        if self.the_board[field_number] == self.user_sign:
            return False

        if self.who_win() is not None:
            return False

        self._user_move(field_number)

        if self.who_win() is not None:
            return True # Wygrałeś, ruch prawidłowy!

        self._ai_move()
        return True

    def reset_game(self):
        self.__init__()


# Zwróć uwagę na wcięcia! Wszystko poniżej jest wciśnięte w prawo.
if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()

    while True:
        # Pytamy gracza o pole i przeliczamy
        wybor = int(pobierz_liczbe("Wybierz pole (1-9): "))
        true_index = wybor - 1

        # Od razu próbujemy wykonać ruch wewnątrz 'if'
        if game.move(true_index) == True:
            game.print_board()
            
            # Sprawdzamy wygraną TYLKO, gdy ruch był udany
            zwyciezca = game.who_win()
            if zwyciezca is not None:
                if zwyciezca == 'Remis':
                    print("Koniec gry! Mamy remis.")
                else:
                    print(f"Koniec gry! Wygrywa: {zwyciezca}")
                break
                
        else:
            print("Nie można wykonać tego ruchu. Spróbuj ponownie.")