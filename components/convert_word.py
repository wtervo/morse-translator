import convert_character as CC
from functools import reduce

def convert_word(word, target):
	"""
	A function to prepare a word for conversion with error checks and splits
	Arguments: word, target
	word is the string of characters to be converted
	target is the direction of conversion (numerical): 0: alphabet to morse, 1: morse to alphabet
	"""
	spread_word = list(word) #spreading the word to a list
	dot_arr = 0 #a value to keep track of how many consecutive dots the word has

	if (target == 1):
		for i in range(0, len(spread_word)):
			if (dot_arr > 1):
				print("Error: The word '%s' has an incorrect number of dots" % word) #if there is an even number of dots consecutively, an error is raised
				return
			elif (spread_word[i] == "."):
				dot_arr += 1
			else:
				dot_arr = 0
	else:
		#If the alphabetical word has, for example, "..." in it, the word must be handled before splitting it
		#so that the "middle" dots are included in the conversion, but not the separators
		for i in range(0, len(spread_word)):
			if (dot_arr != 0 and spread_word[i] != "." and dot_arr % 2 == 0):
				print("Error: The word '%s' has an incorrect number of dots" % word) #if there is an even number of dots consecutively, an error is raised
				return
			elif (dot_arr > 1 and spread_word[i] == "." and dot_arr % 2 == 0):
				spread_word[i - 1] = "x^$" #dummy string to replace later with a dot
				dot_arr += 1
			elif (spread_word[i] == "."):
				dot_arr += 1
			else:
				dot_arr = 0 #the running dot counter value is resetted on every other type of character

	split_word = "".join(spread_word).split(".")

	if (split_word[0] == ""): #splitting creates empty string values if the word has dots in its ends
		split_word = split_word[1:]
	if (split_word[-1] == ""):
		split_word = split_word[:-1]

	dots_corrected = list(map(lambda char: "." if char == "x^$" else char, split_word)) #replacing the dummy strings with dots

	try:
		converted_word = list(map(lambda char: CC.convert_character(char, target), dots_corrected))
	except Exception as e:
		print("Error: Word conversion failed: %s" % e)
	else:
		joined_converted_word = ".".join(tuple(converted_word)) #conversion to tuple for joining
		print(joined_converted_word)
		return joined_converted_word

		#.....a...b.c.....d...
test = convert_word("●−●−●−.●−●−●−.●−.●−●−●−.−●●●.−●−●.●−●−●−.●−●−●−.−●●.●−●−●−", 1)
#TODO: korjaa sanan alussa ja lopussa olevien pisteiden käsittely
#eli ts. parilliset pisteet pitää mennä silloin läpi, koska jos kyseessä string "..r",
#pitäisi splitin jälkeen saada lista [".", "r"] eikä error