#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from components.convert_character import convert_character

def convert_word(word, target):
	"""
	A function to prepare a word for conversion with error checks and splits
	Arguments: word, target
	word is the string of characters to be converted
	target is the direction of conversion (numerical): 0: alphabet to morse, 1: morse to alphabet
	"""
	spread_word = list(word) #spreading the word to a list
	dot_arr = 0 #a value to keep track of how many consecutive dots the word has

	#I considered allowing dots at the word's ends, but this would mean that
	#an even number of dots would be the correct input instead of odd (see below)
	#and I believe implementing that is beyond the scope of this task
	if (spread_word[0] == "." or spread_word[-1] == "."):
		raise Exception("Error: the word cannot have dots in the beginning or the end")

	if (target == 1):
		for i in range(0, len(spread_word)):
			if (dot_arr > 1):
				raise Exception("Error: The word '%s' has an incorrect number of dots" % word) #if there is an even number of dots consecutively, an error is raised
			elif (spread_word[i] == "."):
				dot_arr += 1
			else:
				dot_arr = 0
	elif (target == 0):
		#If the alphabetical word has, for example, "..." in it, the word must be handled before splitting it
		#so that the "middle" dots are included in the conversion, but not the separators
		for i in range(0, len(spread_word)):
			if (dot_arr != 0 and spread_word[i] != "." and dot_arr % 2 == 0):
				raise Exception("Error: The word '%s' has an incorrect number of dots" % word) #if there is an even number of dots consecutively, an error is raised
			elif (dot_arr > 1 and spread_word[i] == "." and dot_arr % 2 == 0):
				spread_word[i - 1] = "x^$" #dummy string to replace later with a dot
				dot_arr += 1
			elif (spread_word[i] == "."):
				dot_arr += 1
			else:
				dot_arr = 0 #the running dot counter value is resetted on every other type of character
	else:
		raise Exception("Error: the second function argument can only be 0 or 1 (was %s)" % target)

	split_word = "".join(spread_word).split(".")

	dots_corrected = list(map(lambda char: "." if char == "x^$" else char, split_word)) #replacing the dummy strings with dots

	try:
		converted_word = list(map(lambda char: convert_character(char, target), dots_corrected))
	except Exception as e:
		raise Exception("Error: Word conversion failed: %s" % e)
	else:
		joined_converted_word = ".".join(tuple(converted_word)) #conversion to tuple for joining
		return joined_converted_word