This is an app for translating files with morse code or (English) alphabets into their counterpart.

Made as part of a job application process for Buutti.

How to use the app:

First you should create an input file (for example, test.txt) in the data/input/ directory.

IMPORTANT: If you wish to create a morse code file from scratch for the input, you MUST use the correct Unicode
symbols. The ones used in this app are 'MINUS SIGN' (U+2212) for the lines and 'BLACK CIRCLE' (U+25CF) for the dots.

In it, you can write what you wish with, but certain rules/restrictions:
1) every letter must be separated with a dot "."
2) every word must be separated with just one empty space " ", any more will trigger an error
3) beginning and end of a row cannot be a dot "."
4) when writing alphabets, it is not allowed to have an even number of dots between letters
(for example, "a.b..c.d" is not OK, but "a.b...c.d" is)

Please note that most special characters can not be converted, for example "!, #, '" to name a few.
This is due to them not being required in the task and me not wanting to bother to add them.

If you wish to use the built-in command console UI, run the file main.py, if not, then run convert_file.py with appropriate arguments

The UI first asks which way should the translation go, then lists the files in the input folder for the user to choose which one to
translate and lastly asks for the name (and datatype) of the output file.

If you get an error saying "Character somethingsomething does not have a matching value", check if you have accidentally chosen the
wrong type of conversion and if this does not help, you most likely have some forbidden character in the input file or your input
file datatype is something unreadable (like hello.kjhs).




Thanks for reading!

PS. Check the translate-me-to-alphabet.txt file