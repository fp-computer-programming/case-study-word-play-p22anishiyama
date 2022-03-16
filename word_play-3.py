# Author: ATN 3/16/22

wordfile = open('words.txt')
line = wordfile.readline().strip()

counter = 0

def avoid(text):
    for line in wordfile:
        if text in line:
            counter += 1

forbidden = input('Please enter the string to exclude: ')
avoid(forbidden)

print('{0} words found.'.format(counter))
