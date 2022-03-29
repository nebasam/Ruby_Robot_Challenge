import sys


from src.executeinstruction import ExecuteInstruction
from src.parser import Parser
from src.logger import Logger


class ProcessInput:
    def __init__(self, inputfile: str):
        self.logger = Logger("ProcessInput.log").get_app_logger()
        self.inputFile = inputfile
    def processInstructions(self):
        try:
            parser= Parser(self.inputFile)
            Testfieldcoordinate = parser.parseFile()
            Testfieldcoordinate, Instructions = parser.parseFile()
            for index, Instruction in enumerate(Instructions):
                if index % 2 == 0:
                    # print(f'if{Instruction}')
                    execute  = ExecuteInstruction(Testfieldcoordinate, Instruction)
                else: 
                    # print(f'else {Instruction}')
                    execute.processInstruction(Instruction)
                    Directions = {
                        'NORTH': 'N',
                        'WEST': 'W',
                        'SOUTH': 'S',
                        'EAST': 'E'
                        }
                    execute.currentPosition = [execute.currentPosition[0], execute.currentPosition[1], Directions[execute.currentPosition[2]]]
                    self.logger.info('Extracts Final Position')
                    print(' '.join(map(str,execute.currentPosition)))
        except Exception as e:
            self.logger.exception('Failed to process input')
            sys.exit(1)