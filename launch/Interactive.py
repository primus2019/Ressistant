import sys
sys.path.append('.')


import random
import time
from ressistant.launch.Loadings import showUsage


def EndTest():
    print('End of test today, bye.')


def ChooseList():
    print('Choose the list you want to recite: ')
    return input()


def TestByCN(listNo, ENList, CNList, log):
    log.seek(0, 0)
    correction = [(int)(record)
                  for record in log.readline()[:-1] if record != ' ']
    # print(correction)
    histories = [(int)(record)
                 for record in log.readline()[:-1] if record != ' ']
    # print(histories)
    TCNList = CNList.copy()
    random.shuffle(TCNList)
    for mngs in TCNList:
        for mng in mngs[1:]:
            print(mng + '\n')
            time.sleep(0.8)
            for cnt, word in enumerate(ENList):
                print((str)(cnt + 1) + word[1], end=' ')
            print('\nYour answer is: ', end='')
            answer = input()
            while not answer.isnumeric():
                print('Enter the numeric options above, or enter "999" to exit.\nYour answer is: ')
                answer = input()
            if int(answer) == mngs[0]:
                print('Great.\n')
                correction[mngs[0] - 1] += 1
                histories[mngs[0] - 1] += 1
            elif answer == '999':
                print('manually exit')
                exit(0)
            else:
                print('Right answer: ' + (str)
                      (mngs[0]) + ENList[mngs[0] - 1][1] + '\n')
                histories[mngs[0] - 1] += 1
            showUsage()
            time.sleep(0.5)
    log.seek(0,0)
    log.truncate()
    for record in correction:
        if record != ' ':
            log.write((str)(record) + ' ')
    log.write('\n')
    for record in histories:
        if record != ' ':
            log.write((str)(record) + ' ')
