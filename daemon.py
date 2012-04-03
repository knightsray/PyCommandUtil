#!/usr/bin/python

import os, sys

# Simple daemon.

if __name__ == '__main__':

    pid_file_path = './daemon.pid'

    # Create a child process.
    pid = os.fork()

    if pid > 0:
        sys.exit(0)
        
    # Create a new session.
    os.setsid()

    # Create a child process.
    pid = os.fork()

    if pid > 0:
        sys.exit(0)

    # Create pid file.
    pid_file = open(pid_file_path, 'w')
    pid_file.write(str(os.getpid()))
    pid_file.close()

    # Change current direcotry.
    os.chdir('/')
  
    # Set umask.
    os.umask(0)

    # Close stdin, stdout, stderr.
    sys.stdin.close()
    sys.stdin = None
    sys.stdout.close()
    sys.stdout = None
    sys.stderr.close()
    sys.stderr = None
    os.close(0)
    os.close(1)
    os.close(2)

