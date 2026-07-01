print("Hola", 'mundo', 'como estas "fiera"?\n', "\"Chamaco\"", " \\campeon"  , sep="-", end="!")
print()
# Operadores + - * / % // ** 

# valor = int(input("ingrese un valor: ")) # valor por teclado

# Comparadores == != < > >= <= 

while True:
    print("bucle infinito")
    break

for i in range (3):
    print("va del 0 a 2:", i)

for letter in "word  long":
    print("letra", letter)
    if letter == "-":
        continue

start = 2 # 0 default
stop = 8 # stop - 1
step = 2

for i in range(start, stop, step):
    print(i)

# Listas
my_list = [1, None, True, "Soy una cadena", 256, 0]
print(my_list[3])
my_list[1] = '?'
print(my_list)
my_list.insert(0, "Primero") 
my_list.append("Ultimo")
len(my_list)
my_list.sort
my_list.reverse
listaParte = my_list[0:2]
listaTotal = my_list[:]
listaIndNeg = my_list[2:-1] #cuenta desde el final hacia el principio
1 in my_list # Booleano
2 not in my_list
my_list.count
del my_list[2]
del my_list

# Tuplas
myTuple = (1, 2, True, "una cadena", (3,4), [5,6], None)
oneElemTuple = ("uno",)
oneElemTuple = "uno",


#Diccionarios
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
item = dictionary["gato"]
item = dictionary.get("perro")
booleano = "key" in dictionary
booleano = "key" in dictionary.keys()
dictionary.items()
dictionary.update({"si":"simon"})
dictionary.popitem() # Pop, elimina el ultimo


# Excepciones
while True:
    try:
        number = int(input("ingrese un numero entero "))
        print(5/number)
        break
    except ValueError:
        print("Valor incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except:
        print("No se que hacer") #print("Advertencia: el valor ingresado no es un numero valido")



