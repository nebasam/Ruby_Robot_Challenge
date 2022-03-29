class Position:
     def __init__(self, position: position, initialPosition: initialposition):
        self.position: position = position
        self.currentPosition: Position = initialPosition

     def Left(self) -> Position:
        newOrientation = self.currentPosition.orientation
        newPosition = Position(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition
     def Right(self) -> Position:
        newOrientation = self.currentPosition.orientation
        newPosition = Position(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition

     def move(self) -> Position:
        
        newRoverPosition = self.currentPosition.orientation
        self.currentPosition = newRoverPosition
        return self.currentPosition
