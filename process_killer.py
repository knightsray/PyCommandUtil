#!/usr/bin/python

import os
import signal
import sys


# Send spefied signal to process ID.
def signal_sender(pid, signum):
    os.kill(int(pid), signum)


def process_finisher(pid_file, signum=signal.SIGTERM):
    with open(pid_file, 'r') as pids:
        for pid in pids:
            signal_sender(pid, signum)


def process_terminator(pid):
    signal_sender(pid, signal.SIGTERM)


def process_aborter(pid):
    signal_sender(pid, signal.SIGABRT)


def process_killer(pid):
    signal_sender(pid, signal.SIGKILL)


if __name__ == '__main__':
    process_killer(sys.argv[1])
