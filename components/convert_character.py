#importing the character array
import symbol_list as SL

def convert_character(char, target):
	"""
	Function that searches the correct alphabet character or morse code character
	from an array and returns its corresponding opposite.
	Arguments: char, target
	char is the character to be converted (string)
	target is the direction of conversion (numerical): 0: alphabet to morse, 1: morse to alphabet
	"""
	if (target == 0):
		convert = 1 #the value of convert defines which value is to be returned
		char = char.upper()
	elif (target == 1):
		convert = 0
	else:
		print("Error: the second function argument can only be 0 or 1 (was %s)" % target)
		return
	#filter the correct array corresponding the "char" argument
	found_target = list(filter(lambda char_pair: char_pair[target] == char, SL.symbol_list))
	try:
		return_value = found_target[0][convert]
	except IndexError:
		raise Exception(" Character '%s' does not have a matching value" % char) #raise an error to stop conversion if any character in a word fails
	else:
		return return_value