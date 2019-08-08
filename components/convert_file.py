#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from components.convert_word import convert_word


def convert_file(inputfile, outputfile, target):
	"""
	This function reads the file to be converted, separates words from it,
	calls the word conversion function and saves the converted words into a new file
	Arguments: inputfile, outputfile, target
	inputfile is the name of the file to be converted
	outputfile is the name of the file where the conversion result is saved
	target is the direction of conversion (numerical): 0: alphabet to morse, 1: morse to alphabet
	"""

	script_path = os.path.abspath(__file__)
	base_path = os.path.join(os.path.split(script_path)[0].split("components")[0], "data") #filepath joining to point to data folder

	input_path = os.path.join(base_path, "input", inputfile)
	input_f = open(input_path, "r", encoding="utf-8-sig") #utf8 both for read and write, utf-8-sig to avoid unwanted "\ufeff" string
	file_lines = []
	for line in input_f:
		if (line.strip() != ""): #empty lines are ignored
			file_lines.append(line.strip()) #strip empty spaces
	input_f.close()

	#checking for incorrect empty spaces before moving on
	for i in range(0, len(file_lines)):
		line_check_val = 0

		line_to_check = file_lines[i]
		for character in range(0, len(line_to_check)):
			if (line_check_val > 1):
				raise Exception("Error: The input file has too many empty spaces between words (text line %s)" % str(i + 1)) #if there are more than 1 spaces consecutively, an error is raised
			elif (line_to_check[character] == " "):
				line_check_val += 1
			else:
				line_check_val = 0

	output_path = os.path.join(base_path, "output", outputfile)
	output_f = open(output_path, "w+", encoding="utf-8-sig")

	for i in range(0, len(file_lines)):
		split_line = file_lines[i].split(" ")
		line_arr = []
		for j in range(0, len(split_line)):
			try:
				converted_word = convert_word(split_line[j], target)
			except Exception as e:
				output_f.close()
				raise Exception(e) #child functions raise their exceptions, which show here when needed
			else:
				line_arr.append(converted_word)
		joined_output = " ".join(tuple(line_arr)) #convert to tuple before joining
		output_f.write(joined_output + "\n")

	output_f.close()