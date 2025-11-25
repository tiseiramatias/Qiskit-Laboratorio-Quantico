# ⚛️ Simulaciones Científicas y Algoritmos con Python

Un repositorio de código abierto dedicado a explorar y visualizar diversos fenómenos científicos, algoritmos fundamentales y conceptos de Inteligencia Artificial mediante simulaciones escritas en Python.

##  Acerca del Proyecto

Este repositorio contiene una colección de *scripts* simples y educativos en Python diseñados para modelar y demostrar conceptos complejos de una manera accesible. Desde la física clásica hasta la teoría del caos y la implementación de algoritmos básicos de IA.

El objetivo es proporcionar un recurso práctico para estudiantes, educadores y cualquier persona interesada en comprender cómo funcionan estos sistemas a través de la programación.

###  Simulaciones Incluidas

| Archivo | Concepto Principal | Descripción Breve |
| :--- | :--- | :--- |
| `simulacion_browniano.py` | Movimiento Browniano | Simulación del movimiento aleatorio de partículas en un fluido. |
| `simulacion_caos.py` | Teoría del Caos | Demostración de sistemas sensibles a las condiciones iniciales (Ej: el Atractor de Lorenz o un péndulo doble). |
| `simulacion_epidemia.py` | Modelo SIR | Modelado de la propagación de enfermedades infecciosas (Susceptible, Infectado, Recuperado). |
| `simulacion_estimacion_de_pi.py` | Método de Monte Carlo | Estimación del valor de $\pi$ utilizando muestreo aleatorio. |
| `simulacion_fractal.py` | Geometría Fractal | Generación de estructuras auto-similares (Ej: Conjunto de Mandelbrot o Curva de Koch). |
| `simulacion_gravedad.py` | Simulación Física | Modelo simple de interacción gravitatoria entre cuerpos (Ej: Problema de los N-cuerpos). |
| `simulacion_perceptron_IA.py` | Inteligencia Artificial | Implementación básica del Perceptrón, la unidad neuronal más simple. |
| `simulacion_sorting.py` | Algoritmos de Ordenación | Visualización o implementación de algoritmos de ordenación (Ej: *Bubble Sort*, *Merge Sort*). |
| `simulacion_turing_difusion.py` | Reacción-Difusión | Simulación de patrones biológicos o químicos generados por ecuaciones de reacción-difusión (Patrones de Turing). |
| `simulacion_vida.py` | Autómatas Celulares | Implementación del Juego de la Vida de Conway. |

---

## 🛠️ Requisitos e Instalación

Para ejecutar estas simulaciones, necesitas tener **Python** instalado en tu sistema. Muchas de las simulaciones que incluyen visualización requieren librerías científicas y de trazado de gráficos.

### 📌 Requisitos Previos

Asegúrate de tener instalado **Python 3.x**.

Instalar dependencias:
Bash

    pip install numpy matplotlib

    (Asegúrate de incluir aquí cualquier otra dependencia necesaria, como scipy si se usa en alguna simulación.)

 Uso

Para ejecutar cualquier simulación, simplemente navega al directorio del proyecto y ejecuta el archivo deseado con Python:
Bash

python simulacion_epidemia.py

    Nota: Revisa el código de cada archivo para ver si se requieren argumentos de línea de comandos o si hay parámetros ajustables.

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar una simulación existente, añadir una nueva o corregir un bug, por favor sigue estos pasos:

    Haz un Fork del repositorio.

    Crea una nueva rama (git checkout -b feature/AmazingFeature).

    Comitéa tus cambios (git commit -m 'feat: añadir nueva simulación de [Concepto]').

    Empuja la rama (git push origin feature/AmazingFeature).

    Abre un Pull Request.
