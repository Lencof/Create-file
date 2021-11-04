# __Author__ __Lencof__
# Norton.py

Norton = '''
Norton
'''

# Open for 'w'riting
f = open('Norton.txt', 'w') # name file
f.write(Norton)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Norton.txt') # name file
while True: 
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
f.close() 
