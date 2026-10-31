print("\n^^^^ Grecia Avril Gutierrez Torres   T07252385 ^^^^")
print("\n^^^^ Renata Zoé Valdés García T03089040 ^^^^")

print("^^^^ Ejercicio 8: CUENTA ENTRE AMIGAS ^^^^")

cuenta = float(input("¿Cuánto fue la cuenta?"))
personas = int(input("¿Cuántas personas van a pagar?"))
dinero = float(input("¿Cuánto dinero traes?"))

propina = cuenta * 10 / 100
total = cuenta + propina
por_persona = total / personas

print("Total con propina: $", total, sep="")
print("A cada persona le toca: $", por_persona, sep="")

if dinero >= por_persona:
    print("Te alcanza, te sobran $", dinero - por_persona, sep="")
else:
    print("No te alcanza, te faltam $", por_persona - dinero, sep="")

if por_persona > 300:
    print("Salio caro, la próxima busquen  promo\n")
else:
    print("¡Buen precio!\n")