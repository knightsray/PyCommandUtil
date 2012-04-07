#!/usr/bin/python

import os, sys, time

# Simple daemon.

if __name__ == '__main__':

    STDIN = 0
    STDOUT = 1
    STDERR = 2
    pid_file_path = './daemon.pid'

    # Create a child process.
    pid = os.fork()

    if pid > 0:
        sys.exit(0)
        
    # Create a new session.
    os.setsid()

    # Create a grand child process.
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

    # Redirect stdin, stdout, stderr to null device.
    dev_null = os.open(os.devnull, os.O_RDWR)
    if dev_null == -1:
        sys.exit(1)

    os.dup2(dev_null, STDIN)
    os.dup2(dev_null, STDOUT)
    os.dup2(dev_null, STDERR)

    time.sleep(60)
