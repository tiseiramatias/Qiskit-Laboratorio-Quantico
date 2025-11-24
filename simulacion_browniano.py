import numpy as np
import matplotlib.pyplot as plt

# Configuración
num_particulas = 5
num_pasos = 1000

# Generar pasos aleatorios (dx, dy) distribuidos normalmente
dx = np.random.normal(0, 1, (num_particulas, num_pasos))
dy = np.random.normal(0, 1, (num_particulas, num_pasos))

# Acumular pasos para obtener posiciones (Camino aleatorio)
x = np.cumsum(dx, axis=1)
y = np.cumsum(dy, axis=1)

# Graficar
plt.figure(figsize=(8, 8))
for i in range(num_particulas):
    plt.plot(x[i], y[i], alpha=0.6, linewidth=1)
    plt.plot(x[i, -1], y[i, -1], 'ko') # Punto final

plt.title("Movimiento Browniano (Caminata Aleatoria)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
