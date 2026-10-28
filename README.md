# Práctica 8: Algoritmos de Deutsch y Deutsch-Jozsa

Implementación en Python (PyQuil) y simulación mediante QVM en Docker de los algoritmos de decisión de promesas (Deutsch y Deutsch-Jozsa), comparando la eficiencia de consultas entre los enfoques clásicos y cuánticos[cite: 3].

## Estructura del Proyecto
* **`parte_1_clasico.py`**: Versión clásica del algoritmo de Deutsch ($n=1$)[cite: 3].
* **`parte_1_cuantico.py`**: Versión cuántica del algoritmo de Deutsch ($n=1$) mediante *phase kickback*[cite: 3, 5, 6].
* **`parte_2_clasico.py`**: Versión clásica del algoritmo de Deutsch-Jozsa ($n=3$) evaluando el peor caso de consultas[cite: 3, 5, 8, 9].
* **`parte_2_cuantico.py`**: Versión cuántica del algoritmo de Deutsch-Jozsa ($n=3$) utilizando codificación matricial (`DefGate`) e interferencia[cite: 3, 7, 8, 9].

## Requisitos y Entorno
* Python 3.12[cite: 3]
* Docker (Contenedor QVM ejecutándose en el puerto 5000)[cite: 3, 6, 10]
* PyQuil, NumPy