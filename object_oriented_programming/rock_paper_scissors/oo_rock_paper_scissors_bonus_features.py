# TODO add total wins count?
# TODO get Winner dictionary update to work

import random
from pprint import pp
import os

class Player:
    ROBOTS = ('r2d2', 'hal', 'daneel', 'asimo')
    MOVES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    WINNING_SCORE = 5

    def __init__(self):
        self.move = None

    def wins_game(self):
        return self.score == self.WINNING_SCORE

class Computer(Player):
    # chooses randomly
    def __init__(self):
        super().__init__()
        self.score = 0

    def choose(self):
        self.move = random.choice(Player.MOVES)

class R2D2(Computer):
    # always chooses rock
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = 'rock'

class HAL(Computer):
    # prefers scissors
    HAL_MOVES = Player.MOVES + ['scissors' for _ in range(95)]
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(self.HAL_MOVES)

class Daneel(Computer):
    # first move random, then always chooses what you chose in the previous match
    def __init__(self):
        super().__init__()

    def choose(self):
        # TODO pull game, match methods out into subclass of RPSGame so not referencing
        # instance of RPSGame outside of definitions
        if new_game.match_() == 1:
            self.move = random.choice(Player.MOVES)
        else:
            self.move = new_game.humans_last_move()

class Human(Player):
    def __init__(self):
        self.move = None
        self.opponent = None
        self.score = 0

    def choose(self, choice_type):

        match choice_type:
            case 'robot':
                prompt = "Please select an opponent: R2D2, HAL, Daneel, or Asimo: "
                options = Player.ROBOTS
            case 'move':
                prompt = "Please choose rock, paper, or scissors, lizard, or spock: "
                options = Player.MOVES

        while True:
            choice = input(prompt).lower()

            if choice.lower() in options:
                break

            print(f"Sorry, {choice} is not valid.")

        match choice_type:
            case 'robot':
                self.opponent = choice
            case 'move':
                self.move = choice

    def opponent_name(self):
        return self.opponent.title()

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
        self._computer = None

        self._game = 0
        self._match = 0

        self._history = {}

    def match_(self):
        return self._match

    def _current_game(self):
        return f"Game {self._game}"

    def _current_match(self):
        return f"Match {self._match}"

    def _previous_match(self):
        return f"Match {self._match - 1}"

    def _increment_game(self):
        self._game += 1

    def _increment_match(self):
        self._match += 1

    def _reset(self):
        self._human.score = self._computer.score = self._match = 0

    def _display_welcome_message(self):
        print("%====================================================%")
        print("|  WELCOME TO ROCK, PAPER, SCISSORS, LIZARD, SPOCK!  |")
        print("%====================================================%")

        print('''
                    RULES:
        ROCK crushes SCISSORS, LIZARD
        PAPER covers ROCK, disproves SPOCK
        SCISSORS cut PAPER, LIZARD
        LIZARD chews on PAPER, poisons SPOCK
        SPOCK vaporizes ROCK, smashes SCISSORS
                ''')

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _initialize_opponent(self):
        match self._human.opponent:
            case 'r2d2':
                self._computer = R2D2()
            case 'hal':
                self._computer = HAL()
            case 'daneel':
                self._computer = Daneel()
            case 'asimo':
                self._computer = Computer()

    def _human_wins_match(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move in self.WINNING_COMBINATIONS[human_move]

    def _computer_wins_match(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move in self.WINNING_COMBINATIONS[computer_move]

    def _increment_score(self):
        if self._human_wins_match():
            self._human.score += 1
        elif self._computer_wins_match():
            self._computer.score += 1

    def _display_match_winner(self):
        print(f"You chose: {self._human.move}.")
        print(f"{self._human.opponent_name()} chose: {self._computer.move}.")

        if self._human_wins_match():
            print("You win this match!")
        elif self._computer_wins_match():
            print(f"{self._human.opponent_name()} wins this match!")
        else:
            print("It's a tie!")

    def _display_score(self):
        print(f"\n"
              f"Scores: \n"
              f"    Player: {self._human.score} | {self._human.opponent_name()}: {self._computer.score}\n")

    def _display_game_winner(self):
        if self._human.wins_game():
            print("You won the game!")
        elif self._computer.wins_game():
            print(f"{self._human.opponent_name()} wins the game!")

    def humans_last_move(self):
        return self._history[self._current_game()][self._previous_match()]['You']

    def _display_match_turns(self):
        if self.match_() > 1:
            print(f"{self._current_game()}:")
            for match in self._history[self._current_game()]:
                print(f"    {match}:")
                for player in  self._history[self._current_game()][match]:
                    print(f"        {player} chose {self._history[self._current_game()][match][player]}")

    def _display_history(self):
        print("\n"
              "GAME HISTORY:\n"
              "_____________")

        for game in self._history:
            print(f"{game}:")

            for match in self._history[game]:
                print(f"    {match}:")

                for player in  self._history[game][match]:
                    print(f"        {player} chose {self._history[game][match][player]}")

            # print(f"Winner: {self._history[game]['Winner']}")

    def play(self):
        self._display_welcome_message()

        while True:
            # log new game
            self._increment_game()
            if self._current_game() not in self._history:
                self._history[self._current_game()] = {}

            # choose opponent
            self._human.choose('robot')
            self._initialize_opponent()

            # set scores, match to zero
            self._reset()


            while True:
                # log new match
                self._increment_match()

                # human, computer moves
                self._human.choose('move')
                os.system('clear')
                self._computer.choose()

                # log moves
                self._history[self._current_game()][self._current_match()] = {'You': self._human.move,
                                                                              f'{self._human.opponent_name()}': self._computer.move}

                # match outcome, history of current game
                self._display_match_winner()
                self._increment_score()
                self._display_score()
                self._display_match_turns()

                if self._human.wins_game():
                    # self._history[self._current_game()]['Winner'] = 'You'
                    break
                elif self._computer.wins_game():
                    # self._history[self._current_game()]['Winner'] = self._human.opponent_name()
                    break

            # game outcome
            self._display_game_winner()
            if not self._play_again():
                break

        # display history of all games, goodbye message
        self._display_history()
        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n): ")
        return answer.lower().startswith('y')

new_game = RPSGame()
new_game.play()
