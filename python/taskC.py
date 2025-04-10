class Uzel:
    def __init__(self, znach):
        self.leviy = None
        self.praviy = None
        self.znach = znach

def set_znach(koren, znach):
    if koren is None:
        koren = Uzel(znach)
        #print('!')
    elif koren.znach > znach:
        koren.leviy = set_znach(koren.leviy, znach)
    elif koren.znach < znach:
        koren.praviy = set_znach(koren.praviy, znach)
    return koren

def leaves(koren):
    if koren != None:
        leaves(koren.leviy)
        if koren.leviy == None and koren.praviy == None:
            print(koren.znach, end=" ")
        leaves(koren.praviy)

n = int(input())
numbers = list(map(int, input().split()))

koren = None
for number in numbers:
    koren = set_znach(koren, number)
leaves(koren)



class Uzel:
    def __init__(self, znach):
        self.leviy = None
        self.praviy = None
        self.znach = znach

def set_znach(koren, znach):
    if koren is None:
        koren = Uzel(znach)
        #print('!')
    elif koren.znach < znach:
        koren.leviy = set_znach(koren.leviy, znach)
    return koren

def leaves(koren):
    if koren == None:
        leaves(koren.leviy)
        if koren.leviy == None and koren.praviy == None:
            print(koren.znach)
        leaves(koren.praviy)

n = int(input())
numbers = list(map(int, input().split()))

koren = None
for number in numbers:
    koren = set_znach(koren, number)
leaves(koren)