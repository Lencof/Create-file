# __Author__ __Lencof__
# Baze.py

Baze = '''
Baze
'''

# Open for 'w'riting
f = open('Baze.txt', 'w') 
f.write(Baze)
f.close()

# 'r'ead mode is assumed by default
f = open('Baze.txt') 
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
