# __Author__ __Lencof__
# File_Capa.py

Capa = '''
 Capa 
'''

# Open for 'w'riting
f = open('Capa.txt', 'w') # name file
f.write(Capc)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('Capc.txt') # name file
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
