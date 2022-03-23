# Author: ATN 3/23/22

wordfile = open('words.txt')
line = wordfile.readline().strip()


# created a blank list to handle the words given
words = []


# defined the function
def is_abecedarian(line):
    counter = 0
    while counter < len(line) - 1:
        # checks if the line meets the requirements
        if line[counter + 1] < line[counter]:
            return False
        counter += 1
    return True


# goes through each line of the file while calling upon the function
for line in wordfile.readline().strip():
    if is_abecedarian(line):
        words.append(line)

# finding the amount of terms within the print statement using len()
print('{0} words found.'.format(len(words)))
