from src.executesinstruction import ExecutesInstruction
from src.parser import Parser

inputFile = 'inputFile.txt'
print('here')
parser= Parser(inputFile)
Testfieldcoordinate, Instruction = parser.parseFile()
print(Instruction)
execute  = ExecutesInstruction(Testfieldcoordinate, Instruction[0])
execute.processInstruction(Instruction[1])
Directions = {
            'NORTH': 'N',
            'WEST': 'W',
            'SOUTH': 'S',
            'EAST': 'E'
        }
execute.currentPosition = [execute.currentPosition[0], execute.currentPosition[1], Directions[execute.currentPosition[2]]]
print(' '.join(map(str,execute.currentPosition)))