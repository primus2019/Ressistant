import time
import random
import sys
import os
import commands.Commands as Commands
import Loadings
import Interactive
import Loggings


def main(argv):
    if argv[1:] != []:
        Commands.hello(argv[1:])
        return
    listNo = Interactive.ChooseList()
    print('Loading...\n')
    list = Loadings.ReadList(listNo)
    enList = Loadings.getENList(list)
    cnList = Loadings.getCNList(list)
    log = Loggings.ReadLog(listNo, enList)
    Interactive.TestByCN(listNo, enList, cnList, log)
    Loggings.SumByEN(listNo, enList, log)
    log.close()
    Interactive.EndTest()


if __name__ == '__main__':
    main(sys.argv)
