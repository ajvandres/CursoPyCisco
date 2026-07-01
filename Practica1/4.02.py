# Diccionarios

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

item = dictionary["gato"]
print(item)

item = dictionary.get("perro")
print(item)
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)


words = ["gato", "leon", "caballo"]

for word in words:
    if word in dictionary:
        print(word, "-->", dictionary[word])
    else:
        print(word, "no esta en el diccionario")

print()

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()

for spanish, french in dictionary.items():
    print(spanish, "->", french)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
dictionary["si"] = "wi"
dictionary.update({"si":"simon"})
del dictionary["caballo"]
dictionary.popitem() # Pop, elimina el ultimo
print(dictionary)