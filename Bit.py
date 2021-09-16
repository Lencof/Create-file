# __Author__ __Lencof__
# Bit.py

Bit = '''
Bit
'''

# Open for 'w'riting
f = open('Bit.txt', 'w') # name file
# Write text to file
f.write(Bit)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Bit.txt') # name file
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
