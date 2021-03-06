import re
import sys
sys.tracebacklimit=0

from logger import Logger



class Parser:
    """A Parser Class which parses the inputfile whether the file holds the right character.

    Parameters
    ----------
    filePath : str
        the file that will be parsed
    Returns
    -------
    None
    """
    def __init__(self,filePath: str ) -> None:
        self.logger = Logger("parser.log").get_app_logger()
        self.filePath =  filePath
    def parseFile(self) -> int:
        """Checks whether the value inside the file is valid to control the ruby robot.
        Parameters
        ----------
        None

        Returns
        -------
        tuple
            Returns tuple of the testfield coordinates and instructions for the ruby robot that is
            parsed from the file
        """
        try:
            validCoordinatesInput = re.compile("^[0-9]* [0-9]*$") 
            validRubyPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")
            validRubycommands = re.compile("[LRM]")
       
            with open(self.filePath, 'r') as input:
                testfieldInput = input.readline()
                Testfield = []
                if not re.match(validCoordinatesInput, testfieldInput):
                    self.logger.exception('Failed to extract test field coordinates')
                    raise ValueError("Invalid CoordinatesInput")
                
                inputStringAsList = testfieldInput.split()
                testfield = [int(inputStringAsList[0]), int(inputStringAsList[1])]
                Testfield.extend(testfield)
                self.logger.info('extracts Test field coordinates')
                rubyInstructions = []
                for lineCount, line in enumerate(input, 1):
                    if lineCount % 2 != 0:
                        if not re.match(validRubyPosition, line):
                            self.logger.exception('Invalid ruby initial position')
                            raise ValueError("Invalid ruby initial position")
                        inputLineAsList = line.split()
                        Direction = {'N': 'NORTH','S':'SOUTH','W':'WEST','E':'EAST'}
                        direction = Direction[inputLineAsList[2]]
                        RubyInitialPosition = [int(inputLineAsList[0]), int(inputLineAsList[1]),direction]
                        rubyInstructions.append(RubyInitialPosition)
                        self.logger.info('extracts ruby initial position')
              
                    else:
                        for l in line[:-1]:
                            if not re.match(validRubycommands, l):
                                self.logger.exception('Invalid ruby instruction')
                                raise ValueError("Invalid ruby instruction")
                        MovementCommand = {'L':'LEFT','R':'RIGHT','M':'FORWARD'}
                        commandsToMoveRuby = [MovementCommand[command] for command in list(line.replace('\n', ''))]
                        rubyInstructions.append(commandsToMoveRuby)
                        self.logger.info('extracts ruby instruction')
                return Testfield, rubyInstructions
        except Exception as e:
            self.logger.exception('Failed to parse')
            sys.exit(1)
        


        
