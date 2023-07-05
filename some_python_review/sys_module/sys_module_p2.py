#Command line arguments

'''
Command-line arguments are those which are passed during the aclling of the program
along with the calling statement

The sys module provide a variable called sys.argv.the main purpose is:
    * It is a list of command-line arguments
    * len(sys.argv) provides the number of command-line arguments
    * sys.argv[0] is the name of the current Python script

'''

import sys
#total arguments
total_arg = len(sys.argv)
print(f'Total arguments passed: {total_arg}')

#arguments passed
print(f"\nName of python script:{sys.argv[0]}")

print("\nArguments passed:",end=" ")
for i in range(1,total_arg):
    print(sys.argv[i],end=" ")

#addition of numbers
sum = 0

for i in range(1,total_arg):
    sum+=int(sys.argv[i])

print("\n\nresult: ",sum)
