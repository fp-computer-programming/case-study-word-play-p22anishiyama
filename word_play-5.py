# Author: ATN 3/18/22

wordfile = open('words.txt')
line = wordfile.readline().strip()


# defined the function
def is_abecedarian():
    if line == line.sort() in line:
        return True
    else:
        return False

counter = 0

for line in wordfile:
    if is_abecedarian():
        counter += 1
        


# calling the function within the print statement for a value
print('{0} words found.'.format(counter))
