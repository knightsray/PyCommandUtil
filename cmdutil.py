#!/usr/bin/python

import subprocess


# Simple execute command utility class
class CmdUtil():

    def __init__(self, cmdpath):
        self.cmdpath = cmdpath.split(' ')

    def __del__(self):
        if self.stdin != None:
            self.stdin.close()
        if self.stdout != None:
            self.stdout.close()
        if self.stderr != None:
            self.stderr.close()

    def run(self):
        self.popen = subprocess.Popen(self.cmdpath,          \
                                      stdin=subprocess.PIPE, \
                                      stdout=subprocess.PIPE,\
                                      stderr=subprocess.PIPE,\
                                      close_fds=True,        \
                                      shell=False)
        self.stdin = self.popen.stdin
        self.stdout = self.popen.stdout
        self.stderr = self.popen.stderr
        self.output = ""
        self.error = ""

    def poll(self):
        self.popen.poll()

    def wait(self):
        self.popen.wait()

    def setIn(stdin):
        self.stdin = stdin

    def getOut(self):
        if self.output == "":
            for line in self.stdout:
                self.output = self.output + line
        return self.output

    def getErr(self):
        if self.error == "":
            for line in self.stderr:
                self.error = self.error + line
        return self.error

    def getStatus(self):
        return self.popen.returncode

    def getPid(self):
        return self.popen.pid


if __name__ == "__main__":

    ls = CmdUtil('ls')
    ls.run()
    ls.wait()
    if ls.getStatus() == 0:
        print ls.getOut(),
    else:
        print ls.getErr(),
