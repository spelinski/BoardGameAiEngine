
#Dummy card class until one is actually created.

class Flag(object):
    """A representation of a flag in Battle Line.
    A flag can hold 3 cards for both players.
    """
    PLAYER_ONE_ID = "player1"
    PLAYER_TWO_ID = "player2"
    MAX_CARDS_PER_SIDE = 3

    def __init__(self):
        """
        Constructor
        """
        self.sides = {self.PLAYER_ONE_ID:[], self.PLAYER_TWO_ID:[]}

    def is_empty(self):
        """
        Determines if there are any cards played on this flag.
        """
        return self.is_player_side_empty(self.PLAYER_ONE_ID) and self.is_player_side_empty(self.PLAYER_TWO_ID)

    def is_player_side_empty(self, player):
        """ Determines if a player side is empty.

        @param player The player side to check.
        """
        if not self.__is_valid_player_choice(player): 
            raise InvalidPlayerError(player)
        else:
            return len(self.sides[player]) == 0

    def add_card(self, player, card):
        """Add a card to the Flag

        @param player player side to add the flag to. 
        @param card   the card to add to the player side
        """
        if not self.__is_valid_player_choice(player):
            raise InvalidPlayerError(player)
        if len(self.sides[player]) >= self.MAX_CARDS_PER_SIDE:
            raise TooManyCardsOnOneSideError(player) 
        self.sides[player].append(card)

    def __is_valid_player_choice(self, player):
        return player in self.sides

class InvalidPlayerError(Exception):
     def __init__(self, player_string):
         """Create an Exception that the player is not valid
         @param player_string the player name that was not valid
         """
         self.player = player_string 
 
     def __str__(self):
         return "Player String {} is invalid".format(self.player)

class TooManyCardsOnOneSideError(Exception):
     def __init__(self, player_string):
         """Create an Exception that the player is trying to add to many cards
         @param player_string the player name that was adding too many cards 
         """
         self.player = player_string 
 
     def __str__(self):
         return "Player {} is attempting to add to many cards".format(self.player)

