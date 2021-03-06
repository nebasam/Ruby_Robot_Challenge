import sys


from executeinstruction import ExecuteInstruction
from parser import Parser
from logger import Logger


class ProcessInput:
    """A ProcessInput Class where it will process the input after it is parsed 
       by using execueting scripts then print the output.
    Parameters
    ----------
    inputfile : str
        the file that will be processed
    Returns
    -------
    None
    """
    def __init__(self, inputfile: str):
        self.logger = Logger("ProcessInput.log").get_app_logger()
        self.inputFile = inputfile
    def processInstructions(self):
        """process the instructions that is extracted from a file.
        Parameters
        ----------
        None

        Returns
        -------
        str
            Returns final position of the ruby robots
        """
        try:
            parser= Parser(self.inputFile)
            Testfieldcoordinate, Instructions = parser.parseFile()
            for index, Instruction in enumerate(Instructions):
                if index % 2 == 0:
                    execute  = ExecuteInstruction(Testfieldcoordinate, Instruction)
                else: 
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