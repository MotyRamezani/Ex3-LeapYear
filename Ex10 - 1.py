import numpy as np
import matplotlib.pyplot as plt
x = 6
pow(x,2)
#print(pow(x,2))
theta = 30
np.sin(30)
print("Sin(",theta,") = ",np.sin(30))
np.cos(30)
print("Cos(",theta,") = ",np.cos(30))
meshPoints = np.linspace(-1,1,500)
#print(meshPoints)
meshPoints[53]
print("53th element of meshPoints= ",meshPoints[53])
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()