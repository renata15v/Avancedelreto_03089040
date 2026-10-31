
print("\n𝄞⨾𓍢ִ໋  Renata Zoé Valdés García T03089040 ໋𓍢ִ໋⨾𝄞")
print("𝄞⨾𓍢ִ໋  Grecia Avril Gutierrez Torres T07252385 ໋𓍢ִ໋⨾𝄞")

print("*** Ejercicio 3: WI-FI DEL CAFÉ ***\n")

contrasena_cafe = "Coffee4ever"

nombre = input("¿Cómo te llamas?  ")
contrasena = input("Escribe la contraseña:  ")
gasto = float(input("¿Cuánto gastaste?  "))

if contrasena == contrasena_cafe:
    print("Conectado al WI-FI, bienvenida", nombre)
else:
    print("Contraseña incorrecta")

if gasto >= 100: 
    print("Tienes 1 hora de WI-FI\n")
else:
    print("Tienes 30 minutos de WI-FI\n")
