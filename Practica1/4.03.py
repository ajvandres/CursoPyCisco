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


while True:
    try:
        number = int(input("ingrese un numero entero "))
        print(5/number)
        break
    except (ValueError,ZeroDivisionError):
        print("Valor incorrecto o No se puede dividir por cero")
    except KeyboardInterrupt:
        print("Interrupcion por teclado")
    except:
        print("No se que hacer") #print("Advertencia: el valor ingresado no es un numero valido")        