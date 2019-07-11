import os


def resetLog(listNo):
    os.remove('log/List_' + str(listNo) + '.log')


def hello(argv):
    if argv[0] == '-r':
        print('Are you sure to reset list log ' + str(argv[1]) + '? (y/n)')
        if input() == 'y':
            resetLog(int(argv[1]))
        elif input() == 'n':
            pass
        else:
            print('exit reset mode without changing anything...')
    elif argv[0] == '-c':
        if os.path.isfile('log/List_' + argv[1] + '.log'):
            with open('log/List_' + argv[1] + '.log', 'r') as log:
                print('Correction: ' + log.readline()[:-1])
                print('Count: ' + log.readline()[:-1])
        else:
            print('log ' + argv[1] + ' not found')
    elif argv[0] == '-':
        if os.path.isfile('list/List_' + argv[1] + '.md'):
            pass
