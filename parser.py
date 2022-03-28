import re


class Parser:

   def parseFile(self, filePath: str) -> int:
       
       validCoordinatesInput = re.compile("^[0-9]* [0-9]*$")
       validRubyPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")
       
       with open(filePath, 'r') as input:
            testfieldInput = input.readline()
            if not re.match(validCoordinatesInput, testfieldInput):
                raise ValueError("Invalid test field coordinates")
            inputStringAsList = testfieldInput.split()
            testfield = int(inputStringAsList[0]), int(inputStringAsList[1])

            rubyInstructions = []
            for lineCount, line in enumerate(input, 1):
                if lineCount % 2 != 0:
                    if not re.match(validRubyPosition, line):
                        raise ValueError("Invalid ruby initial position")
                    inputLineAsList = line.split()
                    Orientation = {'N': 'NORTH','S':'SOUTH','W':'WEST','E':'EAST'}
                    orientation = Orientation[inputLineAsList[2]]
                    RubyInitialPosition = int(inputLineAsList[0]), int(inputLineAsList[1]),orientation
                else:
                    MovementCommand = {'L':'LEFT','R':'RIGHT','M':'FORWARD'}
                    commandsToMoveRuby = [MovementCommand[command] for command in list(line.replace('\n', ''))]
                    RubyInstruction = RubyInitialPosition, commandsToMoveRuby
                    rubyInstructions.append(RubyInstruction)
       return testfield, rubyInstructions


        
