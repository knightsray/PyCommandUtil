#!/usr/bin/python

import os
import sys

def main(field, target, src, dst=None):
    if dst == None:
        dst_file = sys.stdout
    else:
        dst_file = open(dst, 'w')

    src_file = src

    with open(src_file, 'r') as src:
        for line in src:
            if line.find(field) != -1:
                dst_file.write(str(target) + '\n')
            else:
                dst_file.write(line)

    if dst != None:
        dst_file.close()


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) == 4:
        main(argv[1], argv[2], argv[3])
    else:
        main(argv[1], argv[2], argv[3], argv[4])

