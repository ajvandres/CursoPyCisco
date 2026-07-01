hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

horasDura = dura // 60
minsDura = dura - horasDura *60
minsFinal_c_Horas =  minsDura + mins
minsFinal = minsFinal_c_Horas % 60
horasMas60Min = minsFinal_c_Horas // 60
horasFinal = (horasDura + hour + horasMas60Min) % 24

print(horasFinal,minsFinal,sep=":")


print(horasDura)
print (minsDura)
print(minsFinal_c_Horas)
print(minsFinal)
print(horasMas60Min)
print(horasFinal)
