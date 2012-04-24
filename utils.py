#!/usr/bin/python

import os, shutil, tarfile, pwd


# Check whether specified argument is string
def isString(string):
    return isinstance(string, basestring)

def isFile(path):
    return os.path.isfile(path)

def isDir(path):
    return os.path.isdir(path)

def pwd():
    return os.getcwd()

def mkDir(path):
    if  isDir(path):
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
    if isFile(srcPath) and isDir(dstPath):
        shutil.copy2(srcPath, dstPath)
        return True
    else:
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

def rmDirs(path):
    if isDir(dirPath):
        shutil.rmtree(path)
        return True
    else:
        return False

def findFile(file_name, dir_path = pwd()):
    list = []
    for dirpath, dirs, files in os.walk(dir_path):
        for file in files:
            if str(file_name) == str(file):
                path = dirpath + '/' + file
                if isFile(path):
                    list.append(path)
    return list 
            

def findDir(dir_name, dir_path = pwd()):
    list = []
    for dirpath, dirs, files in os.walk(dir_path):
        for dir in dirs:
            if str(dir_name) == str(dir):
                path = dirpath + '/' + dir
                if isDir(path):
                    list.append(path)
    return list 

class A:
	def __init__(self):
		a = True

if __name__ == '__main__':
	mkdir('hoge')
	chdir('geho')
	copy('foo', 'hoge')
	isUpdated('chip', 'chop')
	tarDir('test.py', 'bar')

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

