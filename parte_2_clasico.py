
# Deutsch-Jozsa - Versión Clásica

n = 3

# Catálogo de las 6 funciones para n=3
f_todo_0 = lambda x: 0
f_todo_1 = lambda x: 1
f_b_msb   = lambda x: (x >> 2) & 1                  # x0 (bit más significativo)[cite: 8]
f_b_lsb   = lambda x: x & 1                         # x2 (bit menos significativo)[cite: 8]
f_b_par   = lambda x: bin(x).count("1") % 2         # Paridad x0 ^ x1 ^ x2[cite: 8]
f_b_tab   = lambda x: 1 if x in [1, 2, 3, 6] else 0 # Tabla específica[cite: 8, 9]

funciones_n3 = [
    ("Todo 0", f_todo_0), ("Todo 1", f_todo_1), ("b_msb", f_b_msb),
    ("b_lsb", f_b_lsb), ("b_par", f_b_par), ("b_tab", f_b_tab)
]

class OraculoClasicoDJ:
    def __init__(self, f):
        self.f = f
        self.consultas = 0

    def __call__(self, x):
        self.consultas += 1
        return self.f(x)

def dj_clasico(f, n):
    oraculo = OraculoClasicoDJ(f)
    primero = oraculo(0)
    # Comprueba hasta 2^(n-1) + 1 entradas en el peor caso
    for x in range(1, 2**(n - 1) + 1):
        if oraculo(x) != primero:
            return "balanceada", oraculo.consultas
    return "constante", oraculo.consultas

print("--- RESULTADOS CLÁSICOS (Deutsch-Jozsa) ---")
for nombre, func in funciones_n3:
    tipo, consultas = dj_clasico(func, n)
    print(f"Función: {nombre:8s} | Tipo: {tipo:10s} | Consultas: {consultas} (Máx teórico: {2**(n-1) + 1})")

# COMENTARIO TÉCNICO: Los resultados muestran que las funciones constantes ("Todo 0" y "Todo 1") 
# y la función balanceada "b_msb" alcanzan el máximo teórico de 5 consultas (2^(n-1) + 1), ya que el 
# algoritmo clásico determinista necesita agotar la mitad de las entradas más uno para confirmar 
# que la función es constante o descartarla. En cambio, funciones como "b_lsb", "b_par" y "b_tab" 
# requieren solo 2 consultas al encontrar un valor diferente de forma prematura.