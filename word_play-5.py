# Author: ATN 3/18/22

wordfile = open('words.txt')
line = wordfile.readline().strip()

counter = 0

def is_abecedarian(line):
    if line == ''.join(sorted(line)) in line:
        return True
    else:
        return False
        

for line in wordfile:
    if is_abecedarian(line):
        counter += 1

# calling the function within the print statement for a value
print('{0} words found.'.format(counter))
