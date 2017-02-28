#!/usr/bin/python
# Filename: pluck.py

def pluck(dictionary, key):
	try:
		ages = [li[key] for li in dictionary]
		return ages
	except KeyError, e:
		raise KeyError('Key not found')
	except TypeError, e:
		raise TypeError('dictionary must be of type Array')
	
version = '0.1.1'

