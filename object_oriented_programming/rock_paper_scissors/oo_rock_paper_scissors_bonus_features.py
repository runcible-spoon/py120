import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    WINNING_SCORE = 5

    def __init__(self):
        self.move = None
        # needs a self.score?

    def wins_game(self):
        return self.score == self.WINNING_SCORE

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        self.move = None
        self.score = 0

    def choose(self):
        prompt = "Please choose rock, paper, or scissors: "

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f"Sorry, {choice} is not valid.")

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _reset_scores(self):
        self._human.score = self._computer.score = 0

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors. Goodbye!")

    def _human_wins_round(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins_round(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                 (computer_move == 'paper' and human_move == 'rock') or
                 (computer_move == 'scissors' and human_move == 'paper'))

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

    def play(self):
        self._display_welcome_message()

        while True:
            self._reset_scores()
            while True:
                self._human.choose()
                self._computer.choose()
                self._display_round_winner()
                self._increment_score()
                self._display_score()
                if self._human.wins_game() or self._computer.wins_game():
                    break

            self._display_game_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n): ")
        return answer.lower().startswith('y')

RPSGame().play()
