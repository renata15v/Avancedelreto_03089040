print("\n** Renata Zoé Valdés García  T03089040**")
print("\n** Grecia Avril Gutierrez Torres  T07252385 **")

print("⋆. 𐙚˚࿔ Ejercicio 15: Rango en tu videojuego 𝜗𝜚˚⋆")

#int() convierte el texto a número entero para poder comparar y hacer cuentas
puntos = int(input("\n¿Cuántos puntos tienes?"))
#Si el usuario escribe 3000, ahora puntos vale 3000

print("\n⋆. 𐙚˚࿔ TU RANGO 𝜗𝜚˚⋆")

#Empezamos por el rango MÁs ALTO
#¿3000 es mayor o igual que 3500? False, pasa a la siguiente
if puntos > 3500:
    print("Rango:DIAMANTE")
    print("¡Ya estás en el rango máximo!")

#¿3000 es mayor o igual que 2500? True, entra aquí y TERMINA
elif puntos > 2500:
    #esta formula dice: faltan = 3500 - 3000
    falta =3500 - puntos
    #Ahora faltan vale 500
    print("Rango: ORO")
    print(f"Te faltan {falta} puntos para Diamante")

elif puntos > 1500:
    faltan = 2500 - puntos
    print("Rango: PLATA")
    print(f"Te faltan {faltan} puntos para Oro")

#else: tiene menos de 1500
else:
    falta = 1500 - puntos
    print("Rango: BRONCE")
    print(f"Te faltan {falta} puntos para Plata")