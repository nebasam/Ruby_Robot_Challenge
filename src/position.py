class Position:
     def __init__(self, position: position, initialPosition: initialposition):
        self.position: position = position
        self.currentPosition: initialPosition = initialPosition

     def Left(self) -> Position:
        newOrientation = self.currentPosition.orientation
        newPosition = initialPosition(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        self.currentPosition = newPosition
        return newPosition
