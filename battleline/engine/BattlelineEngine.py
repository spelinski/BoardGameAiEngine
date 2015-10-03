from mechanics.Deck import Deck
from BoardLogic import BoardLogic
from itertools import product
from battleline.Identifiers import TroopCard

class BattlelineEngine(object):
    """
    An engine that coordinates two players, a board and the decks for battleline
    """

    def __init__(self, player1, player2):
        """
        Constructor
        @param player1 the first player
        @param player2 the second player
        """
        self.player1 = player1
        self.player2 = player2
        self.troop_deck = Deck(self.get_troop_cards())
        self.boardLogic = BoardLogic()

        self.__make_player_turn_index = 0

    def initialize(self):
        """
        Initialize the game
        Deal seven cards to each player
        """
        for i in xrange(7):
            self.player1.add_to_hand(self.troop_deck.draw())
            self.player2.add_to_hand(self.troop_deck.draw())

    def get_troop_cards(self):
        """
        Get the troop cards
        @return A list of all troop cards
        """
        colors = ["RED", "GREEN", "ORANGE", "YELLOW", "BLUE", "PURPLE"]
        return [TroopCard(number, color) for color, number in product(colors, range(1, 11))]

    def progress_turn(self):
        """
        Perform one turn
        """
        self.__make_player_turn(self.player1)
        self.__make_player_turn(self.player2)
        self.__make_player_turn_index = self.__make_player_turn_index + 1
        if self.__make_player_turn_index == 9:
            self.__make_player_turn_index = 0

    def __make_player_turn(self, player):
        player.remove_from_hand(player.hand[0])
        self.boardLogic.addCard(self.__make_player_turn_index,player.name,player.hand[0])
        if not self.troop_deck.is_empty():
            player.add_to_hand(self.troop_deck.draw())
