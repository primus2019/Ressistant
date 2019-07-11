def showUsage():
    pass


def ReadList(listNumber):
    try:
        lists = [line for line in open(
            "list/List_" + (str)(listNumber) + ".md", encoding="utf8")]
    except FileNotFoundError:
        print('List ' + str(listNumber) + ' not found!')
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


def getENList(vol):
    return [[cnt + 1, word[0]] for cnt, word in enumerate(vol)]


def getCNList(vol):
    CNList = []
    cnt = -1
    for word in vol:
        cnt += 1
        CNList.append([cnt + 1])
        for mng in word[1:]:
            CNList[cnt].append(mng[0])
    # print(CNList)
    return CNList
