# __Author__ __Lencof__
# Maze.py

import os
import sys

# file name README
# text description
Maze = '''
Maze
'''

# Open for 'w'riting
f = opne('Maze.txt', 'w') # name file
# Write text to file
f.write(Maze)
# Close the file
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Maze.txt') # name file
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
