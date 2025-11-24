import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# Ecuaciones de Lorenz
def lorenz(state, t, sigma, rho, beta):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# Parámetros estándar de Lorenz
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Estado inicial
state0 = [1.0, 1.0, 1.0]

# Tiempo
t = np.arange(0.0, 40.0, 0.01)

# Resolver ecuaciones diferenciales
states = odeint(lorenz, state0, t, args=(sigma, rho, beta))

# Graficar
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2], lw=0.5, color='purple')

ax.set_title("Atractor de Lorenz (Teoría del Caos)")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
plt.show()
