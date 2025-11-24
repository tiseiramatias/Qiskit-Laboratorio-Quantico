import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración
N = 100 # Tamaño de la cuadrícula (100x100)
ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """Devuelve una cuadrícula de NxN con valores aleatorios"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(frameNum, img, grid, N):
    # Copiamos la cuadrícula para calcular el siguiente estado
    newGrid = grid.copy()
    
    for i in range(N):
        for j in range(N):
            # Cálculo de la suma de los 8 vecinos (usando condiciones de frontera toroidal)
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            
            # Reglas del Juego de la Vida de Conway
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
                    
    # Actualizamos los datos de la imagen
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Inicialización
grid = randomGrid(N)
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=10, interval=50, save_count=50)

plt.title("Juego de la Vida de Conway")
plt.show()
