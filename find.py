#!/usr/bin/env python

# The "import" statement finds modules (whatever those are!) and defines names
# in a namespace (whatever that is!):                                                                          
#                                                                                                              
#   http://docs.python.org/reference/simple_stmts.html#the-import-statement                                    
#                                                                                                              
# The "sys" module provides things related (apparently) to the interpreter
# (whatever that is!):                                                                                         
#                                                                                                              
#   http://docs.python.org/library/sys.html

#this opens the sys library
import sys

# This Variable is the error output for a syntax error"
USAGE = "Usage: ./find.py word filename [filename]*"

# This is the function that is called when there is an error.

def fail(msg):

# This is the error message that always prints out. sys.stderr is the the error message from the OS
    print >> sys.stderr, USAGE

    print >> sys.stderr, msg
 # This exits the python script
    sys.exit()
# this loads the first argument in the the varable "word"
# If if fails it calls the fail function and passes the text "Please provide the word to find."
# to be printed in the error message. 
try:
    word = sys.argv[1]
except:
    fail("Please provide a word to find.")

# this loads all the arguments 2 and greater into the variable "filenames"

filenames = sys.argv[2:]
# If filenames is empty call the fail function 
if not filenames:
    fail("Please enter at least one filename.")
# this loop iterates though every value in filenames and puts the value into the variable filename.

for filename in filenames:
    # This opens the file, unless there is an error then it will throw and error and the
    # continue statement will move on the the next line and not stop the script. 

    try:
        file_pointer = open(filename)
    except IOError:
        print >> sys.stderr, "Could not open file:", filename
        continue

    #this loop scans every line and look for the value of the word and print the name of the file if the
    #value is in the line. The break statement exits the loop and continues on the "for filename in 
    #filenames" loop

    for line in file_pointer:
        if word in line:
            print filename
            break