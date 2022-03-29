import os
import sys


sys.path.append(os.path.abspath(os.path.join('../src')))

from processinput import ProcessInput


def test_shouldCalculateFinalPositionForTwoRubyRobots(capsys):
        # Given
        inputFile = '../inputFile.txt'
        processinput = ProcessInput(inputFile)
    
    
        # When
        processinput.processInstructions()
        printedOutput = capsys.readouterr().out
        print(printedOutput)
        # Then
        expectedRubyFinalPositions = '1 2 W' + '\n' + '3 2 E' + '\n'
        assert expectedRubyFinalPositions == printedOutput