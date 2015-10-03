import unittest
from battleline.engine.CommandParser import ServerCommandParser, ClientCommandParser, InvalidParseError
from battleline.Identifiers import *


def make_dict(msg_type, value):
    return {"type": msg_type, "value": value}


class TestServerParser(unittest.TestCase):

    def test_invalid_message_thrown_if_invalid_message_server(self):
        invalid_messages = ["Invalid Server Message",
                            "player north wrong", "player unknown name", "colors 0 1 2 3 4", "player unknown hand",
                            "player north hand 1,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8",
                            "flag claim-status north north north north north north north north",
                            "flag claim-status north north north north north north north north north north",
                            "flag claim-wrong north north north north north north north north north",
                            "flag claim-status north north north north north north north north wrong"]
        for message in invalid_messages:
            self.assertRaisesRegexp(
                InvalidParseError, "Invalid Parsed Message - {}".format(message), ServerCommandParser().parse, message)

    def test_can_parse_player_name_request(self):
        self.assertEquals(make_dict("player_name_request", Identifiers.NORTH),
                          ServerCommandParser().parse("player north name"))
        self.assertEquals(make_dict("player_name_request", Identifiers.SOUTH),
                          ServerCommandParser().parse("player south name"))

    def test_can_parse_colors(self):
        self.assertEquals(make_dict("colors", ["0", "1", "2", "3", "4", "5"]),
                          ServerCommandParser().parse("colors 0 1 2 3 4 5"))

    def test_can_parse_player_hand_empty(self):
        self.assertEquals(make_dict("player_hand", (Identifiers.NORTH, [])),
                          ServerCommandParser().parse("player north hand"))

    def test_can_parse_player_hand_one_card(self):
        self.assertEquals(make_dict("player_hand", (Identifiers.SOUTH, [TroopCard(color=Identifiers.COLORS[0], number=5)])),
                          ServerCommandParser().parse("player south hand color1,5"))

    def test_can_parse_player_hand_one_card(self):
        self.assertEquals(make_dict("player_hand", (Identifiers.SOUTH, [TroopCard(color=Identifiers.COLORS[0], number=5),
                                                                        TroopCard(color=Identifiers.COLORS[0], number=6),
                                                                        TroopCard(color=Identifiers.COLORS[0], number=7),
                                                                        TroopCard(color=Identifiers.COLORS[1], number=1),
                                                                        TroopCard(color=Identifiers.COLORS[1], number=2),
                                                                        TroopCard(color=Identifiers.COLORS[1], number=3),
                                                                        TroopCard(color=Identifiers.COLORS[1], number=4),])),
                       ServerCommandParser().parse("player south hand color1,5 color1,6 color1,7 color2,1 color2,2 color2,3 color2,4"))

    def test_invalid_parse_error_raised_when_invalid_card(self):
        self.assertRaisesRegexp(
            InvalidParseError, "Invalid Parsed Message - Invalid Card colorx,5", ServerCommandParser().parse, "player north hand colorx,5")
        self.assertRaisesRegexp(
            InvalidParseError, "Invalid Parsed Message - Invalid Card color1,string", ServerCommandParser().parse, "player north hand color1,string")
        self.assertRaisesRegexp(
            InvalidParseError, "Invalid Parsed Message - Invalid Card color1", ServerCommandParser().parse, "player north hand color1")
        self.assertRaisesRegexp(
            InvalidParseError, "Invalid Parsed Message - Invalid Card color1,string,3", ServerCommandParser().parse, "player north hand color1,string,3")

    def test_flag_claim_status(self):
        self.assertEquals(make_dict("flag_claim", ["unclaimed", Identifiers.NORTH, Identifiers.SOUTH,
                                             "unclaimed", Identifiers.NORTH, Identifiers.SOUTH,
                                             "unclaimed", Identifiers.NORTH, Identifiers.SOUTH]),
                                    ServerCommandParser().parse("flag claim-status unclaimed north south unclaimed north south unclaimed north south"))


class TestClientParser(unittest.TestCase):

    def test_invalid_message_thrown_if_invalid_message_server(self):
        self.assertRaisesRegexp(
            InvalidParseError, "Invalid Parsed Message - Invalid Server Message", ServerCommandParser().parse, "Invalid Server Message")

    def test_can_parse_player_name_response(self):
        self.assertEquals({"type": "player_name_response", "value": (
            Identifiers.NORTH, "name")}, ClientCommandParser().parse("player north name"))
        self.assertEquals({"type": "player_name_response", "value": (
            Identifiers.SOUTH, "name2")}, ClientCommandParser().parse("player south name2"))
