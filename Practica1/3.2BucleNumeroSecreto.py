secret_number = 777


print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input())
while secret_number != numero:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingrese un numero nuevamente: "))
    
print("¡Bien hecho, muggle! Eres libre ahora.")    