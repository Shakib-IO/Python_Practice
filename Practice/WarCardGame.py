"""
Class: 
    Suit
        - description
        - symbol

    Card
        - suit
        - show
        - is_special

    Deck
        - cards
        - build, 
        - show, 
        - shuffle, 
        - draw, 
        - add
    Player
        - name, 
        - deck, 
        - is_computer.
        - has_empty_deck, 
        - draw_card, 
        - add_card
"""
import random


class Suit:

    SYMBOLS = {"clubs":"♠", "diamonds":"♦" , "hearts": "♥", "spades":"♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        return self._description
    @property
    def symbol(self):
        return self._symbol


class Card:

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")

    def is_special(self):
        return self._value >= 11


class Deck:

    SUITS = ("clubs", "diamonds", "hearts", "spades")
    def __init__(self, is_empty = False):
        self._cards = []
        if not is_empty:
            self.build()
    
    @property
    def size(self):
        return len(self._cards)
    
    def build(self):
        for suit in Deck.SUITS:
            for value in range (2,15):
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        for card in self._cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None
    
    def add(self, card):
        self._cards.insert(0, card)


class Player:

    def __init__(self, name, deck , is_computer = False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def deck(self):
        return self._deck
    
    def has_empty_deck(self):
        return self._deck.size == 0
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None
    def add_card(self, card):
        self._deck.add(card)


class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):

        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f"Your Card:")
        player_card.show()

        print(f"\nComputer Card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            computer_card = self._computer.draw_card()
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print("Try again. The computer won.")
            return True
        elif self._computer.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"Excellent. You won, {self._player.name}! Congratulations.")
            return True
        else:
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The computer has {self._computer.deck.size} cards on its deck.")
        print("----")

    def print_welcome_message(self):
        print("==============================")
        print("|        War Card Game       |")
        print("==============================")

player = Player("Shakib", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter X to stop.\n")

    if answer.lower() == "x":
        break
