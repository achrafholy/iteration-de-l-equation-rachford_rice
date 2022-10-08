import numpy as np
import pandas as pd
import math as mt
#le vecter de la composition chimique
Zi = np.array([0.1, 0.2, 0.3, 0.4])
#le vecteur de taux de vaporisation
Ki = np.array([4.2, 1.75, 0.74, 0.34])
#la premiere valeur de ksi
ksi = np.array([0.121])
#la valeur de epsilon c-a-d la valeur de sortie doit etre inferieur a epsilon (presque 0)
epsilon = 0.0001
#le calcul de la premiére fonction ( la somme)
def RR(Zi, Ki,ksi):
    result = np.sum(Zi * (Ki-1) / (1 + ksi * (Ki - 1)))
    return result
#La valeur sortie
print(RR(Zi, Ki,ksi))
#le calcul de la premiére fonction dérivé ( la somme)
def RRD(Zi, Ki,ksi):
    result1 = np.sum(pow((Zi * (Ki-1)), 2) / pow((1 + ksi * (Ki - 1)), 2))
    return result1
print(RRD(Zi, Ki,ksi))
ref_value =RR(Zi, Ki,ksi)
print(ref_value)

#for ksi in range(0.1,1,0.001):
while ref_value >= epsilon:
       ksi = ksi - RR(Zi, Ki,ksi)/ RRD(Zi, Ki,ksi)
       ref_value=(RR(Zi, Ki,ksi))
print(ref_value,ksi)

