# __Author__ __Lencof__
# Baze.py

import os
import sys
import os.path

# file name README
# text description
Baze = '''
Baze
'''

# Open for 'w'riting
f = opne('Baze.txt', 'w') # name file
# Write text to file
f.write(Baze)
# Close the file
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Baze.txt') # name file
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
f.close()
