# __Author__ __Lencof__
# File_Ags.py

Ags = '''
'''

# Open for 'w'riting
f = open('Ags.txt', 'w') 
f.write(Ags)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Ags.txt')
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
