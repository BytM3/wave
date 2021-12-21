import math
import numpy as np
import matplotlib.pyplot as plt 

t= np.arange(0, 10, 0.01);  
pi= math.pi


def getwave():
    AM=float(input("Donner amplitude:"))
    FM=float(input("Donner la frequence:"))
    return AM,FM

def affich(wave):
    plt.figure()
    plt.plot(t, wave)
    plt.title('Modulation')
    plt.xlabel('Temp')
    plt.ylabel('Amplitude ')
    plt.grid(True, which='both',color = 'green', linestyle = '--', linewidth = 0.5)
    plt.axhline(y=0, color='k')
    plt.show()

def mod_sp(ams,fms,amp,fmp,k=1):
    s=(k*amp*ams*np.cos(2*pi*fms*t))*np.cos(2*pi*fmp*t)
    return s

def mod_ap(ams,fms,amp,fmp,k=1):
    s=amp*(1+k*ams*np.cos(2*pi*fms*t))*np.cos(2*pi*fmp*t)
    return s


"""
main program
"""

print("Representation de la figure Mdulation [AM]")
print()
print("[1]-Modulation d'amplitude à double bande sans porteuse (DBSP)")
print("[2]-Modulation d'amplitude à double bande avec porteuse (DBAP)")
ch=int(input("\nvotre choix: "))
while True:
    if ch == 1:
        print("Signal: ")
        ams,fms=getwave()
        print("Porteuse: ")
        amp,fmp=getwave()
        affich(mod_sp(ams,fms,amp,fmp,k=1))
        break
    elif ch == 2:
        print("Signal: ",end="")
        ams,fms=getwave()
        print("Porteuse: ",end="")
        amp,fmp=getwave()
        affich(mod_ap(ams,fms,amp,fmp,k=1))
        break  
    else:
        print("ERREUR")
        break      

