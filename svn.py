#!/usr/bin/python

import cmdutil


class Svn(cmdutil.CmdUtil):

    def __init__(self, uri, directory='.'):
        self.maincmd = 'svn'
        self.revision = 0
        self.uri = uri
        self.directory = directory

    def setUri(uri):
        self.uri = uri

    def setDirectory(directory):
        self.directory = directroy

    def setRevision(revision):
        self.revision = revision

    def co(self):
        self.subcmd = 'co'

        if self.revision == 0:
            self.cmdpath = [self.maincmd,
                            self.subcmd,
                            self.uri,
                            self.directory]
        else:
            self.cmdpath = [self.maincmd,
                            self.subcmd,
                            '-r',
                            str(self.revision),
                            self.uri,
                            self.directory]
        self.run()
        self.wait()

    def export(self):
        self.subcmd = 'export'

        if self.revision == 0:
            self.cmdpath = [self.maincmd,
                            '--force',
                            self.subcmd,
                            self.uri,
                            self.directory]
        else:
            self.cmdpath = [self.maincmd,
                            '--force',
                            self.subcmd,
                            '-r',
                            str(self.revision),
                            self.uri,
                            self.directory]
        self.run()
        self.wait()

    def info(self):
        self.subcmd = 'info'
        self.cmdpath = [self.maincmd, self.subcmd]
        self.run()
        self.wait()

    def status(self):
        self.subcmd = 'status'
        self.cmdpath = [self.maincmd, self.subcmd]
        self.run()
        self.wait()

    def diff(self, target=''):
        self.subcmd = 'diff'
        if self.revision == '':
            self.cmdpath = [self.maincmd,
                            self.subcmd,
                            '-r',
                            ':',
                            str(target)]

        else:
            if target == '':
                self.cmdpath = [self.maincmd,
                                self.subcmd,
                                '-r',
                                str(self.revision),
                                ':']
            else:
                self.cmdpath = [self.maincmd,
                                self.subcmd,
                                '-r',
                                str(self.revision),
                                ':',
                                str(target)]

        self.run()
        self.wait()

if __name__ == '__main__':
    import sys
    svn = Svn(sys.argv[1], sys.argv[2])
    svn.co()
    print svn.getOut()
    svn.info()
    print svn.getOut()
