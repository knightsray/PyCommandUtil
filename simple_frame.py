#!/usr/bin/python

import subprocess

# Simple command utility class


class Cmd():

    def __init__(self, cmdpath):
        self.cmdpath = cmdpath.split(' ')

    def __del__(self):
        if self.stdin is not None:
            self.stdin.close()
        if self.stdout is not None:
            self.stdout.close()
        if self.stderr is not None:
            self.stderr.close()

    def run(self):
        self.popen = subprocess.Popen(self.cmdpath,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      close_fds=True,
                                      shell=False)
        self.stdin = self.popen.stdin
        self.stdout = self.popen.stdout
        self.stderr = self.popen.stderr
        self.output = ''
        self.error = ''
        self.popen.wait()

    def getOut(self):
        if self.output == '':
            for line in self.stdout:
                self.output = self.output + line
        return self.output

    def getErr(self):
        if self.error == '':
            for line in self.stderr:
                self.error = self.error + line
        return self.error

    def getStatus(self):
        return self.popen.returncode


def ExpectEQ(actual, expected):
    if actual != expected:
        print 'Expected: ' + str(expected)
        print 'Actual: ' + str(actual)


def ExpectNE(actual, expected):
    if actual == expected:
        print 'Expected: ' + str(expected)
        print 'Actual: ' + str(actual)


def ExpectCmdNormal(cmd, expected, status=0):
    ExpectEQ(cmd.getStatus(), status)
    ExpectEQ(cmd.getOut(), expected)
    ExpectEQ(cmd.getErr(), '')


def ExpectCmdAbnormal(cmd, expected, status=1):
    ExpectNE(cmd.getStatus(), 0)
    ExpectEQ(cmd.getStatus(), status)
    ExpectEQ(cmd.getOut(), '')
    ExpectEQ(cmd.getErr(), expected)


def AssertEQ(actual, expected):
    assert actual == expected


def AssertNE(actual, expected):
    assert actual != expected


def AssertCmdNormal(cmd, expected, status=0):
    AssertEQ(cmd.getStatus(), status)
    AssertEQ(cmd.getOut(), expected)
    AssertEQ(cmd.getErr(), '')


def AssertCmdAbnormal(cmd, expected, status=1):
    AssertNE(cmd.getStatus(), 0)
    AssertEQ(cmd.getStatus(), status)
    AssertEQ(cmd.getOut(), '')
    AssertEQ(cmd.getErr(), expected)


def LoopRun(cmdpath, filepath, count):
    cmd = Cmd(cmdpath)

    with open(filepath, 'w') as file:
        for i in xrange(count):
            cmd.run()
            if cmd.getStatus() == 0:
                file.write(cmd.getOut())
            else:
                file.write(cmd.getErr())


if __name__ == '__main__':

    cmd = Cmd('who')
    cmd.run()

    if cmd.getStatus() == 0:
        print cmd.getOut()
    else:
        print cmd.getErr()

    i = 0
    for cmdpath in ['whoami', 'ls -l', 'date']:
        LoopRun(cmdpath, 'file' + str(i) + '.txt', 3)
        i += 1

    AssertEQ(0, 0)
    AssertEQ('hogehoge', 'hogehoge')
    AssertNE(0, 1)
    AssertNE('hogehoge', 'hooge')
#   AssertEQ(0, 1)
    ExpectEQ(0, 0)
    ExpectEQ('hogehoge', 'hogehoge')
    ExpectNE(0, 1)
    ExpectNE('hogehoge', 'hooge')
    ExpectEQ(0, 1)
    ExpectCmdNormal(cmd, 'hoge', 0)
