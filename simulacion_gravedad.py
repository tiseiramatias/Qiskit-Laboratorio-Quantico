import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constantes
G = 1.0  # Constante gravitacional simplificada
M_star = 1000 # Masa de la estrella
dt = 0.05 # Paso de tiempo

# Estado inicial del planeta: [x, y, vx, vy]
# Posición (10, 0), Velocidad (0, 10) para órbita estable aprox
state = np.array([10.0, 0.0, 0.0, 8.0]) 

trajectory_x = []
trajectory_y = []

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
star, = ax.plot([0], [0], 'yo', markersize=15, label='Estrella') # Estrella fija
planet, = ax.plot([], [], 'bo', markersize=5, label='Planeta')
trail, = ax.plot([], [], 'b-', linewidth=0.5)

def update(frame):
    global state
    x, y, vx, vy = state
    
    # Calcular distancia al centro (r)
    r = np.sqrt(x**2 + y**2)
    
    # Fuerza de gravedad F = G*M/r^2
    # Aceleración a = F (masa planeta = 1) -> a = G*M / r^2
    # Descomposición vectorial: ax = a * (-x/r), ay = a * (-y/r)
    acc = G * M_star / (r**2)
    ax_acc = acc * (-x / r)
    ay_acc = acc * (-y / r)
    
    # Actualizar velocidad
    vx += ax_acc * dt
    vy += ay_acc * dt
    
    # Actualizar posición
    x += vx * dt
    y += vy * dt
    
    state = np.array([x, y, vx, vy])
    
    # Guardar trayectoria
    trajectory_x.append(x)
    trajectory_y.append(y)
    
    planet.set_data([x], [y])
    trail.set_data(trajectory_x, trajectory_y)
    return planet, trail

ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)
plt.title("Simulación Gravitacional (2 Cuerpos)")
plt.legend()
plt.grid()
plt.show()
