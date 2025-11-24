import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth, ax):
    if depth == 0:
        return

    # Calcular punto final de la rama
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    # Dibujar línea (más fina cuanto más profunda)
    ax.plot([x, x_end], [y, y_end], 'brown', lw=depth*0.5)

    # Recursividad: Dos ramas nuevas
    new_length = length * 0.75
    draw_branch(x_end, y_end, angle - 20, new_length, depth - 1, ax) # Rama izquierda
    draw_branch(x_end, y_end, angle + 20, new_length, depth - 1, ax) # Rama derecha

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Árbol Fractal (Recursividad)")

# Iniciar el árbol desde abajo
draw_branch(0, 0, 90, 100, 10, ax)

plt.show()
