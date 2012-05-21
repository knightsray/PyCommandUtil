#!/usr/bin/python 

import subprocess

# Simple execute command utility class
class CmdUtil():
    def __init__(self, cmdpath):
	self.cmdpath = cmdpath
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
                                      close_fds=True, shell=True)
        self.stdin = self.popen.stdin
        self.stdout = self.popen.stdout
        self.stderr = self.popen.stderr
    def poll(self):
        self.popen.poll()
    def wait(self):
        self.popen.wait()

    def printOut(self):
        for line in self.stdout:
            print "%s" % line, 
    def printErr(self):
        for line in self.stderr:
            print "%s" % line,

    def printStatus(self):
        print self.popen.returncode
    def printPid(self):
        print self.popen.pid
    def isKilled(self):
        if self.popen.returncode < 0:
           return True
        else:
           return False

if __name__ == "__main__":

    ls = CmdUtil('ls')
    ls.run()
    ls.wait()
    ls.printOut()
    ls.printStatus()
