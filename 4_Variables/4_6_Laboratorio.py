"""1. Ejercicios para el tipo de dato int (entero)
 
Empresa: "LogiExpress" — Empresa de envíos nacionales
Situación:
El departamento de operaciones necesita calcular la cantidad total de paquetes procesados en una jornada.
Ejercicio:
Pide al usuario ingresar:
Cantidad de paquetes enviados en la mañana
 
 
Cantidad de paquetes enviados en la tarde
 
 
Cantidad de paquetes enviados en la noche
 
 
Objetivo:
Suma los valores y muestra el total de paquetes procesados."""

paquetes_am = input("Ingrese la cantidad de paquetes enviados en la mañana: \n")
print(type(paquetes_am))
paquetes_am = int(paquetes_am)
print(type(paquetes_am))
paquetes_pm = input("Ingrese la cantidad de paquetes enviados en la tarde: \n")
print(type(paquetes_pm))
paquetes_pm = int(paquetes_pm)
print(type(paquetes_pm))
paquetes_nocturno = input("Ingrese la cantidad de paquetes enviados en la noche: \n")
print(type(paquetes_nocturno))
paquetes_nocturno = int(paquetes_nocturno)
print(type(paquetes_nocturno))

total_paquetes = paquetes_am + paquetes_pm + paquetes_nocturno

print("Total de paquetes procesados en la jornada: ", total_paquetes)
