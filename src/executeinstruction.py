import sys
sys.tracebacklimit=0


from logger import Logger


class ExecuteInstruction:
   """An ExecuteInstruction Class where it will executes the instructions for the ruby robot.
    Parameters
    ----------
    coordinate : list
        the test field coordinates
    initialPosition: list
        the initial position of ruby robot
    Returns
    -------
    None
    """

   def __init__(self, coordinate: list, initialPosition: list) -> None:
        self.logger = Logger("ExecutesInstruction.log").get_app_logger()
        self.Coordinate = coordinate,
        self.currentPosition = initialPosition

   def processInstruction(self, Instructions: list) -> None:
       """process instruction by mapping every letter to corresponding function.
        Parameters
        ----------
        Instructions: list
            the instructions used to move the ruby robot

        Returns
        -------
        None
      
        """
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
        """ Orients the ruby robot to the left.
        Parameters
        ----------
        None
        

        Returns
        -------
        list 
          the new position of the ruby robot
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

        
   def Right(self) -> list:
       """ Orients the ruby robot to the right
        Parameters
        ----------
        None
        

        Returns
        -------
        list 
          the new position of the ruby robot
        """
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
        

   def move(self) -> list:
       """ moves the ruby robot forward.
        Parameters
        ----------
        None
        

        Returns
        -------
        list 
          the new position of the ruby robot
        """
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
