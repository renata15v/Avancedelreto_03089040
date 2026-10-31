print("\n~~ Grecia Avril Gutierrez Torres   T07252385 ~~")
print("\n~~ Renata Zoé Valdés García T03089040 ~~")

print("~~ Ejercicio 7 Tiempo de pantalla ~~")

nombre = input("¿Cómo te llamas?  ")
limite = float(input("¿Cuál es tu límite de horas?  "))
horas_redes = float(input("¿Cuántas horas en redes sociales?  "))
horas_juegos = float(input("¿Cuántas horas en videojuegos?  "))

total = horas_redes + horas_juegos 
print(nombre + ", hoy usaste el celular", total, "horas")

if total > limite:
    print("Te pasaste", total - limite, "horas de tu límite, ¡es hora de desconectarte!")
else: 
    print("¡Felicidades! Cumpliste tu meta de tiempo de pantalla")

if horas_redes > horas_juegos:
    print("Lo que más usaste fueron las redes sociales\n")
else:
    print("Lo que más usaste fueron los videojuegos\n")
    