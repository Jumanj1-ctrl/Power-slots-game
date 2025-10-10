import random
#=========================================================================================================================
#Class for reels
#=========================================================================================================================

class Reel:
    def __init__(self):
        self.sym = ['$','£','@','#','*']
        self.list = []
    def easy(self):
        for i in range(0, len(self.sym)):
            if i < 2:
                for x in range(0,6):
                    self.list.append(self.sym[i])
            else:
                for x in range(0,1):
                    self.list.append(self.sym[i])
        return self.list

r1 = Reel()
r2 = Reel()
r3 = Reel()
m = ''


R1 = r1.easy()[random.randint(0,len(r1.easy())-1)]
R2 = r2.easy()[random.randint(0,len(r2.easy())-1)]
R3 = r3.easy()[random.randint(0,len(r3.easy())-1)]
menu = False
if m != '':
    menu = True
while menu == False:
    print(R1, R2, R3)
    if R1 == R2 and R2 == R3:
        print('YOU WIN')
        m = input('press Enter : ')
        if m != '':
            menu = True
        else:
            R1 = r1.easy()[random.randint(0,len(r1.easy())-1)]
            R2 = r2.easy()[random.randint(0,len(r2.easy())-1)]
            R3 = r3.easy()[random.randint(0,len(r3.easy())-1)]
    else:
        m = input('press Enter : ')
        if m != '':
            menu = True
        else:
            R1 = r1.easy()[random.randint(0,len(r1.easy())-1)]
            R2 = r2.easy()[random.randint(0,len(r2.easy())-1)]
            R3 = r3.easy()[random.randint(0,len(r3.easy())-1)]
    




        