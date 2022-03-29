import pytest
import os
import sys
from mock import patch, mock_open
sys.path.append(os.path.abspath(os.path.join('../')))
from src.parser import Parser


class Test_Parser:

    def test_shouldParseAValidSetOfInstructions(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMR\n2 2 N\nRMLM'

        parser = Parser(filePath)

        Testfielcoordinate = [5, 5]
        ruby1position = [3, 3, 'EAST']
        ruby2position = [2, 2, 'NORTH']
        rubyInstruction1 = ['FORWARD', 'FORWARD', 'RIGHT']
        rubyInstruction2 = ['RIGHT', 'FORWARD', 'LEFT', 'FORWARD']

        expectedSetOfInstructions = Testfielcoordinate,[ruby1position,rubyInstruction1,ruby2position,rubyInstruction2]

        # When
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            result = parser.parseFile()

        # Then
        assert result == expectedSetOfInstructions