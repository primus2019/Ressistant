import time
import random
import os


def ReadList(listNumber):
    try:
        lists = [line for line in open(
            "list/List_" + (str)(listNumber) + ".md", encoding="utf8")]
    except FileNotFoundError:
        print('List not found!')
        exit(0)
    vol, cnt = [], -1
    for line in lists:
        if line[0] == '-':
            cnt = cnt + 1
            vol.append([line[1:-1]])
        elif line[0] == '\n':
            continue
        else:
            tcnt, cn, en = 0, '', ''
            for word in line:
                if word == '*':
                    tcnt += 1
                elif tcnt == 2 and word != '*':
                    cn += word
                elif tcnt == 4 and word != '*' and word != '\n':
                    en += word
            vol[cnt].append([cn, en[1:]])
    return vol


def ENList(vol):
    return [[cnt + 1, word[0]] for cnt, word in enumerate(vol)]


def CNList(vol):
    CNList = []
    cnt = -1
    for word in vol:
        cnt += 1
        CNList.append([cnt + 1])
        for mng in word[1:]:
            CNList[cnt].append(mng[0])
    # print(CNList)
    return CNList


def TestByCN(listNo, ENList, CNList, log):
    log.seek(0, 0)
    correction = [(int)(record) for record in log.readline()[:-1] if record != ' ']
    # print(correction)
    histories = [(int)(record) for record in log.readline()[:-1] if record != ' ']
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
            if (int)(input()) == mngs[0]:
                print('Great.\n')
                correction[mngs[0] - 1] += 1
                histories[mngs[0] - 1] += 1
            else:
                print('Right answer: ' + (str)
                        (mngs[0]) + ENList[mngs[0] - 1][1] + '\n')
                histories[mngs[0] - 1] += 1
            time.sleep(0.5)
    log.seek(0)
    log.truncate()
    for record in correction:
        if record != ' ':
            log.write((str)(record) + ' ')
    log.write('\n')
    for record in histories:
        if record != ' ':
            log.write((str)(record) + ' ')


def EndTest():
    print('End of test today, bye.')


def ChooseList():
    print('Choose the list you want to recite: ')
    return input()

def ReadLog(listNo, ENList):
    fileName = 'log/List_' + (str)(listNo) + '.log'
    if not os.path.isfile(fileName):
        os.mkdir('log')
        with open(fileName, 'a+') as log:
            for word in ENList:
                log.write((str)(0) + ' ')
            log.write('\n')
            for word in ENList:
                log.write((str)(0) + ' ')
    return open(fileName, 'a+')


def SumByEN(listNo, ENList, log):
    log.seek(0, 0)
    correction = [(int)(record) for record in log.readline()[:-1] if record != ' ']
    # print(correction)
    histories = [(int)(record) for record in log.readline()[:-1] if record != ' ']
    # print(histories)
    print('Summary of list ' + (str)(listNo))
    correction = [correction[i] / histories[i] for i in range(len(correction))]
    for cnt, rate in enumerate(correction):
        print((str)(ENList[cnt][1][1:]) + ': ' + '{:.1%}'.format(rate))



listNo = ChooseList()
print('Loading...\n')
list = ReadList(listNo)
ENList = ENList(list)
CNList = CNList(list)
log = ReadLog(listNo, ENList)
TestByCN(listNo, ENList, CNList, log)
SumByEN(listNo, ENList, log)
log.close()
EndTest()
