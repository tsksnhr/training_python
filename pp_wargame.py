import random

class Card:

    suits = [None, "spade", "heart", "diamond", "clover"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, another):
        if self.value < another.value:
            return True
        elif self.value == another.value:
            if self.suit < another.suit:
                return True
            else:
                return False
        else:
            return False

    def __qt__(self, another):
        if self.value > another.value:
            return True
        elif self.value == another.value:
            if self.suit > another.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return "{} of {}".format(self.values[self.value], self.suits[self.suit])

class Deck:
    def __init__(self):
        self.cards = []

        for suit in range(1,5):
            for value in range(2, 15):
                self.cards.append(Card(suit, value))
                #self.cards.append((suit, value))
        
        random.shuffle(self.cards)

    def rim_card(self):
        if self.cards == 0:
            return None
        else:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

class Game:
    def __init__(self):
        self.player_1 = Player(input("Player1?: "))
        self.player_2 = Player(input("Player2?: "))
        self.deck = Deck()

    def wins(self, winner):
        print("{} is winner!".format(winner))

    def draw(self, player_1_name, player_1_card, player_2_name, player_2_card):
        temp = "{} drawed {}, {} drawed {}"
        temp = temp.format(player_1_name, player_1_card, player_2_name, player_2_card)
        print(temp)

    def play_game(self):
        cards = self.deck.cards
        print("Start the war!")

        while len(cards) >= 2:
            temp = "q: quit, or others: start  :"
            response = input(temp)
            
            if response == "q":
                break
            
            player_1_card = self.deck.rim_card()
            player_2_card = self.deck.rim_card()
            player_1_name = self.player_1.name
            player_2_name = self.player_2.name

            self.draw(player_1_name, player_1_card, player_2_name, player_2_card)

            if player_1_card > player_2_card:
                self.wins(player_1_name)
                self.player_1.wins += 1
            else:
                self.wins(player_2_name)
                self.player_2.wins += 1

        win = self.winner(self.player_1, self.player_2)
        print("Finish! {} vs {}, {} win!".format(self.player_1.wins, self.player_2.wins, win))

    def winner(self, player_1, player_2):
        if player_1.wins > player_2.wins:
            return player_1.name
        elif player_1.wins < player_2.wins:
            return player_2.name
        else:
            return "Draw"

game = Game()
game.play_game()
