import random
from pprint import pp

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    WINNING_SCORE = 5

    def __init__(self):
        self.move = None

    def wins_game(self):
        return self.score == self.WINNING_SCORE

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"
        self.score = 0

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        self.move = None
        self.name = "You"
        self.score = 0

    def choose(self):
        prompt = "Please choose rock, paper, or scissors, lizard, or spock: "

        while True:
            choice = input(prompt).lower()

            if choice.lower() in Player.CHOICES:
                break

            print(f"Sorry, {choice} is not valid.")

        self.move = choice

class RPSGame:
    WINNING_COMBINATIONS = {
        'rock':     ['scissors',    'lizard'],
        'paper':    ['rock',        'spock'],
        'scissors': ['paper',       'lizard'],
        'lizard':   ['paper',       'spock'],
        'spock':    ['rock',        'scissors']
    }

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._history = []

        self._game = 0
        self._round = 0

    def _current_game(self):
        return f"Game {self._game}"

    def _current_round(self):
        return f"Round {self._round}"

    def _reset(self):
        self._human.score = self._computer.score = 0

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _human_wins_round(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move in self.WINNING_COMBINATIONS[human_move]

    def _computer_wins_round(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move in self.WINNING_COMBINATIONS[computer_move]

    def _increment_score(self):
        if self._human_wins_round():
            self._human.score += 1
        elif self._computer_wins_round():
            self._computer.score += 1

    def _display_round_winner(self):
        print(f"You chose: {self._human.move}.")
        print(f"The computer chose: {self._computer.move}.")

        if self._human_wins_round():
            print("You win this round!")
        elif self._computer_wins_round():
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    def _display_score(self):
        print(f"Scores: \n"
              f"    Player: {self._human.score} | Computer: {self._computer.score}\n")

    def _display_game_winner(self):
        if self._human.wins_game():
            print("You won the game!")
        elif self._computer.wins_game():
            print("Computer wins the game!")

    def _display_history(self):
        print(f"Game history:")
        pp(self._history)

    def play(self):
        self._display_welcome_message()

        while True:
            self._game += 1
            self._history.append(self._current_game())
            self._reset()

            while True:
                self._round += 1
                self._human.choose()
                self._computer.choose()
                self._history.append([self._current_round(), f"You: {self._human.move}", f"Computer: {self._computer.move}"])
                self._display_round_winner()
                self._increment_score()
                self._display_score()
                if self._human.wins_game() or self._computer.wins_game():
                    break

            self._display_game_winner()
            if not self._play_again():
                break
        self._display_history()
        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n): ")
        return answer.lower().startswith('y')

RPSGame().play()
