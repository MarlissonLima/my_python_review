'''
The sys module in Python provides varius functions and variables that are
used to manipulate different parts of the Pyhton runtime enviroment.It allows interact strongly
with the interpreter


Input and output using sys:
    *stdin
    *stdout
    *stderr
'''

import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print('Exit')

sys.stdout.write('something')