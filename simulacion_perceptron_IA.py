import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generar datos separables linealmente
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = np.array([0] * 20 + [1] * 20) # Etiquetas 0 y 1

# Inicializar pesos (w) y sesgo (b) aleatorios
w = np.random.rand(2)
b = np.random.rand(1)
learning_rate = 0.01

fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=Y, cmap='bwr', edgecolors='k')
line, = ax.plot([], [], 'k-', lw=2)
ax.set_title("Entrenamiento del Perceptrón")

# Función de activación (Escalón)
def activation(z):
    return 1 if z >= 0 else 0

def train_step(frame):
    global w, b
    # Elegir un punto aleatorio para entrenar
    idx = np.random.randint(0, len(Y))
    x_sample, y_sample = X[idx], Y[idx]
    
    # Predicción
    prediction = activation(np.dot(w, x_sample) + b)
    
    # Regla de actualización del Perceptrón
    error = y_sample - prediction
    w += learning_rate * error * x_sample
    b += learning_rate * error

    # Calcular línea de decisión (w1*x + w2*y + b = 0) => y = -(w1*x + b)/w2
    x_vals = np.array([-4, 4])
    y_vals = -(w[0] * x_vals + b) / w[1]
    
    line.set_data(x_vals, y_vals)
    return line,

ani = animation.FuncAnimation(fig, train_step, frames=100, interval=100, blit=True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
