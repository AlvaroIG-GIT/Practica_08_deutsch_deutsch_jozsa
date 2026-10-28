from collections import Counter
import numpy as np
from pyquil import Program, get_qc
from pyquil.gates import H, X, MEASURE
from pyquil.quil import DefGate


# Deutsch-Jozsa - Versión Cuántica

n = 3

f_todo_0 = lambda x: 0
f_todo_1 = lambda x: 1
f_b_msb   = lambda x: (x >> 2) & 1
f_b_lsb   = lambda x: x & 1
f_b_par   = lambda x: bin(x).count("1") % 2
f_b_tab   = lambda x: 1 if x in [1, 2, 3, 6] else 0

funciones_n3 = [
    ("Todo 0", f_todo_0), ("Todo 1", f_todo_1), ("b_msb", f_b_msb),
    ("b_lsb", f_b_lsb), ("b_par", f_b_par), ("b_tab", f_b_tab)
]

def construir_oraculo(f, n):
    U = np.zeros((2**(n + 1), 2**(n + 1)))
    for x in range(2**n):
        for y in (0, 1):
            U[(x << 1) | (y ^ f(x)), (x << 1) | y] = 1
    return DefGate("UF", U)

def dj_cuantico(f, n, shots=200):
    definicion = construir_oraculo(f, n)
    UF = definicion.get_constructor()
    prog = Program(definicion)
    ro = prog.declare("ro", "BIT", n)
    prog += X(n)
    prog += [H(q) for q in range(n + 1)]
    prog += UF(*range(n + 1))
    prog += [H(q) for q in range(n)]
    prog += [MEASURE(q, ro[q]) for q in range(n)]
    prog.wrap_in_numshots_loop(shots)
    
    qc = get_qc(f"{n + 1}q-qvm")
    bits = qc.run(prog).get_register_map().get("ro")
    return Counter("".join(map(str, fila)) for fila in bits)

def decidir(cuentas, n):
    return "constante" if cuentas["0" * n] == sum(cuentas.values()) else "balanceada"

print("--- RESULTADOS CUÁNTICOS (Deutsch-Jozsa) ---")
for nombre, func in funciones_n3:
    cuentas = dj_cuantico(func, n, shots=200)
    resultado = decidir(cuentas, n)
    print(f"Función: {nombre:8s} | Resultado más frecuente: {max(cuentas, key=cuentas.get)} | Detectado: {resultado}")

# COMENTARIO TÉCNICO: Los resultados muestran que las funciones constantes ("Todo 0" y "Todo 1") 
# devuelven el estado |000>, identificándose correctamente como constantes. Las funciones balanceadas 
# producen estados no nulos (|100>, |001>, |111>), permitiendo clasificarlas con una única consulta 
# mediante interferencia cuántica. La ejecución se simuló utilizando el servidor QVM activo en el 
# puerto 5000 mediante un contenedor de Docker.