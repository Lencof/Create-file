# __Author__ __Lencof__
# File_Onef.py

import os

Onef = '''
Hello Onef
'''

# Open for 'w'riting
f = opne('Onef.txt', 'w') # name file
# Write text to file
f.write(Onef)
# Close the file
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Onef.txt') # name file
while True: # use True
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close() # close()
