import sys
sys.path.append('.')


import os
from ressistant.launch.Loadings import ReadList, getCNList, getENList


def resetLog(listNo):
    os.remove('log/List_' + str(listNo) + '.log')


def hello(argv):
    if argv[0] == '-r':
        if os.path.isfile('log/List_' + argv[1] + '.log'):
            print('Are you sure to reset list log ' + str(argv[1]) + '? (y/n)')
            answer = input()
            if answer == 'n':
                return
            if answer == 'y':
                resetLog(int(argv[1]))
            else:
                print('exit reset mode without changing anything...')
        else:
            print('log ' + argv[1] + ' not found')
    elif argv[0] == '-c':
        if os.path.isfile('log/List_' + argv[1] + '.log'):
            temp = ''
            with open('log/List_' + argv[1] + '.log', 'r') as log:
                print('Correction: ' + log.readline()[:-1])
                print('Count: ' + log.readline()[:-1])
        else:
            print('log ' + argv[1] + ' not found')
    elif argv[0] == '-g':
        print('read')
        if os.path.isfile('list/List_' + argv[1] + '.md'):
            list = []
            for i, list_num in enumerate(argv[1:]):
                list.append(ReadList(list_num))
            
            enList = getENList(list)
            cnList = getCNList(list)
            