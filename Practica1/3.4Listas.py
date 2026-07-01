# 2)

my_list = [1, None, True, "Soy una cadena", 256, 0]

print(my_list[3])
print(my_list[-1])

my_list[1] = '?'

print(my_list)

my_list.insert(0, "Primero")
my_list.append("Ultimo")

print(my_list)


# 3)

mi_lista = [1, 'a', ["lista", 64, [0, 1], False]]

print(mi_lista)

mi_lista.insert(1, ["otra", "lista"])

print(mi_lista)



# 4)

del mi_lista[3]

print(mi_lista)

del mi_lista


# 5)

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in my_list:
    print(color)

print(len(my_list))

del my_list[2]

print(len(my_list))