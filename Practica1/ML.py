# Datos de entrenamiento: pares de (x, y). Queremos que descubra que y es el doble de x.
datos = [(1, 2), (2, 4), (3, 6), (4, 8)]

w = 0.0  # El "cerebro" inicial del algoritmo (un peso al azar)
tasa_aprendizaje = 0.01

# Ciclo de entrenamiento: El algoritmo ajusta su "cerebro" con cada dato
for _ in range(100):  # Entrena por 100 iteraciones
    for x, y_real in datos:
        prediccion = w * x                  # Hace una suposición
        error = prediccion - y_real         # Calcula qué tan equivocado está
        w = w - (tasa_aprendizaje * error * x) # Ajusta el peso para mejorar

# --- ¡El modelo ya está entrenado! ---
# Ahora le pedimos que prediga el resultado para un número que NUNCA vio (el 5)
x_nuevo = 8
print(f"Para x={x_nuevo}, la IA predice y={x_nuevo * w:.2f}") 
# Resultado: Para x=5, la IA predice y=10.00