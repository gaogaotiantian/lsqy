import random

def testOnce(num, slots, init = None):
    curr = [None]*slots
    if init != None:
        idx = 0
        for i in init:
            assert(i < num)
            curr[idx] = i
            idx += 1
    cost = [0]*num

    while True:
        for i in range(num):
            if i not in curr:
                curr[random.randrange(slots)] = i
                cost[i] += 1
                break
        else:
            break
    assert(set(curr) >= set(range(num)))
    return cost

def testAvr(num, slots, it = 50000, init = None):
    assert(num <= slots)
    result = [0]*num
    for i in range(it):
        r = testOnce(num, slots, init)
        result = [sum(x) for x in zip(result, r)]
    result = [float(r) / it for r in result]
    return result

if __name__ == '__main__':
    print(testAvr(8,8,init=[1,2,3,4,5,6,7]))
    print(testAvr(7,8,init=[]))

