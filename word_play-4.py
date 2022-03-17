# Author: ATN 3/17/22

wordfile = open('words.txt')
line = wordfile.readline().strip()


# defined the function
def uses_only(uses):
    counter = 0
    # checks if the line meets the requirements
    for line in wordfile:
        if uses in line:
            counter += 1
    return counter
            

uses = input('Please enter the string to include: ')

# calling the function within the print statement for a value
print('{0} words found.'.format(uses_only(uses)))
