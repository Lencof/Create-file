# __Author__ __Lencof__
# File_Askola.py

Askola = '''
Hi!
'''

f = open('Askola.txt', 'w')
f.write(Askola)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Askola.txt') # name file
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
