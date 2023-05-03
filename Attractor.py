#Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#This code plot a attractor from Henon Map

#Set a constants values
a=1.4
b=0.3
it=100000 #iterations

#Henon Map
def mhen(x,y): #equation recurrence
    xn=1-a*x**2+y
    yn=b*x
    return xn,yn

#Create lists and initial conditions
xt=np.zeros(it+1)
yt=np.zeros(it+1)
xt[0],yt[0]=0.5,0.2

#Calculates each value xt[i],yt[i] from i=0 to it
for i in range(it): 
    xk,yk=mhen(xt[i],yt[i])
    xt[i+1]=xk
    yt[i+1]=yk

#data=pd.DataFrame({'Eixo x':xt,'Eixo y':yt})
#print(data)



#Settings to plot a Graphic
plt.style.use('dark_background')
plt.figure(figsize = (18,12))
plt.plot(xt,yt,',',color='white',markersize=0.3)
plt.xlim([-1.5,1.5])
plt.xlabel(r'$x_n$')
plt.ylabel(r'$y_n$')
plt.show()


#Zooms to see a fractal dimensional

'''
#Original Image
plt.figure(figsize = (18,12))
plt.plot(xt,yt,',',color='black',markersize=0.3)
plt.plot([0.4,0.4,0.6,0.6,0.4],[0.1,0.3,0.3,0.1,0.1],color='black',markersize=0.3)
plt.xlim([-1.5,1.5])
plt.xlabel(r'$x_n$')
plt.ylabel(r'$y_n$')
plt.show()

#Zoom 1
plt.figure(figsize = (18,12))
plt.plot(xt,yt,',',color='black',markersize=0.3)
plt.plot([0.425,0.425,0.525,0.525,0.425],[0.125,0.225,0.225,0.125,0.125],color='black',markersize=0.3)
plt.ylim([0.15,0.3])
plt.xlim([0.4,0.6])
plt.xlabel(r'$x_n$')
plt.ylabel(r'$y_n$')
plt.show()

#Zoom 2
plt.figure(figsize = (18,12))
plt.plot(xt,yt,',',color='black',markersize=0.3)
plt.plot([0.46,0.46,0.48,0.48,0.46],[0.20,0.22,0.22,0.20,0.20],color='black',markersize=0.3)
plt.ylim([0.125,0.225])
plt.xlim([0.425,0.525])
plt.xlabel(r'$x_n$')
plt.ylabel(r'$y_n$')
plt.show()

#Zoom 3
plt.figure(figsize = (18,12))
plt.plot(xt,yt,',',color='black',markersize=0.3)
plt.ylim([0.20,0.22])
plt.xlim([0.46,0.48])
plt.xlabel(r'$x_n$')
plt.ylabel(r'$y_n$')
plt.show()

#plt.style.use('dark_background')
'''