#!/usr/bin/python

import re


def getCpuModelName():
    prefix = re.compile('model\sname\s+:\s')
    sufix = re.compile('\n')
    modelname = ''

    with open('/proc/cpuinfo') as file:
        for line in file:
            modelname = prefix.sub('', line)
            if line != modelname:
                modelname = sufix.sub('', modelname)
                break
    return modelname


def getCpuCoreNum():
    prefix = re.compile('cpu\scores\s+:\s')
    sufix = re.compile('\n')
    cpunum = 0

    with open('/proc/cpuinfo') as file:
        for line in file:
            strnum = prefix.sub('', line)
            if line != strnum:
                corenum = int(sufix.sub('', strnum))
                break
    return corenum


def getMemTotal():
    prefix = re.compile('MemTotal:\s+')
    sufix = re.compile('\skB\n')
    memtotal = 0

    with open('/proc/meminfo') as file:
        for line in file:
            memtotal = prefix.sub('', line)
            if line != memtotal:
                memtotal = sufix.sub('', memtotal)
                break
    return memtotal

if __name__ == '__main__':

    print getCpuModelName()
    print getCpuCoreNum()
    print getMemTotal()
