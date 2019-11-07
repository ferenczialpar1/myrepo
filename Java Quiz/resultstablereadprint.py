import resultclass
import easygui

def resultsappend(a,b,c):
    f=open("dicsoseg.txt","a")
    f.write("{};{};{:0.5}\n".format(a,b,c))
    f.close()

def resultlist():
    lista=[]
    hp=[]
    f = open("dicsoseg.txt", "rt")
    while True:
        sor=f.readline()
        if sor == "":
                break   
        darabok = sor.split(";")
        lista.append(resultclass.Resultclass(darabok[0],darabok[1],darabok[2]))
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-1):
            if int(lista[i].win)>int(lista[j].win):
                lista[i].name,lista[j].name,lista[i].win,lista[j].win,lista[i].time,lista[j].time=lista[j].name,lista[i].name,lista[j].win,lista[i].win,lista[j].time,lista[i].time
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-1):
            if int(lista[i].win)==int(lista[j].win) and float(lista[i].time)<=float(lista[j].time):
                lista[i].name,lista[j].name,lista[i].win,lista[j].win,lista[i].time,lista[j].time=lista[j].name,lista[i].name,lista[j].win,lista[i].win,lista[j].time,lista[i].time

    a="A 10 legjobb eredmény: \t \n"
    for i in range(len(lista[:10])):
        a=a+lista[i].name + "\t"
        a=a+lista[i].win + " Ft" + "\t"
        a=a+lista[i].time
    easygui.buttonbox(a, image="2-jtk.png", choices=["Vissza a főmenűbe"])


    
