#!/usr/bin/python

import os
import shutil
import tarfile
import pwd
import socket
import stat


# Return True if specified argument is string
def isString(string):
    return isinstance(string, basestring)


def isFile(path):
    return os.path.isfile(path)


def isDir(path):
    return os.path.isdir(path)


def pwd():
    return os.getcwd()


def mkDir(path):
    if isDir(path):
        return False
    else:
        os.mkdir(path)
        return True


def chDir(path):
    if isDir(path):
        os.chdir(path)
        return True
    else:
        return False


def copy(srcPath, dstPath):
    if isFile(srcPath):
        shutil.copy2(srcPath, dstPath)
        return True
    elif isDir(srcPath):
        if not os.path.exists(dstPath):
            shutil.copytree(srcPath, dstPath)
            return True

    return False


def move(srcPath, dstPath):
    if os.path.exist(srcPath):
        shutil.move(srcPath, dstPath)
        return True
    else:
        return False


def chmod(path, mode):
    if os.path.exist(path):
        os.chmod(path, mode)
        return True
    else:
        return False


def checkMode(path, stmode):
    if os.path.exist(path):
        mode = oct(stat.S_IMODE(os.stat(path)[stat.ST_MODE]))
        if mode == stmode:
            return True

    return False


def isUpdated(srcPath, dstPath):
    if isFile(srcPath) and isFile(dstPath):
        if os.path.getmtime(srcPath) > os.path.getmtime(dstPath):
            return True
    return False


def tarDir(name, dirPath):
    tarName = str(name) + '.gz'
    print tarName
    if (not isFile(tarName)) and isDir(dirPath):
        tar = tarfile.open(tarName + '.gz', 'w|gz')
        tar.add(dirPath)
        tar.close()
        return True
    else:
        return False


def rmDirs(dirPath):
    if isDir(dirPath):
        shutil.rmtree(dirPath)
        return True
    else:
        return False


def findFile(file_name, dir_path=pwd()):
    file_list = []
    for dirpath, dirs, files in os.walk(dir_path):
        for target_file in files:
            if str(file_name) == str(target_file):
                file_path = dirpath + '/' + target_file
                if isFile(file_path):
                    file_list.append(file_path)
    return file_list


def findDir(dir_name, dir_path=pwd()):
    dir_list = []
    for dirpath, dirs, files in os.walk(dir_path):
        for target_dir in dirs:
            if str(dir_name) == str(target_dir):
                path = dirpath + '/' + target_dir
                if isDir(path):
                    dir_list.append(path)
    return dir_list


def hostname():
    return socket.gethostname()


def getFileSize(file):
    if isFile(file):
        return os.path.getsize(file)
    else:
        return -1


class A:
    def __init__(self):
        self.a = True
    def Print(self):
        print self.a

if __name__ == '__main__':
    mkDir('hoge')
    chDir('geho')
    copy('foo', 'hoge')
    isUpdated('chip', 'chop')
    tarDir('test.py', 'bar')
    print hostname()

    print 'start test'
    a = 1
    b = True
    c = A()
    d = 'h'
    e = 'hogehoge'
    for obj in a, b, c, d, e:
        print isString(obj)

        findFile('Makefile')
        findDir('lib')
