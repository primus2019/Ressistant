import os


def ReadLog(listNo, ENList):
    fileName = 'log/List_' + (str)(listNo) + '.log'
    if not os.path.isdir('log'):
        os.mkdir('log')
    if not os.path.isfile(fileName):
        with open(fileName, 'a+') as log:
            for word in ENList:
                log.write((str)(0) + ' ')
            log.write('\n')
            for word in ENList:
                log.write((str)(0) + ' ')
    return open(fileName, 'a+')


def SumByEN(listNo, ENList, log):
    log.seek(0, 0)
    correction = [(int)(record)
                  for record in log.readline()[:-1] if record != ' ']
    # print(correction)
    histories = [(int)(record)
                 for record in log.readline()[:-1] if record != ' ']
    # print(histories)
    print('Summary of list ' + (str)(listNo))
    correction = [correction[i] / histories[i] for i in range(len(correction))]
    for cnt, rate in enumerate(correction):
        print((str)(ENList[cnt][1][1:]) + ': ' + '{:.1%}'.format(rate))
