#This code plot a Bifurcation Diagram from Henon Map for each value a with a 
#constant

#Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Set a constants values and initial conditions
x0=0
xi=0
b=-0.39999
a=1.4
it = 100 #Iterations
e=500 #Evoltion: How much values x its calculated for r
t=200 #Transient: How much iterations whill the function do before returning xn


#Functions
def Hen(x,xi,a,b): 
    return 1-a*(x**2)+b*xi
def transi(xn,xni,a,b):
    for i in range(int(t)):
        xk=np.copy(xn)
        xn=Hen(xn,xni,a,b)
        xni=xk
    return xn,xni

#Lists
xn=[x0]
xni=[xi]
xn1=[Hen(xn[-1],xni[-1],a,b)]
xni=np.copy(xn)
xn.append(xn1[-1])
xn1.append(xn1[-1])
B=np.linspace(-0.39999,0.3,500) #Cria um conjunto no intervalo [1,4], com 200 elementos
bt=[] 
xt=[]


#This "for" calculated the values x in Henon map for the "e" evolutions after 
#transient "t", in function of all elements in the set A

for i in range(len(B)):
    x = transi(x0,xi,a,B[i])[0] 
    xi=transi(x0,xi,a,B[i])[1] 
    for j in range(e):
        xk=np.copy(x)
        x = Hen(x,xi,a,B[i])
        xi=xk
        bt.append(B[i])
        xt.append(x)

#data=pd.DataFrame({'Lista b':bt,'Lista x':xt})
#print(data)

#Settings to plot a Graphic
fig = plt.figure(figsize = (18,12))
plt.style.use('dark_background')
plt.title("Mapa de Hénon em função da variável B")
plt.plot(bt,xt,'.w',alpha=0.5,markersize=0.1)
plt.show()