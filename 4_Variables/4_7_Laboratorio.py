"""2. Ejercicios para el tipo de dato float (decimal)
Empresa: "AquaPure" — Purificadora de agua
Situación:
El laboratorio debe registrar la cantidad de litros purificados en distintos tanques.
Ejercicio:
Pide al usuario:
Litros purificados en el tanque A
 
 
Litros purificados en el tanque B
 
 
Objetivo:
Calcular la producción total con decimales."""

Litros_tanque_A = input("Ingrese la cantidad de litros purificados en el tanque A: \n")
tanque_a = float(Litros_tanque_A)
Litros_tanque_B = input("Ingrese la cantidad de litros purificados en el tanque B: \n")
tanque_b = float(Litros_tanque_B)

total_Litros = tanque_a + tanque_b

print("Total de litros purificados: ", total_Litros)