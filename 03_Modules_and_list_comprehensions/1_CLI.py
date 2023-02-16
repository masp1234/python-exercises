import sys

def takeCommand(command):
    print(command)
    if len(command) == 1:
        print('Usage: python script.py [-it] {--rm}')
    if len(command) == 2 and command[1] == '-it':
        print('Interactive terminal started')
    if len(command) == 3 and command[2] == '--rm':
        print('Will be removed at exit')
    
    




takeCommand(sys.argv)

