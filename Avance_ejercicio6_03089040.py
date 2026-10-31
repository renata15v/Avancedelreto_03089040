print("\n~~ Grecia Avril Gutierrez Torres   T07252385 ~~")
print("\n~~ Renata Zoé Valdés García T03089040 ~~")

print("~~ Ejercicio 6 MI META DE AHORRO ~~")

producto = input("¿Qué quieres comprar?")
precio = float(input("¿Cuánto cuestan?"))
ahorrado = float(input("¿Cuánto tienes ahorrado?"))
ahorro_semanal = float(input("¿Cuánto ahorras por semana?"))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal
    print("Te faltan $", faltante, "para tus", producto, sep="")
    print("Ahorrado $", ahorro_semanal, "por semana, los tenrás en", semanas, "semanas", sep="")
    print("\n")
