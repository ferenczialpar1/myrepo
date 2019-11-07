import random
aidtable=[]
hpp=["A","B","C","D"]

def phone(crrect):
    global aidtable
    global hpp
    i=0
    while True:
            if str(hpp[i])!=crrect:
                aidtable.append(hpp[i])
            if len(aidtable)==3:
                break
            i+=1
    telefonos = ((aidtable[0].upper()) * 7 + (aidtable[1].upper()) * 6 + (aidtable[2].upper())* 7 + (crrect)* 80)
    phonex=random.choice(telefonos)
    del aidtable[:]
    return phonex
    
def half(crrect):
    global aidtable
    global hpp
    solution=[]
    while True:
            felezünk=random.choice(hpp)
            if str(felezünk)!=crrect:
                aidtable.extend([felezünk,crrect])
                break
    aidtable=sorted(aidtable)
    solution=aidtable[0],aidtable[1]
    del aidtable[:]
    return solution
    
def spectators(crrect):
    global aidtable
    global hpp
    solution1=[]
    x1=random.randint(75,90)
    y1=random.randint(0,100-x1)
    aidtable.append(y1)
    z1=random.randint(0,100-x1-y1)
    aidtable.append(z1)
    w1=100-x1-y1-z1
    aidtable.append(w1)
    for i in range(len(hpp)):
        if crrect==hpp[i]:
            solution1.append(hpp[i])
            solution1.append(x1)
            solution1.append(x1//5*"X")
        else:
            solution1.append(hpp[i])
            solution1.append(aidtable[0])
            solution1.append(aidtable[0]//5*"X")
            del aidtable[0]
    del aidtable[:]
    soolution=("\n {} válasz:{}% {} \n {} válasz:{}% {}\n {} válasz:{}% {}\n {} válasz:{}% {},".format(solution1[0],solution1[1],solution1[2],solution1[3],solution1[4],solution1[5],solution1[6],solution1[7],solution1[8],solution1[9],solution1[10],solution1[11]))
    return soolution


