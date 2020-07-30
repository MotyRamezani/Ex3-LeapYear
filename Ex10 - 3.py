import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,500)

f_x = np.exp(-x/10) * np.sin(np.pi*x)
plt.plot(x,f_x, label = "f(x)")

g_x = x * np.exp(-x/3)
plt.plot(x,g_x, label = "g(x)")

plt.title("f(x) & g(x) Diagram")
plt.xlabel("x-axes")
plt.ylabel("y-axes")
plt.legend()
plt.show()

################################################################

theta = np.linspace(0,2*np.pi,500)

l1 = [0.8,1.0,1.2]
for r_0 in l1:
    r = r_0 + np.cos(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x,y)

plt.title("Limacon Shape")
plt.xlabel("x-axes")
plt.ylabel("y-axes")
plt.legend(["Diagram with r-0 = 0.8","Diagram with r-0 = 1.0","Diagram with r-0 = 1.2"])
plt.show()