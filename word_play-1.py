# Author: ATN 3/16/22

# began by setting up the 2 files we are using and the method for getting a line
wordfile = open('words.txt')
line = wordfile.readline().strip()
greaterfile = open('greater_than_20.txt', 'w')

# going through each word in the file and checking if it meets this condition
for line in wordfile:
    if len(line) > 20:
        # adds this word to the file if it does
        greaterfile.write(line)
