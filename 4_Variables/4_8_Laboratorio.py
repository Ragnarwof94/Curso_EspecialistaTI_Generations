"""3. Ejercicios para el tipo de dato str (texto)
Empresa: "CustomerFirst" — Call Center de atención al cliente
Situación:
El supervisor necesita registrar el nombre del agente y el nombre del cliente atendido.
Ejercicio:
Pide al usuario:
Nombre del agente
 
 
Nombre del cliente
 
 
Objetivo:
Mostrar un mensaje combinando textos."""

nombre_agente = input("Ingrese el nombre del agente: \n")
nombre_cliente = input("Ingrese el nombre del cliente: \n")

print("\nEl agente", nombre_agente, "ha atendido al cliente", nombre_cliente, "\n***¡Gracias por su preferencia!***\n")