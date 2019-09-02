# author: Carlos Dante Cervantes
# submission date: 09/01/2019
# os fall 2019
import sys
import re

# get file names from arguments
inputFile = sys.argv[1]

# create dictionary to hold words
repeatCount = dict()
fileContents = open(inputFile).read().lower()

# count all possible words in file (starts & ends with a letter and is between 1 and 30 characters long)
for word in re.findall(r'\b[a-z]{1,30}\b', fileContents):
    indexCount = repeatCount.get(word, 0)
    repeatCount[word] = indexCount + 1
wordList = repeatCount.keys()

# create file and write the output
outputFile = open(sys.argv[2], "w")
for keyWord in sorted(wordList):
    row = keyWord + " " + str(repeatCount[keyWord]) + "\n"
    outputFile.write(row)
outputFile.close()
