#!/usr/bin/python
'''
Created on Sep 23, 2015

@author: rohk
'''

from sys import stdin, stdout


class Bot:

    def run(self):
        while not stdin.closed:
            try:
                line = stdin.readline().strip()

                if len(line) == 0:
                    continue

                if line == "testing":
                    try:
                        stdout.write("1..2..3\n")
                        stdout.flush()
                    except:
                        pass

            except EOFError:
                return

    @staticmethod
    def sendMoves(moves):
        stdout.write(','.join(moves) + '\n')
        stdout.flush()


if __name__ == '__main__':
    Bot().run()