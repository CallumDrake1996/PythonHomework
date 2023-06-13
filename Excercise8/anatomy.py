# !/usr/bin/python

# example python script

import sys

# argv is part of the sys module
# argument (it is the parameters to get into something) vector aka the list of parameters or inputs to the program

# argc is our variable
argument_count = len(sys.argv)
#  'if' is called a condition expression
if argument_count > 1:
    print('Too many args')

else:
    # where is a variable whose value is  a string 'world'
    where = 'World'
    print('hello', where)
# will print as it is not indented
print('goodbye from ' + sys.argv[0])

