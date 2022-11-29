import math
import numpy as np

# Eingabeparameter:

mu = 0.5 # Reibungszahl je nach Material (~0,5 vgl. Tabelle 16.1 RoloffMatek)
beta1 = 180 # Grad Umschlingungsbogen
Ka = 1 # nach Tabelle 3-5
Tnenn = 1 # Nm Nenndrehmoment
d = 0.12 # m Scheibendurchmesser
m2 = 5.5 # kg/m Masse pro Meter
l = 0.46 # m Trumlänge / Achsabstand
b = 0.05 # m Riemenbreite


# Ausgabeparameter:

Ft = (Ka*Tnenn)/(d/2) # Umfangskraft
print('Ft =',Ft,'[N]')

m = np.exp((mu*np.pi*beta1)/180) # Trumkraftverhaeltnis
print('m =',m)

Fw = Ft*math.sqrt(((m**2)+1-2*m*math.cos(beta1*(180/math.pi)))/(m-1)) # Wellenbelastung/Vorspannkraft
print('Fw =',Fw,'[N]')

m3 = l*b*m2
print('m3',m3,'[kg]')

f = math.sqrt((Fw/(4*m3*l*l)))
print('f =',f,'[Hz]')