#!/usr/bin/python

import os, shutil, tarfile, pwd

def isString(string):
	return isinstance(string, basestring)

def pwd():
	return os.getcwd()

def mkdir(path):
	if isString(path) and os.path.isdir(path):
		return False
	else:
		os.mkdir(path)
		return True

def chdir(path):
	if isString(path) and os.path.isdir(path):
		os.chdir(path)
		return True
	else:
		return False

def copy(srcPath, dstPath):
	if not (isString(srcPath) and isString(dstPath)):
		return False

	if os.path.isfile(srcPath) and os.path.isdir(dstPath):
		shutil.copy2(srcPath, dstPath)
		return True
	else:
		return False

def isUpdated(srcPath, dstPath):
	if not (isString(srcPath) and isString(dstPath)):
		return False

	if os.path.isfile(srcPath) and os.path.isfile(dstPath):
		if os.path.getmtime(srcPath) > os.path.getmtime(dstPath):
			return True
	return False

def tarDir(name, dirPath):
	tarName = str(name) + '.gz'
	print tarName
	if (not os.path.isfile(tarName)) and os.path.isdir(dirPath):
		tar = tarfile.open(tarName + '.gz', 'w|gz')
		tar.add(dirPath)
		tar.close()
		return True
	else:
		return False

def rmDirs(path):
	if isString(path) and os.path.isdir(dirPath):
		shutil.rmtree(path)
		return True
	else:
		return False

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


