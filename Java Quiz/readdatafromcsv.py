import csv
import easygui
import questionclass

def readdata():
    easy=[]
    medium=[]
    hard=[]
    with open('kerdesek.csv') as csvfile:
        readcsv = csv.reader(csvfile,delimiter=';')
        for k in readcsv:
            k[2]="A:" + k[2]
            k[3]="B:" + k[3]
            k[4]="C:" + k[4]
            k[5]="D:" + k[5]
            if int(k[0]) <=5:
                easy.append(questionclass.Questions(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
            elif 10 >= int(k[0]) > 5:
                medium.append(questionclass.Questions(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
            elif 15 >= int(k[0]) > 10:
                hard.append(questionclass.Questions(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
                
    selectlevel = easygui.buttonbox("Kérem válasszon a játék indulása előtt az alábbi nehezségi szintek közül:",image = "2-jtk.png",choices = ["\n Könnyű \n", "\n Közepes \n", "\n Nehéz \n"] )
    while True:
        if selectlevel=="\n Könnyű \n":
            return easy
            break
        elif selectlevel=="\n Közepes \n":
            return medium
            break
        elif selectlevel=="\n Nehéz \n":
            return hard
            break
