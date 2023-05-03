#This code plot a Bifurcation Diagram from Henon Map for each value a with b 
#constant

#Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Set a constants values and initial conditions
x0=-1
xi=-1
b=0.3
it = 100 #Iterations
e=500 #Evoltion: How much values x its calculated for r
t=200 #Transient: How much iterations whill the function do before returning xn


#Functions
def Hen(x,xi,a,b): #Is a equation recurrence in two steps
    return 1-a*(x**2)+b*xi
def transi(xn,xni,a,b): #This function calculate value of xn each r
    for i in range(int(t)):
        xk=np.copy(xn) #Save a copy of xn in xk
        xn=Hen(xn,xni,a,b) #xn=x_{i} and xni=x_{i-1}
        xni=xk #Now x_{i-1}=xk
    return xn,xni #Return news values from xn=x_{i} and xni=x_{i-1}

#Lists
xn=[x0]#xn=x_{i+1}
xni=[xi]#xni=x_{i-1}
xn1=[Hen(xn[0],xni[0],1.4,b)]#Calculate the new xn1=x_n{i+1}
xni=np.copy(xn)#Now xni=x_{i-1} is a copy from xn=x_{i+1}
xn.append(xn1[0])#xn is the xn1[0]
xn1.append(xn1[0])#Duplicate value xn1[0] in list xn1
A=np.linspace(0,1.4,500) #Create a set in the range [1,4], with 200 elements
at=[] #Receive each value from A
xt=[] #Receive each x_{i+1} calculated on each element A 


#This "for" calculated the values x in Henon map for the "e" evolutions after 
#transient "t", in function of all elements in the set A

for i in range(len(A)): 
    x = transi(x0,xi,A[i],b)[0] #x=x_{i+1}
    xi=transi(x0,xi,A[i],b)[1] #x=x_i
    for j in range(e):
        xk=np.copy(x)
        x = Hen(x,xi,A[i],b)
        xi=xk
        at.append(A[i])
        xt.append(x)

#data=pd.DataFrame({'Lista a':at,'Lista x':xt})
#print(data)


#Settings to plot a Graphic
fig = plt.figure(figsize = (18,12))
plt.style.use('dark_background')
plt.title("Mapa de Hénon em função da variável A")
plt.plot(at,xt,'.w',alpha=0.8,markersize=0.3)
plt.show()