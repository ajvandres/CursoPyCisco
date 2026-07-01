income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = max(income * 0.18 - 556.02, 0)
# Escribe tu código aquí.
else:
	tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
    