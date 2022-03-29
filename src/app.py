from src.processinput import ProcessInput



def main():
    inputFile = 'inputFile.txt'
    processinput = ProcessInput(inputFile)
    processinput.processInstructions()


if __name__ == '__main__':
    main()