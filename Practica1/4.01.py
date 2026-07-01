# Tuplas

myTuple = (1, 2, True, "una cadena", (3,4), [5,6], None)
myList = [1, 2, True, "una cadena", (3,4), [5,6], None]

emptyTuple = ()
print("emptyTuple", type(emptyTuple))

oneElemTuple = ("uno",)
oneElemTuple = "uno",
print("oneElemTuple", type(emptyTuple))

# Indexacion

print(myTuple[4])

del emptyTuple

tuple1 = (1,2,3)

for elemen in tuple1:
    print(elemen)

print(5 in tuple1)
print(5 not in tuple1)
print("len", len(tuple1))

tuple3 = tuple1 + oneElemTuple
tuple4 = tuple1 * 2

print(tuple3)
print(tuple4)


# Desempaquetar cada elemento de la tupla

a, b, c = tuple1

print(a, b, c)

# COunt 
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) 
print(duplicates) # salida: 4