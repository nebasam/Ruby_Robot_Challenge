# Ruby_Robot_Challenge
The objective of this project is to develop Prototypes of a squad of ruby robots s. A ruby robot
is a robot which is able to explore and interact with the outer world in some degree by moving and exploring. This project navigate our Ruby Robots through an open field and test its Geo cache mapping functionality.

The robot's position is represented by a combination of an x and y coordinates and a letter representing one of the four cardinal compass points. The test field is divided up into a grid to simplify navigation. An example position might be 1, 1, N, meaning our robot is in the bottom
left corner and facing North.

In order to control the ruby robot, we can send a simple string of letters. The only valid possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes our robot spin 90 degrees left or right respectively, without moving from its current position. 'M' means move forward one grid point, and maintain the same heading. Assume that the square directly North from (x, y) is (x, y+1).

## Input

The first line of input is the upper-right coordinates of the test field, the lower-left coordinates are assumed to be 0,0. The rest of the input is information to the robots that have been deployed. Each robot has two lines of input. The first line gives the robot's position, and the second line is a series of instructions telling the robot how to explore the test field.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the robot orientation. Each robot run will be finished sequentially/

## Output
The output for each robot should be its final coordinates and heading.

### The InputFile that is used for the project
```
10 10
2 3 E
RMRMRLMRMRMRMR
5 4 W
LMRMLMRMRLMRRM

```
### The Output from the project
```
1 2 W
3 2 E

```

## Project Structure

.github                        # github workflows for dockerizing the code

logs
|__ExecutesInstruction.log     # log file for ExecutesInstruction script
|__parser.log                  # log file for parser script
|__ProcessInput.log            # log file for ProcessInput script

src
|__app.py                      # script for running the whole project
|___executeinstruction.py      # script for executing the instruction
|___parser.py                  # script for parsing input file
|___processinput.py            # script for processing input

Tests
|__executeinstruction_test.py  # script for testing executinginstruction function
|__parser_test.py              # script for testing parser function
|__processinput_test.py        # script for testing processinput function

inputFile.txt                  # inputFile for controlling the robot

## How to install and use

1) Using git clone
```
git clone https://github.com/nebasam/Ruby_Robot_Challenge
cd Ruby_Robot_Challenge/src
python3 app.py
```

2) Using Docker
```
docker pull nebasam/ruby:latest
docker run nebasam/ruby

```

## To run the tests

```
python3 pytest <script name>
```