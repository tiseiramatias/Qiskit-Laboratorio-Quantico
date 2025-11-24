import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

N = 30
data = np.random.randint(1, 100, N) # Datos desordenados

# Generador que realiza el Bubble Sort paso a paso
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr # Pausa y devuelve el estado actual

generator = bubble_sort(data.copy())

fig, ax = plt.subplots()
ax.set_title("Visualización: Bubble Sort")
bar_rects = ax.bar(range(len(data)), data, align="edge")
ax.set_xlim(0, N)
ax.set_ylim(0, 100)

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

def update_fig(data, rects, iteration):
    for rect, val in zip(rects, data):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"Iteraciones: {iteration[0]}")

ani = animation.FuncAnimation(fig, update_fig, fargs=(bar_rects, [0]),
                              frames=generator, interval=50,
                              repeat=False, save_count=500)
plt.show()
