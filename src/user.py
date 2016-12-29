#!/usr/bin/env python

class User:
	def __init__(self, id, name, path2file):
		self.id = id
		self.name = name
		self.path2file = path2file

	def getName(self):
		return self.name
	
	def getPath(self):
		return self.path2file

	def getId(self):
		return self.id


