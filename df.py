from parser import Parser

inputFile = 'inputFile.txt'
parser= Parser(inputFile)
setOfInstructions = parser.parseFile()
print(setOfInstructions)