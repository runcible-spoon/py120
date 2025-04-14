import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    time.sleep(2)

class Card:
    ACE_HIGH_VALUE = 11
    ACE_LOW_VALUE = 1
    FACE_VALUE = 10

    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']

    SUITS = ['Clubs', 'Spades' ,'Hearts', 'Diamonds']

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    def __str__(self):
        return f" - {self.rank} of {self.suit}"

    @staticmethod
    def display_hole():
        print(" - ? Hole card ?")

class Deck:
    def __init__(self):
        self.deck = self.new_deck()

    def new_deck(self):
        new_deck = [ Card(rank, suit)
                    for rank in Card.RANKS
                    for suit in Card.SUITS ]
        random.shuffle(new_deck)
        return new_deck

    def deal_starting_hand(self):
        return [self.deal() for _ in range(Participant.STARTING_HAND_AMOUNT)]

    def deal(self):
        try:
            return self.deck.pop()
        except IndexError:
            self.__init__()
            return self.deck.pop()


class Participant:
    STARTING_HAND_AMOUNT = 2

    WINS_GAME = 21
    GAME_POINT = 1
    WINS_MATCH = 3

    def __init__(self):
        self.hand = None

    def chose_to_hit(self):
        while True:
            choice = input("(H)it or (S)tay? ").lower()

            if choice in ("h", "s"):
                break

            print("Sorry, that's not a valid choice.\n")

        return choice == "h"

    @property
    def hand_total(self):
        values = [ card.rank for card in self.hand ]

        sum_value = 0
        for value in values:
            if value == 'Ace':
                sum_value += Card.ACE_HIGH_VALUE
            elif value in ['Jack', 'Queen', 'King']:
                sum_value += Card.FACE_VALUE
            else:
                sum_value += int(value)

        aces = values.count('Ace')
        while sum_value > self.WINS_GAME and aces:
            sum_value -= Card.FACE_VALUE
            aces -= Card.ACE_LOW_VALUE

        return sum_value

    def has_blackjack(self):
        return self.hand_total == self.WINS_GAME and len(self.hand) == self.STARTING_HAND_AMOUNT

    def has_twenty_one(self):
        return self.hand_total == self.WINS_GAME

    def is_busted(self):
        return self.hand_total > self.WINS_GAME

class Player(Participant):
    STARTING_BALANCE = 5
    RICH_BALANCE = 10
    BROKE_BALANCE = 0

    def __init__(self):
        super().__init__()
        self.balance = Player.STARTING_BALANCE

    def increase_balance(self):
        self.balance += 1

    def decrease_balance(self):
        self.balance -= 1

    def display_balance(self):
        print(f"You have ${self.balance}.")

    def is_rich(self):
        return self.balance >= Player.RICH_BALANCE

    def is_broke(self):
        return self.balance <= Player.BROKE_BALANCE

class Dealer(Participant):
    DEALER_CUTOFF = 17


