#!/usr/bin/python

import datetime
import subprocess
import shlex
import os


class Clocker():
    def __init__(self, date=None):
        if date == None:
            self.date = datetime.datetime.now()
        else:
            self.date = date

    def __del__(self):
        self.reset()

    def reset(self):
        cmd = 'date -s "' + str(self.date) + '"'
        subprocess.check_call(shlex.split(cmd))


def setSysClock(days=0):
    # Check root:
    if os.getuid() != 0:
        return False

    if days == 0:
        cmd = 'date -s "' + str(datetime.datetime.now()) + '"'
        subprocess.check_call(shlex.split(cmd))
    else:
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        date = datetime.datetime(date.year, date.month, date.day, 9, 0, 0)
        cmd = 'date -s "' + str(date) + '"'
        subprocess.check_call(shlex.split(cmd))
        
    return True

if __name__ == '__main__':
    print datetime.datetime.now()
    a = Clocker()
    print datetime.datetime.now()
    setSysClock()
    print datetime.datetime.now()
    setSysClock(1)
    print datetime.datetime.now()
    setSysClock(10)
    print datetime.datetime.now()
    setSysClock(90)
    print datetime.datetime.now()
