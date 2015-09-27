class BattlelinePlayer(object):
    """
    Player object for Battleline
    Keeps track of a hand
    """

    HAND_LIMIT = 7


    def __init__(self, name, communication):
        """Constructor
        @param name the player name
        @param communication the communication the player has with a bot
        """
        self.name = name
        self.hand = []
        self.communication = communication

    def add_to_hand(self, card):
        """
        Add to the hand, as long as the hand is not already at the limit
        @param card the card we want to add to the hand
        @raise HandFullError if we are already have a full hand
        """
        if(self.__is_hand_at_limit()):
            raise HandFullError(BattlelinePlayer.HAND_LIMIT)
        self.hand.append(card)

    def __is_hand_at_limit(self):
        return len(self.hand) == BattlelinePlayer.HAND_LIMIT

    def send_message(self, message):
        """
        Use the underlying communication object to talk convey commands
        @param the message we want to send using communication object
        """
        return self.communication.send_message(message)
    
    def get_response(self):
        """
        Use the underlying communication object to get messages back
        @return response being sent back
        """
        return self.communication.get_response()

    def remove_from_hand(self, card):
        """
        Remove a card from the hand
        @param the card to remove
        @raises InvalidMoveError if the player didn't have the card
        """
        if card not in self.hand:
            raise InvalidMoveError("Player did not have card in hand")
        self.hand.remove(card)

class HandFullError(Exception):
    def __init__(self, hand_limit):
        """
        Construtor
        @param hand_limit the limit that the player hand can be
        """
        self.hand_limit = hand_limit

    def __str__(self):
        """
        Return a string representation of the exception
        """
        return "Cannot exceed hand limit of {}".format(self.hand_limit)

class InvalidMoveError(Exception):
    def __init__(self, reason):
        """
        Constructor
        @param reason the reason why this is an invalid mov
        """
        self.reason = reason

    def __str__(self):
        """
        Return a string representation of the exception
        """
        return "Invalid Move - {}".format(self.reason)
