import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.wipe()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def wipe(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    MATCH_GOAL = 3
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.current_player = None

    def play(self):
        self.display_welcome_message()
        self.play_match()
        self.display_goodbye_message()

    def play_match(self):
        print(f"The first player to win {TTTGame.MATCH_GOAL} "
               "games wins the match.")

        while True:
            self.play_one_game()
            self.update_match_score()
            self.display_match_score()

            if self.match_over():
                break
            if not self.play_again():
                break

        self.display_match_results()

    def match_over(self):
        return (self.is_match_winner(self.human) or
                self.is_match_winner(self.computer))

    def is_match_winner(self, player):
        return player.score >= TTTGame.MATCH_GOAL

    def update_match_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def display_match_score(self):
        human = self.human.score
        computer = self.computer.score
        print("Current match score: "
              f"[you: {human}] [computer: {computer}]")

    def display_match_results(self):
        if self.human.score > self.computer.score:
            print("You won this match! Congratulations!")
        elif self.human.score < self.computer.score:
            print("Oh, boo hoo. You lost the match!")

    def choose_first_player(self):
        self.current_player = random.choice([self.human, self.computer])

    def play_one_game(self):
        self.board.wipe()
        self.board.display()
        self.choose_first_player()

        while True:
            self.player_moves(self.current_player)
            self.swap_player()
            if self.is_game_over():
                break

            self.board.display_with_clear()

        self.board.display_with_clear()
        self.display_game_results()

    def swap_player(self):
        if self.current_player == self.human:
            self.current_player = self.computer
        else:
            self.current_player = self.human

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_game_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    @staticmethod
    def _join_or(sequence, delimiter=', ', conjunction='or'):
        match len(sequence):
            case 0:
                return ''
            case 1:
                return str(sequence[0])
            case 2:
                return f"{sequence[0]} {conjunction} {sequence[1]}"

        leading_items = delimiter.join(str(item) for item in sequence[0:-1])
        return f'{leading_items}{delimiter}{conjunction} {sequence[-1]}'

    def player_moves(self, player):
        match player:
            case self.computer:
                self.computer_moves()
            case self.human:
                self.human_moves()

    def human_moves(self):
        choice = None
        valid_choices = self.board.unused_squares()
        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = self._join_or(choices_list)
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()
        if not choice:
            choice = self.defensive_computer_move()
        if not choice:
            choice = self.pick_center_square()
        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)


    def find_critical_square(self, player):
        for row in self.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key

        return None

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key

        return None

    def defensive_computer_move(self):
        return self.find_critical_square(self.human)

    def offensive_computer_move(self):
        return self.find_critical_square(self.computer)

    def pick_center_square(self):
        return 5 if self.board.is_unused_square(5) else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def play_again(self):
        while True:
            choice = input("Play again? 'y' or 'n': ").lower().strip()
            if choice in ('y', 'n'):
                break

            print("Sorry, that's not a valid choice.")
            print()

        return choice == 'y'

game = TTTGame()
game.play()
