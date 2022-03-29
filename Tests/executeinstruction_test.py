import os
import sys
from mock import patch, mock_open
sys.path.append(os.path.abspath(os.path.join('../src')))
from parser import Parser
from executeinstruction import ExecuteInstruction

class Test_executeinstruction:

    def test_shouldOrientToTheLeftDirection(self):
        # Given
        Testfielcoordinate = [5, 5]
        rubyinitialposition = [3, 3, 'EAST']
    

        expectedOutput = [3, 3, 'NORTH']

        # When
        execute = ExecuteInstruction(Testfielcoordinate,rubyinitialposition)
        result = execute.Left()
        # Then
        assert result == expectedOutput
    
    def test_shouldOrientToTheRightDirection(self):
        # Given
        Testfielcoordinate = [5, 5]
        rubyinitialposition = [3, 3, 'EAST']
    

        expectedOutput = [3, 3, 'SOUTH']

        # When
        execute = ExecuteInstruction(Testfielcoordinate,rubyinitialposition)
        result = execute.Right()
        # Then
        assert result == expectedOutput
    
    def test_shouldMoveForward(self):
        # Given
        Testfielcoordinate = [5, 5]
        rubyinitialposition = [3, 3, 'EAST']
    

        expectedOutput = [4, 3, 'EAST']

        # When
        execute = ExecuteInstruction(Testfielcoordinate,rubyinitialposition)
        result = execute.move()
        # Then
        assert result == expectedOutput