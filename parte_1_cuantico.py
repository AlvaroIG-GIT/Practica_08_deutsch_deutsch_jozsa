from pyquil import Program, get_qc
from pyquil.gates import H, X, I, CNOT, MEASURE
import numpy as np


# Algoritmo de Deutsch - Versión Cuántica

# Oráculos cuánticos según la tabla de la práctica
def oraculo_cuantico_f0():
    return Program(I(1))

def oraculo_cuantico_f1():
    return Program(X(1))

def oraculo_cuantico_f2():
    return Program(CNOT(0, 1))

def oraculo_cuantico_f3():
    return Program([CNOT(0, 1), X(1)])

def deutsch_cuantico(oraculo_prog, shots=100):
    prog = Program()
    ro = prog.declare("ro", "BIT", 1)
    prog += [X(1), H(0), H(1)]
    prog += oraculo_prog
    prog += [H(0), MEASURE(0, ro[0])]
    prog.wrap_in_numshots_loop(shots)
    
    qc = get_qc("2q-qvm")
    bits = qc.run(prog).get_register_map().get("ro")
    return bits.flatten()

print("--- RESULTADOS VERSIÓN CUÁNTICA (Deutsch) ---")
oraculos = [
    ("f0", oraculo_cuantico_f0()), 
    ("f1", oraculo_cuantico_f1()), 
    ("f2", oraculo_cuantico_f2()), 
    ("f3", oraculo_cuantico_f3())
]

for nombre, oraculo in oraculos:
    bits = deutsch_cuantico(oraculo, shots=100)
    print(f"Función: {nombre} | Frecuencia de medir 1: {bits.mean():.2f}")

# COMENTARIO TÉCNICO: Los resultados experimentales muestran que para las funciones constantes (f0 y f1) 
# la frecuencia de medir 1 es exactamente 0.00, mientras que para las funciones balanceadas (f2 y f3) 
# la frecuencia es de 1.00. Esto se debe al efecto de phase kickback y a la interferencia cuántica 
# resultante de aplicar puertas Hadamard antes y después del oráculo, permitiendo resolver el problema 
# con una única consulta. Para la ejecución de la simulación fue necesario levantar previamente el 
# servidor QVM en el puerto 5000 mediante un contenedor de Docker.