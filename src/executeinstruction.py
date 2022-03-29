import sys
sys.tracebacklimit=0


from logger import Logger


class ExecuteInstruction:

    def __init__(self, coordinate: list, initialPosition: list):
        self.logger = Logger("ExecutesInstruction.log").get_app_logger()
        self.Coordinate = coordinate,
        self.currentPosition = initialPosition

    def processInstruction(self, Instructions: list) -> list:
       try:
          MovementInstruction = {'L':'LEFT','R':'RIGHT','M':'FORWARD'}
          for Instruction in Instructions:
            if Instruction == MovementInstruction['R']:
                self.Right()
            if Instruction == MovementInstruction['L']:
                self.Left()
            if Instruction== MovementInstruction['M']:
                self.move()
          self.logger.info('Processed Instruction')
       except Exception as e:
            self.logger.exception('Failed to process Instruction')
            sys.exit(1)
    
    def Left(self) -> list:
        """
        """
        try:
           leftDirectionMapping = {
            'NORTH': 'WEST',
            'WEST': 'SOUTH',
            'SOUTH': 'EAST',
            'EAST': 'NORTH'
            }
           newDirection= leftDirectionMapping[self.currentPosition[2]]
           newPosition = [self.currentPosition[0], self.currentPosition[1], newDirection]
           self.currentPosition = newPosition
           return newPosition
        except Exception as e:
            self.logger.exception('Failed to orient the ruby to the left direction')
            sys.exit(1)

        
    def Right(self):
       try:
          rightDirectionMapping = {
            'NORTH': 'EAST',
            'WEST': 'NORTH',
            'SOUTH': 'WEST',
            'EAST': 'SOUTH'
            }
          newOrientation = rightDirectionMapping[self.currentPosition[2]]
          newPosition = [self.currentPosition[0], self.currentPosition[1], newOrientation]
          self.currentPosition = newPosition
          return newPosition
       except Exception as e:
            self.logger.exception('Failed to orient the ruby to the right direction')
            sys.exit(1)
        

    def move(self):
       try:
         moveMappingTable = {
            'NORTH': [self.currentPosition[0], self.currentPosition[1] + 1, self.currentPosition[2]],
            'SOUTH': [self.currentPosition[0], self.currentPosition[1] - 1, self.currentPosition[2]],
            'WEST':  [self.currentPosition[0] - 1, self.currentPosition[1], self.currentPosition[2]],
            'EAST':  [self.currentPosition[0] + 1, self.currentPosition[1], self.currentPosition[2]]
         }
         newPosition = moveMappingTable[self.currentPosition[2]]
         if (newPosition[0] > self.Coordinate[0][0] or newPosition[0] > self.Coordinate[0][1]):
            self.logger.exception('ruby position out of testfield coordinate')
            print('ruby cannot be driven out of testfield coordinate')
            raise ValueError("ruby cannot be driven out of testfield coordinate")
         self.currentPosition = newPosition
        
         return self.currentPosition
       except Exception as e:
            self.logger.exception('Failed to move the robot')
            sys.exit(1)
