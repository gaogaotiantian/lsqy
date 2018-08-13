petData = \
[
#   patk, matk, li,  ling, licz, lingcz, patkzz, matmzz, level, xm
    [476, 397,  165, 165,  437,  310,    504,    403,    71,    {}]
]

class Pet:
    def __init__(self, attrList = None, **attrs):
        self.major = 'h'
        self.majorconst = 1.0/150
        if attrList == None:
            attrList = [0,0,0,0,0,0,0,0,0,{}]
        self.patk =   attrList[0] 
        self.matk =   attrList[1] 
        self.li =     attrList[2] 
        self.ling =   attrList[3] 
        self.licz =   attrList[4] 
        self.lingcz = attrList[5] 
        self.patkzz = attrList[6] 
        self.matkzz = attrList[7] 
        self.level =  attrList[8] 
        self.xm =     attrList[9] 

    def calcPatk(self):
        ret = 0
        for k,v in self.xm.items():
            if k == "patk":
                ret += v
                break
        ret += 30
        czconst = self.majorconst
        return ret + (1+self.patkzz*0.0004)*((czconst * self.licz) * self.level + self.li)

    def calcPSat(self):
        ret = 30
        for k,v in self.xm.items():
            if k == "patk":
                ret += v
                break
        czconst = self.majorconst
        return ((self.patk - ret) / (1+self.patkzz*0.0004) - self.li) / ((self.level-1) * self.licz * czconst)

    def calcMatk(self):
        ret = 0
        for k,v in self.xm.items():
            if k == "matk":
                ret += v
                break
        ret += 30
        czconst = self.majorconst
        return ret + (1+self.matkzz*0.0004)*((czconst * self.lingcz) * self.level + self.ling)

    def calcMSat(self):
        ret = 30
        for k,v in self.xm.items():
            if k == "matk":
                ret += v
                break
        czconst = self.majorconst
        return ((self.matk - ret) / (1+self.matkzz*0.0004) - self.ling) / ((self.level-1) * self.lingcz * czconst)


class JL(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 357
        self.matk = 1518
        self.li = 161
        self.ling = 501
        self.licz = 249
        self.lingcz = 935
        self.patkzz = 446
        self.matkzz = 1296
        self.xm = {"matk":130+69*1.2}
        self.level = 69

class JL2(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 244
        self.matk = 1197
        self.li = 133
        self.ling = 403
        self.licz = 138
        self.lingcz = 848
        self.patkzz = 388
        self.matkzz = 1215
        self.xm = {"matk":130+69*1.2}
        self.level = 55

class HS(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 299
        self.matk = 1730
        self.li = 173
        self.ling = 543
        self.licz = 133
        self.lingcz = 1066
        self.patkzz = 238
        self.matkzz = 1203
        self.xm = {"matk":107+75*2}
        self.level = 75


class Tww(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 274
        self.matk = 481
        self.li = 133
        self.ling = 133
        self.licz = 192
        self.lingcz = 425
        self.patkzz = 504
        self.matkzz = 1008
        self.xm = {"matk":78}
        self.level = 55

class Tww2(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 297
        self.matk = 984
        self.li = 143
        self.ling = 438
        self.licz = 200
        self.lingcz = 546
        self.patkzz = 504
        self.matkzz = 1008
        self.xm = {"matk":78}
        self.level = 60

class LL(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'h'
        self.patk = 307
        self.matk = 404
        self.li = 153
        self.ling = 153
        self.licz = 202
        self.lingcz = 371
        self.patkzz = 316
        self.matkzz = 468
        self.level = 65

class Hgs(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'p'
        self.patk = 468
        self.matk = 231
        self.li = 111
        self.ling = 111
        self.licz = 647
        self.lingcz = 195
        self.patkzz = 984
        self.matkzz = 492
        self.xm = {"patk":56}
        self.level = 44

class MC(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'p'
        self.patk = 341
        self.matk = 150
        self.li = 67
        self.ling = 67
        self.licz = 679
        self.lingcz = 238
        self.patkzz = 812
        self.matkzz = 451
        self.xm = {"patk":103}
        self.level = 22

class HL(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.major = 'm'
        self.patk = 186
        self.matk = 327
        self.li = 97
        self.ling = 97
        self.licz = 145
        self.lingcz = 419
        self.patkzz = 420
        self.matkzz = 840
        self.xm = {"matk":60}
        self.level = 37


class QM(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.patk = 468
        self.matk = 231
        self.li = 111
        self.ling = 111
        self.licz = 647
        self.lingcz = 195
        self.patkzz = 984
        self.matkzz = 492
        self.level = 44
lst =  [JL(), JL2(), LL(), HS(), Tww2(), Tww(), Hgs(), MC()]

for p in petData:
    lst.append(Pet(p))
lst.sort(key = lambda x:x.level, reverse=True)
for t in lst:
    print("Level: {}({}), Matk Diff: {:.3f}, Patk Diff: {:.3f} | Psat: {:.4f}({}), Msat : {:.4f}({})".format(t.level, t.major, t.calcMatk() - t.matk, t.calcPatk() - t.patk, t.calcPSat(), t.licz, t.calcMSat(), t.lingcz))
