# __Author__ __Lencof__
# File_Fav.py

Fav = '''
Fav
'''

# Open for 'w'riting
f = open('Fav.txt', 'w') # name file
# Write text to file
f.write(Fav)
# Close the file
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Fav.txt') # name file
while True: # use True
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
f.close() 
