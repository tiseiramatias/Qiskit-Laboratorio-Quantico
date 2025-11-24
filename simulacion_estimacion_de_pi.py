import matplotlib.pyplot as plt
import numpy as np

# Número de puntos a simular
num_puntos = 5000

# Generar puntos aleatorios entre -1 y 1
x = np.random.uniform(-1, 1, num_puntos)
y = np.random.uniform(-1, 1, num_puntos)

# Calcular distancia al origen
distancia = np.sqrt(x**2 + y**2)

# Determinar si están dentro del círculo (radio 1)
dentro_circulo = distancia <= 1

# Estimación de Pi
puntos_dentro = np.sum(dentro_circulo)
pi_estimado = 4 * puntos_dentro / num_puntos

# Visualización
plt.figure(figsize=(6, 6))
plt.scatter(x[dentro_circulo], y[dentro_circulo], color='blue', s=1, label='Dentro')
plt.scatter(x[~dentro_circulo], y[~dentro_circulo], color='red', s=1, label='Fuera')
plt.title(f"Estimación de Pi (Monte Carlo)\nValor calculado: {pi_estimado}")
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()
