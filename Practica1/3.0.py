contador = 0

while contador < 3:
    print(contador)
    contador += 1


# for itera sobre secuencias, como lista, diccionario, tupla o conjunto

palabra = "python"

for letra in palabra:
    print(letra)

for i in range(1,4):
    print(i)

# break sale del bucle, usando condicional

for letra in palabra:
    if letra == "h":
     break
    print(letra, end="")
print()

# continue saltea la posicion actual del bucle y pasa al siguiente , usando condicional

for letra in palabra:
    if letra == "h":
     continue
    print(letra, end="")
print()

# Los bucles while y for, pueden usar clausula else, que se ejecuta al finalizar el bucle, cuando no haya terminado en break
for i in range(1,4):
    print(i)
else:
   print(-1)


# range(start (opcional 0 deafult),     stop (opcional indica cuando termina -1),     opcional (valor incremento de secuencia 1 por defefcto) )  

for i in range(3):
   print(i, end="")
print()

for i in range(6, 1, -1):
   print(i, end="")
print()


# Lista es un tipo de datos que almacena multiples objetos, entre corchetes

lista = [1, None, True, "Cadena", 256, 0.8]

print(lista[3]) # Indexacion

lista [1] = "?" # asignacion de elemento
print(lista)

lista.insert(0, "primero") # inserta en posicion
lista.append("ultimo") # inserta en ultima posicion
del lista[1]
print(lista)
del lista # borra lista entera



listaAnidada = [1, 'a', ["lista", 64, [0,1], False]]



# listas iteradas
colores = ["rojo", "azul", "amarillo"]
for color in colores:
   print(color)

print("longitud lista:", len(colores))


# ORdenamiento
numeros = [3,5,1,2,4]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

