import random
import os

class Player:
    ROBOTS = {
        'r': 'r2d2',
        'h': 'hal',
        'd': 'daneel',
        'a': 'asimo'
    }

    MOVES = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'l': 'lizard',
        'sp': 'spock'
    }

    WINNING_SCORE = 5

    def __init__(self):
        self.move = None
        self.score = 0

    def wins_game(self):
        return self.score == self.WINNING_SCORE

class Computer(Player):
    # chooses randomly
    def choose_move(self):
        self.move = random.choice(list(Player.MOVES.values()))

class R2D2(Computer):
    # always chooses rock
    def choose_move(self):
        self.move = 'rock'

class HAL(Computer):
    # prefers scissors
    HAL_MOVES = list(Player.MOVES.values()) + ['scissors' for _ in range(95)]

    def choose_move(self):
        self.move = random.choice(self.HAL_MOVES)

class Daneel(Computer):
    # first move random, then always chooses
    # what you chose in the previous match
    def choose_move(self):
        if self.match_() == 1:
            self.move = random.choice(Player.MOVES.values())
        else:
            self.move = Human.last_move()

class Human(Player):
    def __init__(self):
        super().__init__()
        self.opponent = None

    def _choose(self, prompt, options):
        while True:
            choice = input(prompt).lower()

            if choice.lower() in options:
                return choice

            print(f"Sorry, {choice} is not valid.")

    def choose_move(self):
        while True:
            prompt = "Please choose (r)ock, (p)aper, \
(s)cissors, (l)izard, (sp)ock, or (h)istory for game history: "

            options = list(Player.MOVES.keys()) + ['h']

            choice = self._choose(prompt, options)

            if choice.startswith('h'):
                RPSGame.display_history(self)
                continue

            self.move = Player.MOVES[choice]
            break


    def choose_opponent(self):
        prompt = "Please select an opponent: \
R2D2, HAL, Daneel, or Asimo: "
        options = Player.ROBOTS.keys()
        choice = self._choose(prompt, options)
        self.opponent = Player.ROBOTS[choice]

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

    @property
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
                self._computer = Daneel(self)
            case 'asimo':
                self._computer = Computer()
        print(f"{self._human.opponent_name()} is your opponent.")

    def _play_match(self):
        while True:
            # log new match
            self._increment_match()

            # human, computer moves
            self._human.choose_move()
            os.system('clear')
            self._computer.choose_move()

            # log moves
            game = self._current_game()
            match_ = self._current_match()
            self._history[game][match_] = {'You': self._human.move,
            f'{self._human.opponent_name()}': self._computer.move}

            # match outcome, history of current game
            self._display_match_winner()
            self._increment_score()
            self._display_score()
            self._display_match_turns()

            if self._human.wins_game()or self._computer.wins_game():
                break

    def _first_player_beats_second_player(self, player1_move, player2_move):
        return player1_move in self.WINNING_COMBINATIONS[player2_move]

    def _increment_score(self):
        if self._first_player_beats_second_player(self._human.move, self._computer.move):
            self._human.score += 1
        if self._first_player_beats_second_player(self._computer.move, self._human.move):
            self._computer.score += 1

    def _display_match_winner(self):
        print(f"You chose: {self._human.move}.")
        print(f"{self._human.opponent_name()} chose: {self._computer.move}.")

        if self._first_player_beats_second_player(self._human.move, self._computer.move):
            print("You win this match!")
        elif self._first_player_beats_second_player(self._computer.move, self._human.move):
            print(f"{self._human.opponent_name()} wins this match!")
        else:
            print("It's a tie!")

    def _display_score(self):
        print("\n"
"Scores: \n"
f"    Player: {self._human.score} | \
{self._human.opponent_name()}: \
{self._computer.score}\n")

    def _display_game_winner(self):
        if self._human.wins_game():
            print("You won the game!")
        elif self._computer.wins_game():
            print(f"{self._human.opponent_name()} wins the game!")

    def _display_match_turns(self):
        game = self._current_game()
        if self.match_ > 1:
            print(f"{game}:")
            for match in self._history[game]:
                print(f"    {match}:")
                for player in self._history[game][match]:
                    print(f"        {player} chose \
{self._history[game][match][player]}")

    def last_move(self):
        game = self._current_game()
        prev_match = self._previous_match()

        return self._history[game][prev_match]['You']

    def display_history(self):
        print("\n"
              "GAME HISTORY:\n"
              "_____________")

        for game, match in self._history.items():
            print(f"{game}:")

            for match in self._history[game]:
                print(f"    {match}:")

                for player in  self._history[game][match]:
                    print(f"        {player} chose \
{self._history[game][match][player]}")

    def play(self):
        self._display_welcome_message()

        while True:
            # log new game
            self._increment_game()
            if self._current_game() not in self._history:
                self._history[self._current_game()] = {}

            # choose opponent
            self._human.choose_opponent()
            self._initialize_opponent()

            # set scores, match to zero
            self._reset()

            self._play_match()

            # game outcome
            self._display_game_winner()
            if not self._play_again():
                break

        # display history of all games, goodbye message
        self.display_history()
        self._display_goodbye_message()

    def _play_again(self):
        while True:
            options = ('y', 'n')
            answer = input("Would you like to play again? (y/n): ")
            if answer.lower() in options:
                break

            print("Sorry, not a valid choice.")

        return answer.lower().startswith('y')

RPSGame().play()
