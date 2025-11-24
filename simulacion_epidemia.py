import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# -- Configuración del Modelo --
N = 1000      # Población total
I0 = 1        # Infectados iniciales
R0 = 0        # Recuperados iniciales
S0 = N - I0 - R0 # Susceptibles iniciales

# Tasas de contacto (beta) y recuperación (gamma)
beta = 0.3    # Probabilidad de contagio
gamma = 1./10 # Recuperación en 10 días

t = np.linspace(0, 160, 160) # Tiempo en días

# Ecuaciones diferenciales del modelo SIR
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Vector inicial
y0 = S0, I0, R0

# Integración (simulación)
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptibles')
plt.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infectados')
plt.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recuperados')
plt.xlabel('Días')
plt.ylabel('Número de personas')
plt.title('Simulación de Epidemia (Modelo SIR)')
plt.legend()
plt.grid(True)
plt.show()
