#!/usr/bin/python

import threading, os

class Timer:
    def __init__(self, interval, function, argument = []):
        self.interval = interval
        self.handler = function
        self.argument = argument
        self.keep_timer = True
        self.status = 0

    def run(self):
        self.status = 1
        timer_thread = threading.Timer(self.interval, self.handler,
                                       self.argument)
        timer_thread.start()
        timer_thread.join()
        self.status = 0

    def periodic_run(self):
        self.keep_timer = True
        self.status = 1

        while self.keep_timer:
            timer_thread = threading.Timer(self.interval, self.handler,
                                           self.argument)
            timer_thread.start()
            timer_thread.join()
        self.status = 0

    def reset_interval(self, interval):
        if self.status == 0:
            self.interval = interval
            return 0
        else:
            return -1

    def reset_handler(self, function, argument):
        if self.status == 0:
            self.handler = function
            self.argument = argument
            return 0
        else:
            return -1

    def stop_timer(self):
         if self.status == 1:
             self.keep_timer = False
             return 0
         else:
             return -1

def func1(arg1, arg2):
    print arg1, arg2

if __name__ == '__main__':
    list = ['arg1', 'arg2']
    timer = Timer(1, func1, list)
    timer.periodic_run()
