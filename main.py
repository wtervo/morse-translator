#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from components.convert_file import convert_file
import os

#simple command line UI for the morse translator app
#actual functions are found in the components folder

if __name__ == "__main__":
	print("Welcome to the morse translator app!")
	print()
	print("Please select if you want to translate from")
	print("1 - (A)lphabet to Morse")
	print("2 - (M)orse to Alphabet")
	#while loops with error checks for user inputs
	while 1:
		print()
		selection = input("Make your selection: ").strip()
		if (selection == "1" or selection.lower() == "a"):
			target = 0
			break
		elif (selection == "2" or selection.lower() == "m"):
			target = 1
			break
		else:
			print()
			print("Error: Invalid input, choose 1 or 2 (a or m)")
	script_path = os.path.abspath(__file__) #absolute path of the main.py file
	input_files_path = os.path.join(os.path.split(script_path)[0], "data", "input")
	input_files = [f for f in os.listdir(input_files_path)] #find all files in the input dir (directories ignored)
	print()
	print("Current files in the input directory")
	for i in range(0, len(input_files)):
		print("%s - %s" % (i + 1, input_files[i]))
	print()
	print("Select a number from 1 to %s" % len(input_files))
	while 1:
		try:
			print()
			file_selection = int(input("Choose a file to translate: ").strip()) #only integers are accepted
		except ValueError:
			print()
			print("Error: Input is not an integer")
			continue
		else:
			if (file_selection > 0 and file_selection <= len(input_files)): #only integers in the appropriate range are accepted
				inputfile = input_files[file_selection - 1]
				break
			else:
				print()
				print("Error: Invalid number, choose from 1 to %s" % len(input_files))
				continue
	print()
	print("Choose the output file (default datatype is .txt)")
	print()
	while 1:
		print()
		output_selection = input("Write the name of the output file: ").strip()
		if (len(output_selection.split(".")) == 1):
			output_selection = output_selection + ".txt" #if no file type is given, defaults to .txt
			break
		elif (len(output_selection.split(".")) > 2): #if the filename has more than two dots, it is considered invalid
			print()
			print("Invalid filename")
			continue
		else:
			break
	print()
	print()
	try:
		convert_file(inputfile, output_selection, target) #actual conversion happens through here
	except Exception as e:
		print()
		print("An error occurred during translation:")
		print(e) #errors raised by child functions are displayed here
		print()
		print("App shutting down")
		print()
		deletepath = os.path.join(os.path.split(script_path)[0], "data", "output", output_selection)
		os.remove(deletepath) #if things go wrong, output file is removed to avoid cluttering the folder with useless stuff
	else:
		print()
		print("Translation successful!")
		print()
		print("The output has been saved in /data/%s" % output_selection)
		print()