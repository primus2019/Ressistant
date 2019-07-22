import sys
sys.path.append('.')


import time
import random
import sys
import os
from ressistant.launch.Commands import hello
from ressistant.launch.Loadings import ReadList, getENList, getCNList
from ressistant.launch.Interactive import ChooseList, TestByCN, EndTest
from ressistant.launch.Loggings import SumByEN, ReadLog

def main(argv):
    if argv[1:] != []:
        hello(argv[1:])
        return
    listNo = ChooseList()
    print('Loading...\n')
    list = ReadList(listNo)
    enList = getENList(list)
    cnList = getCNList(list)
    log = ReadLog(listNo, enList)
    TestByCN(listNo, enList, cnList, log)
    SumByEN(listNo, enList, log)
    log.close()
    EndTest()


if __name__ == '__main__':
    main(sys.argv)
