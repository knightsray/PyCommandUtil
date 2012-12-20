#!/usr/bin/python

import threading
import logging
import time


class Logger():
    def __init__(self, name='default', filename='default_file.log',
                 level=logging.DEBUG):
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


class ProcessStatus():
    def __init__(self, logger):
        self.state = 'init'
        self.lock = threading.Lock()
        self.log = logger

    def setRunning(self):
        self.lock.acquire()
        self.state = 'running'
        self.lock.release()

    def setFin(self):
        self.lock.acquire()
        self.state = 'fini'
        self.lock.release()

    def getStatus(self):
        self.lock.acquire()
        self.log.debug('Process status is ' + self.state)
        stat = self.state
        self.lock.release()
        return stat

def fini_timer(status, log):
    interval = 10
    cond = threading.Condition()
    cond.acquire()
    cond.wait(interval)
    cond.release()
    fini(status, log)

def init():
    LOGFILE = 'test.log'
    LOGLEVEL = logging.DEBUG
    LOGNAME = 'test'

    log = Logger(LOGNAME, LOGFILE, LOGLEVEL).getLog()
    log.info('Initialize.')

    status = ProcessStatus(log)

    timer = threading.Thread(target=fini_timer, args=(status, log))
    timer.start()

    return status, log


def main(status, log):
    log.info('Start main function.')
    status.setRunning()

    while status.getStatus() == 'running':
        time.sleep(1)
    
    log.info('Finish main function.')


def fini(status, log):
    log.info('Finalize.')
    status.setFin()


if __name__ == '__main__':
    status, log = init()

    main(status, log)

