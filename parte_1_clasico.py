
# Algoritmo de Deutsch - Versión Clásica
class OraculoClasico:
    """Caja negra: solo se accede a f a través de este contador."""
    def __init__(self, f):
        self.f = f
        self.consultas = 0

    def __call__(self, x):
        self.consultas += 1
        return self.f(x)

def deutsch_clasico(f):
    oraculo = OraculoClasico(f)
    # Se evalúa obligatoriamente en x=0 y x=1 (2 consultas fijas)
    f0 = oraculo(0)
    f1 = oraculo(1)
    tipo = "constante" if f0 == f1 else "balanceada"
    return tipo, oraculo.consultas

# Catálogo de las 4 funciones de Deutsch
f0 = lambda x: 0          # Constante
f1 = lambda x: 1          # Constante
f2 = lambda x: x          # Balanceada
f3 = lambda x: 1 - x      # Balanceada

print("--- RESULTADOS VERSIÓN CLÁSICA (Deutsch) ---")
for nombre, func in [("f0(x)=0", f0), ("f1(x)=1", f1), ("f2(x)=x", f2), ("f3(x)=1-x", f3)]:
    tipo, consultas = deutsch_clasico(func)
    print(f"Función: {nombre} | Tipo: {tipo} | Consultas: {consultas}")

# COMENTARIO TÉCNICO: Los resultados empiricos muestran que todas las funciones (f0, f1, f2 y f3) 
# requieren exactamente 2 consultas en la version clasica. Esto ocurre porque el algoritmo determinista 
# no puede descartar de antemano el tipo de funcion y se ve obligado a evaluar la caja negra punto a 
# punto para ambas entradas posibles (x=0 y x=1), alcanzando siempre el coste maximo del peor caso para n=1.