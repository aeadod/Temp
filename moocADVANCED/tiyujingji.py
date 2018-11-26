import random



def printinfo():
    print('jie shao xin xi')
def getinput():
    a=eval(input('(0~1):'))
    b=eval(input("(0~1):"))
    n=eval(input("changci:"))
    return a,b,n
def gameover(a,b):
    return a==15 or b==15
def simone(proba,probb):
    scorea,scoreb=0,0
    serving='A'
    
    while not gameover(scorea,scoreb):
        if serving =='A':
            if random.random()<proba:
                scorea+=1
            else :
                serving='B'
        else :
            if random.random()<probb:
                scoreb+=1
            else :
                serving='A'
    return scorea,scoreb
def simngames(n,proba,probb):
    winsa,winsb=0,0
    for i in range(n):
        scorea,scoreb=simone(proba,probb)
        if scorea>scoreb:
            winsa+=1
        else:
            winsb+=1
    return winsa,winsb

    
    


def printsummary(winsa,winsb):
    n=winsa+winsb
    print("A{}.{:0.1%}".format(winsa,winsa/n))
    print("B{}.{:0.1%}".format(winsb,winsb/n))
def main():
    printinfo()
    proba,probb,n=getinput()
    winsa,winsb = simngames(n,proba,probb)
    printsummary(winsa,winsb)
    
main()
