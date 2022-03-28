import re

from logger import Logger


class Parser:
    def __init__(self,filePath: str ):
        self.logger = Logger("parser.log").get_app_logger()
        self.filePath =  filePath
    def parseFile(self) -> int:
        
       
       validCoordinatesInput = re.compile("^[0-9]* [0-9]*$")
       validRubyPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")
       
       with open(self.filePath, 'r') as input:
            testfieldInput = input.readline()
            if re.match(validCoordinatesInput, testfieldInput):
                inputStringAsList = testfieldInput.split()
                testfield = int(inputStringAsList[0]), int(inputStringAsList[1])
            else:
                print('Invalid test field coordinates')
                self.logger.exception('Invalid test field coordinates')
            rubyInstructions = []
            for lineCount, line in enumerate(input, 1):
                if lineCount % 2 != 0:
                    if re.match(validRubyPosition, line):
                        inputLineAsList = line.split()
                        Direction = {'N': 'NORTH','S':'SOUTH','W':'WEST','E':'EAST'}
                        direction = Direction[inputLineAsList[2]]
                        RubyInitialPosition = int(inputLineAsList[0]), int(inputLineAsList[1]),direction
                        self.logger.info('extracts ruby initial position')
                    else:
                        print('Invalid ruby initial position')
                        self.logger.exception('Invalid test field coordinates')
                else:
                    MovementCommand = {'L':'LEFT','R':'RIGHT','M':'FORWARD'}
                    commandsToMoveRuby = [MovementCommand[command] for command in list(line.replace('\n', ''))]
                    RubyInstruction = RubyInitialPosition, commandsToMoveRuby
                    rubyInstructions.append(RubyInstruction)
                    self.logger.info('extracts ruby instruction')
       return testfield, rubyInstructions


        
