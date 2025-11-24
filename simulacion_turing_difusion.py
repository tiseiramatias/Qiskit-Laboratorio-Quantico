import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros del modelo Gray-Scott
Da, Db = 0.16, 0.08
f, k = 0.055, 0.062 # Estos valores generan patrones interesantes
N = 100             # Tamaño de la cuadrícula
dt = 1.0
steps_per_frame = 10

# Inicialización
A = np.ones((N, N))
B = np.zeros((N, N))

# Perturbación inicial en el centro
r = 10
A[N//2-r:N//2+r, N//2-r:N//2+r] = 0.50
B[N//2-r:N//2+r, N//2-r:N//2+r] = 0.25

def laplacian(Z):
    # Cálculo discreto de la difusión
    return (np.roll(Z, 1, 0) + np.roll(Z, -1, 0) +
            np.roll(Z, 1, 1) + np.roll(Z, -1, 1) - 4 * Z)

fig, ax = plt.subplots()
img = ax.imshow(B, cmap='inferno', interpolation='bicubic')
ax.set_title("Reacción-Difusión (Patrones de Turing)")
ax.axis('off')

def update(frame):
    global A, B
    # Iterar varias veces por frame para acelerar la animación visual
    for _ in range(steps_per_frame):
        La = laplacian(A)
        Lb = laplacian(B)
        
        diff_A = (Da * La - A * B**2 + f * (1 - A)) * dt
        diff_B = (Db * Lb + A * B**2 - (k + f) * B) * dt
        
        A += diff_A
        B += diff_B
        
    img.set_data(B)
    return img,

ani = animation.FuncAnimation(fig, update, frames=200, interval=20)
plt.show()
