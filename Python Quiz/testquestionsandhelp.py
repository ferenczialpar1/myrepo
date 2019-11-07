import math
import csv
import random
import time
import easygui

###MODULOK###
import resultclass
import questionclass
import resultstablereadprint
import helpoptions
import readdatafromcsv

###FÜGGVÉNYEK###
def menu():
    selectmenu = easygui.buttonbox("Legyen Ön is milliomos",image = "1-kép.png",choices = ['\n Játék indítása\n', '\n Dicsőségtábla \n', '\n Kilépés\n'])
    while True:
        if selectmenu=='\n Játék indítása\n':
            test()
            break
        elif selectmenu=='\n Dicsőségtábla \n':
            resultstablereadprint.resultlist()
            menu()
            break
        elif selectmenu=='\n Kilépés\n':
            exit()


def test():
    easylist=[1,2,3,4,5]
    medlist=[6,7,8,9,10]
    quesionlist=["1","2","3","4","6","7","8","9","11","12","13"]
    
    lista1=readdatafromcsv.readdata()

    previousquestions=[""]
    hpda=["Segítségek:","Telefonos: 1-es gomb","Felezés: 2-es gomb","Közönség: 3-as gomb"]
   
    money=[0]   
    for i in range(0,16):
        if i<11:
            while True:
                x=random.randint(0,len(lista1))
                while quesionlist.count(str(lista1[x].diff)) == 0 and previousquestions.count(lista1[x].question) == 0:
                    x=random.randint(0,len(lista1))
                questions(lista1[x].question,lista1[x].a,lista1[x].b,lista1[x].c,lista1[x].d,lista1[x].correct,i,hpda,money)
                previousquestions.append(lista1[x].question)
                break
        elif i>=11:
            while True:
                y=random.randint(0,len(lista1))
                while quesionlist.count(str(lista1[y].diff)) == 1 and previousquestions.count(lista1[y].question) == 0:
                    y=random.randint(0,len(lista1))
                questions(lista1[y].question,lista1[y].a,lista1[y].b,lista1[y].c,lista1[y].d,lista1[y].correct,i,hpda,money)
                previousquestions.append(lista1[y].question)
                break
                
                

def questions(qstion,optiona,optionb,optionc,optiond,optioncorrect,ii,hpdd,moneyy):
    start = time.time()
    selectanss="Z"
    selectans = easygui.choicebox(qstion,title=("Eddigi nyereménye: {} Ft".format(moneyy[0])),choices = [str(optiona), str(optionb), str(optionc),str(optiond)," Segítséget szeretnék kérni!"] )
    if selectans is None:
        menu()
    ans=selectans[0]
    if ans==" ":
        support=help(qstion,optiona,optionb,optionc,optiond,optioncorrect,hpdd)
        selectanss = easygui.choicebox("{} A lehetséges helyes válaszok: {}".format(qstion,support),choices = [str(optiona), str(optionb), str(optionc),str(optiond)] )

    if str(ans)==str(optioncorrect) or str(selectanss[0])==str(optioncorrect):
        moneyy[0]+=1000
        if ii==15:
            stp=time.time()
            ido=stp-start
            nev=easygui.enterbox(msg = "Gratulálunk megnyerte a főnyereményt! A nyereménye:{} Idő {:00.5}mp // Kérem adja meg a nevét a mentéshez:".format(moneyy[0],ido),title=("Eddigi nyereménye: {} Ft".format(moneyy[0])), default='', image = "2-jtk.png",)
            resultstablereadprint.resultsappend(nev,moneyy[0],ido)
            menu()
    else:
        stp=time.time()
        ido=stp-start
        nev=easygui.enterbox(msg = "Helytelen!A helyes válasz:{} A nyereménye:{} Idő {:00.5}mp // Kérem adja meg a nevét a mentéshez:".format(optioncorrect,moneyy[0],ido),title=("Eddigi nyereménye: {} Ft".format(moneyy[0])), default='', image = "2-jtk.png",)
        resultstablereadprint.resultsappend(nev,moneyy[0],ido)
        menu()
        
                  

def help(kérd,a,b,c,d,hely,hpd):
    if(len(hpd))==4:
        selectmenu = easygui.buttonbox("Legyen Ön is milliomos",image = "2-jtk.png",title=hpd[0],choices = [hpd[1],hpd[2],hpd[3]])
    elif(len(hpd))==3:
        selectmenu = easygui.buttonbox("Legyen Ön is milliomos",image = "2-jtk.png",title=hpd[0],choices = [hpd[1],hpd[2]])
    elif(len(hpd))==2:
        selectmenu = easygui.buttonbox("Legyen Ön is milliomos",image = "2-jtk.png",title=hpd[0],choices = [hpd[1]])
    elif(len(hpd))==1:
        return "Ön már elhasználta a segítségeit"
        
    while True:
        if selectmenu=="Telefonos: 1-es gomb":
            phone=helpoptions.phone(hely)
            xx=hpd.index("Telefonos: 1-es gomb")
            del hpd[xx]
            return phone
        
        elif selectmenu=="Felezés: 2-es gomb":
            twooption=helpoptions.half(hely)
            xx=hpd.index("Felezés: 2-es gomb")
            del hpd[xx]
            return twooption

        elif selectmenu=="Közönség: 3-as gomb":
            spectrs=helpoptions.spectators(hely)
            xx=hpd.index("Közönség: 3-as gomb")
            del hpd[xx]
            return spectrs


def main():
    menu()
main()



