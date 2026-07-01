def mensaje(nombre):
    print("holas", nombre)

mensaje("Andres")

# Argumentos posicionales y palabras clave

def substra(a, b):
    print(a-b)

substra(5,2)
substra(2,5)

substra(a=5, b=2)
substra(b=2, a=5)

substra(5, b=2) # Orden correcto, 1° posicional, luego palabra clave
#substra(b=2, 5) # Orden incorrecto  

def nombreCompleto(nombre, apellido="Violano"):
    print(nombre, apellido)

nombreCompleto("Abigail", "Vive")
nombreCompleto("Andres")    


def wishes():
    print("Mis deseos")
    return "Feliz Cumpleaños"

wishes()

print(wishes())

def hiEverybody(miList):
    for name in miList:
        print("Hola", name)

hiEverybody(["Andres", "Abigail","Santiago", "Valentina"])


def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(3))    


# Variable global

def returnValor():
    global var
    var = 5
    return var

print(returnValor())
print(var)


# Funcion Recursiva

def factorial(n):
    if n == 1: # Caso base condicion de terminacion
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))    