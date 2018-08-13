import random

def Skill1(num):
    total = 0
    eList = [0] * num
    for i in range(4):
        atk = 1
        idx = random.randrange(0, num)
        for de in range(eList[idx]):
            atk *= 0.53
        eList[idx] += 1
        total += atk
    return total

def Skill2(num):
    if num <= 4:
        return num*1.15
    return 1.15*4

def Skill3(num):
    if num <= 6:
        return num*1.15
    return 1.15*6

def Skill4(num):
    if num == 1:
        return 10.4/3
    elif num == 2:
        return 10.4*2/3
    else:
        return 10.4


if __name__ == '__main__':
    testTime = 2000
    enemyNum = range(1, 11)
    res = []
    for e in enemyNum:
        total = [0,0,0,0]
        for t in range(testTime):
            total[0] += Skill1(e)
            total[1] += Skill2(e)
            total[2] += Skill3(e)
            total[3] += Skill4(e)
        avr = [t/testTime for t in total]
        res.append(avr)
    print res