class TwentyOneGame:
    PLAYER_TURN = 'PLAYER_TURN'
    DEALER_TURN = 'DEALER_TURN'

    PLAYER_WINS = 'PLAYER_WINS'
    DEALER_WINS = 'DEALER_WINS'

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

        self.is_player_turn = True

        self.player_wins = None
        self.dealer_wins = None

    def reset(self):
        self.player_wins = self.dealer_wins = None

    def play_twenty_one(self):
        self.display_welcome_message()
        while True:
            self.play_one_round()
            if self.player.is_broke() or self.player.is_rich():
                break
            elif not self.play_again():
                break
            else:
                self.reset()
                clear_screen()

        self.display_game_result()
        self.display_goodbye_message()

    def play_one_round(self):
        self.deal_starting_hands()
        self.show_hands()
        self.player_turn()
        if not self.is_player_turn:
            self.dealer_turn()
        self.calculate_round_result()
        self.adjust_balance()
        self.display_round_result()
        self.is_player_turn = True

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Twenty-One!\n")

    def deal_starting_hands(self):
        self.player.hand = self.deck.deal_starting_hand()
        self.dealer.hand = self.deck.deal_starting_hand()

    def show_hands(self):
        # player's hand
        print("Your hand:")
        for card in self.player.hand:
            print(card)
        print(f"Your total: {self.player.hand_total}\n")

        # dealer's hand
        if self.is_player_turn:
                print("Dealer's hand:")
                print(self.dealer.hand[0])
                Card.display_hole()
                print()
        else:
                print("Dealer's hand:")
                for card in self.dealer.hand:
                    print(card)
                print(f"Dealer's total: {self.dealer.hand_total}\n")

    def player_turn(self):
        if self.player.has_blackjack():
            print("You got a natural 21! Blackjack!")

        while True:
            if self.player.chose_to_hit():
                self.hit(self.player)
                clear_screen()
                self.show_hands()

                if self.player.has_twenty_one():
                    print("Twenty-one!")

                elif self.player.is_busted():
                    print("You busted...")
                    break

            else:
                print("You chose to stay.")
                self.is_player_turn = False
                break

    def hit(self, participant):
        participant.hand.append(self.deck.deal())

    def dealer_turn(self):
        print("Dealer reveals hole card...")
        pause()
        clear_screen()
        self.show_hands()

        while self.dealer.hand_total < Dealer.DEALER_CUTOFF:
            print("Dealer hits.")
            pause()
            self.hit(self.dealer)
            clear_screen()
            self.show_hands()

        if self.dealer.is_busted():
            print("Dealer busted!")
            pause()
        else:
            print("Dealer chooses to stay.")

    def calculate_round_result(self):
        round_outcomes = {

            'DEALER_WINS': {

                # player busted
                self.player.is_busted(),

                # dealer got blackjack, player didn't
                self.dealer.has_blackjack()
                and not self.player.has_blackjack(),

                # dealer's hand larger than player's and dealer didn't bust
                self.dealer.hand_total > self.player.hand_total
                and not self.dealer.is_busted()
                },

            'PLAYER_WINS': {

                # dealer busted
                self.dealer.is_busted(),

                # player got blackjack, dealer didn't
                self.player.has_blackjack()
                and not self.dealer.has_blackjack(),

                # player's hand larger than dealer's and player didn't bust
                self.player.hand_total > self.dealer.hand_total
                and not self.player.is_busted()
                }
        }

        if any(round_outcomes['DEALER_WINS']):
            self.dealer_wins = True

        if any(round_outcomes['PLAYER_WINS']):
            self.player_wins = True

    def display_round_result(self):
        if not self.player_wins and not self.dealer_wins:
            print("This game is a push! No winner.\n"
                f"Your total was {self.player.hand_total}.\n"
                f"Dealer's hand was {self.dealer.hand_total}.\n")

        elif self.dealer_wins:
            print(f"Dealer won this game with {self.dealer.hand_total}.\n"
                  f"You lost with {self.player.hand_total}.\n")

        elif self.player_wins:
            print (f"You won this game with {self.player.hand_total}.\n"
                   f"Dealer lost with {self.dealer.hand_total}.\n")

        self.player.display_balance()

    def play_again(self):
        while True:
            choice = input("Play again? 'y' or 'n': ").lower().strip()
            if choice in ('y', 'n'):
                break

            print("Sorry, that's not a valid choice.")
            print()

        return choice == 'y'

    def adjust_balance(self):
        if self.dealer_wins:
            self.player.decrease_balance()
        if self.player_wins:
            self.player.increase_balance()

    def display_game_result(self):
        if self.player.is_rich():
            print("Wow, ten whole dollars. You're rich!")
        elif self.player.is_broke():
            print("You're flat broke.")
        else:
            print(f"You walked away with ${self.player.balance}.")

    def display_goodbye_message(self):
        print("Thanks for playing! Goodbye.")

game = TwentyOneGame()
game.play_twenty_one()
