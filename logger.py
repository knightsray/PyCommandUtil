#!/usr/bin/python

# test logging module

import logging


class Logger():
    def __init__(self, name='default', filename='default_file.log',
                 level='DEBUG'):
        self.name = name
        self.filename = filename
        self.filemode = 'a'
        self.level = level
        self.format = '%(asctime)s: %(levelname)s: %(name)s: %(message)s'

        logging.basicConfig(filename=self.filename, filemode=self.filemode,
                            level=self.level, format=self.format)

    def __del__(self):
        logging.shutdown()

    def getLog(self):
        return logging.getLogger(self.name)


def main():
    LOGFILE = 'log.txt'
    LOGLEVEL = 'DEBUG'
    LOGNAME = 'log_test'

    log = Logger(LOGNAME, LOGFILE, LOGLEVEL).getLog()

    log.debug('debug message')
    log.info('info message')
    log.warn('warn message')
    log.error('error message')
    log.critical('critical message')


if __name__ == '__main__':
    main()
