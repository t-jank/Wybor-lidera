import random
import math
import numpy as np
import matplotlib.pyplot as plt


########### zadanie 1 ############

jj=random.randint(1,9000)
print("u =",jj)

def scenariusz2(n): # znana liczba wezlow
    i=0 # i - nr slotu
    p=1/n
    sloty=[]
    sloty.append('N')
    suma=0
    sygnaly = []
    for z in range(0,n):
        sygnaly.append(-1)
    
    while sloty[i]!='S':
        i+=1
        for j in range(0,n): # nadawanie sygnalow przez wezly w danym slocie
            x = random.uniform(0,10000)
            if(x<=(10000*p)):
                sygnaly[j]=1
            else:
                sygnaly[j]=0
        for k in range(0,n):
            suma += sygnaly[k]
        if(0==suma):
            sloty.append('N')
        elif(1==suma):
            sloty.append('S')
        elif(suma>=2):
            sloty.append('C')
        suma=0

    return i


def scenariusz3(u,n): # znane gorne ograniczenie liczby wezlow
    i=0 # i - nr slotu
    p=[]
    b=0
    m = int(math.ceil(math.log(u,2)))+1
  #  print("m =",m)
    sloty=[]
    sloty.append('N')
    suma=0
    sygnaly = []
    for a in range(1,m+1):
        p.append(1/(2**a))
    for z in range(0,n):
        sygnaly.append(-1)
    
    while sloty[i]!='S':
        i+=1
        for j in range(0,n): # nadawanie sygnalow przez wezly w danym slocie
            x = random.uniform(0,10000)
            if(x<=(10000*p[b])):
                sygnaly[j]=1
            else:
                sygnaly[j]=0
        for k in range(0,n):
            suma += sygnaly[k]
        if(0==suma):
            sloty.append('N')
        elif(1==suma):
            sloty.append('S')
        elif(suma>=2):
            sloty.append('C')
        suma=0
        b+=1
        if(b>=len(p)):
            b=0

    return i



########### zadanie 2 ############
   
def histogramsc2():
    lslotow=[]
    for rr in range(1,21):
        lslotow.append(0)
    L=np.arange(1,21,1)

    for hh in range(0,1000):
        jj=random.randint(1,9000)
        ll=scenariusz2(jj)
        if(ll<21):
            lslotow[ll-1]+=1
            
    y_pos = np.arange(len(lslotow))
    plt.bar(y_pos, lslotow)
    plt.xticks(y_pos, L)
    plt.xlabel('L - liczba slotow do wystapienia SINGLE')
    plt.ylabel('Liczba przypadkow')
    plt.title('Histogram')
    plt.show()

def histogramsc3(lwezlow): #lwezlow={2,'u/2','u'}
    lslotow=[]
    for tt in range(1,51):
        lslotow.append(0)
    L=np.arange(1,51,1)

    for hh in range(0,1000):
        if(lwezlow==2):
            ll=scenariusz3(jj,2)
        elif(lwezlow=='u/2'):
            ll=scenariusz3(jj,int(jj/2))
        elif(lwezlow=='u'):
            ll=scenariusz3(jj,jj)
        if(ll<51):
            lslotow[ll-1]+=1
    y_pos = np.arange(len(lslotow))
    plt.bar(y_pos, lslotow)
  #  plt.xticks(y_pos, L)
    plt.xlabel('L - liczba slotow do wystapienia SINGLE')
    plt.ylabel('Liczba przypadkow')
    plt.title('Histogram')
    plt.show()



########### zadanie 3 ############

def EVAR():
    suma=0
    sumav=0
    L=[]
    for aa in range(0,1000):
        bb=random.randint(1,9000)
        cc=scenariusz2(bb)
        L.append(cc)
        suma+=cc
    E=suma/1000
    for o in range(0,1000):
        sumav+=(L[o]-E)**2
    Var=sumav/999
    print('E[L] =',E,';  e =',math.e,'\nVar[L] =',Var)



########### zadanie 4 ############

def twierdzenielambda():
    lsukcesow=0
    uu=random.randint(1,500)
    print("\nu =",uu,';  lambda = 0.579')
    L=int(math.ceil(math.log(uu,2)))
    for nn in range(2,uu+1):
        for qq in range(0,200):
            ww=scenariusz3(uu,nn)
            if(ww<=L):
                lsukcesow+=1
        Pr=lsukcesow/200
        if(Pr<0.6):
            print('n =',nn,';  Pr[SLN] =',Pr)
        lsukcesow=0



#histogramsc2()
#histogramsc3(2)
#histogramsc3('u/2')
#histogramsc3('u')
#EVAR()
twierdzenielambda()

