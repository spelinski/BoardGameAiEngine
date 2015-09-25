'''
Created on Sep 23, 2015

@author: rohk
'''
import unittest
from communcation.PlayerCommunication import PlayerCommunication
from communcation.PlayerCommunication import BotCommunicationError


class TestPlayerCommunication(unittest.TestCase):

    def test_should_always_send_without_timout_valid_program(self):
        localPlayerCommunication = PlayerCommunication(
            "test/mockBot/mockBot.py")
        localPlayerCommunication.send_message("testing")
        localPlayerCommunication.close()

    def test_should_always_send_without_timout_invalid_program(self):
        localPlayerCommunication = PlayerCommunication("")
        localPlayerCommunication.send_message("testing")
        localPlayerCommunication.close()

    def test_should_respond_to_say_something(self):
        localPlayerCommunication = PlayerCommunication(
            "test/mockBot/mockBot.py")
        localPlayerCommunication.send_message("testing")
        responseFromBot = localPlayerCommunication.get_response()
        self.assertEqual(responseFromBot, "1..2..3\n")
        localPlayerCommunication.close()

    def test_should_raise_bot_communication_error_if_bot_can_not_respond(self):
        localPlayerCommunication = PlayerCommunication("")
        localPlayerCommunication.send_message("testing")
        self.assertRaisesRegexp(
            BotCommunicationError, "Failed to send message because of program didn't say anything", localPlayerCommunication.get_response)
        localPlayerCommunication.close()

    def test_should_raise_bot_communication_error_if_bot_times_out(self):
        localPlayerCommunication = PlayerCommunication(
            "test/mockBot/mockBot.py")
        localPlayerCommunication.send_message("fail")
        self.assertRaisesRegexp(
            BotCommunicationError, "Failed to send message because of timeout", localPlayerCommunication.get_response, 1)
        localPlayerCommunication.close()
