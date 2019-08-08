#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importing the character array
from components.symbol_list import symbol_list

def convert_character(char, target):
	"""
	Function that searches the correct alphabet character or morse code character
	from an array and returns its corresponding opposite.
	Arguments: char, target
	char is the character to be converted (string)
	target is the direction of conversion (numerical): 0: alphabet to morse, 1: morse to alphabet
	"""
	if (target == 0):
		convert = 1 #the value of convert defines which value from the symbol array is to be returned
		char = char.upper()
	elif (target == 1):
		convert = 0
	else:
		raise Exception("Error: the second function argument can only be 0 or 1 (was %s)" % target)
	#filter the correct array corresponding the "char" argument
	found_target = list(filter(lambda char_pair: char_pair[target] == char, symbol_list))
	try:
		return_value = found_target[0][convert]
	except IndexError:
		raise Exception(" Character '%s' does not have a matching value" % char) #raise an error to stop conversion if any character in a word fails
	else:
		return return_value