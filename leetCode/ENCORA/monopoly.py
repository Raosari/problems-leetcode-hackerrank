import random
class Monopoly:
    def calculateCells(self,shots):
        mapBoard = {     
        'brown' : {1,3,4},
        'blueL' : {6,8,9},
        'jailTemp' : {10},
        'pink' : {11,13,14},
        'orange' : {16,18,19},
        'parking' : {20},
        'red' : {21,23,24},
        'yellow' : {26,27,29},
        'jail': {30},
        'green' : {31,32,34},
        'blueH' : {37,39},
        'goal' : {40},
        'stations' : {5,15,25,35},
        'lucky' : {2,7,17,22,33,36},
        'taxes' : {4,38},
        'companies' : {12,28},
        }

        def calculate(n,st):
            count_cells = {}
            adv = st
            for _ in range(n):
                d1 = random.randrange(1,7)
                d2 = random.randrange(1,7)
                adv +=  (d1 + d2)
                adv %= 40
                for k,v in mapBoard.items():
                    if adv in v:
                        count_cells[k] = count_cells.get(k,0) + 1
                        break
            return count_cells
        t1 = calculate(shots,0)
        t2 = calculate(shots//30000,10)
        finalMap = {}
        for k in t1:
            if k in t2:
                finalMap[k] = t1[k] + t2[k]
            else:
                finalMap[k] = t1[k]
            
            for k in t2:
                if k not in t1:
                    finalMap[k] = t2[k]
            orderedCells = sorted(finalMap.items(),key = lambda x:x[1],reverse=True)
        return orderedCells

test1 = Monopoly()
a = test1.calculateCells(100000)
print(a)