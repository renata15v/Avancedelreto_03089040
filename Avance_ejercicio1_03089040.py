print("\n𝄞⨾𓍢ִ໋  Renata Zoé Valdés García T03089040 ໋𓍢ִ໋⨾𝄞")
print("𝄞⨾𓍢ִ໋  Grecia Avril Gutierrez Torres T07252385 ໋𓍢ִ໋⨾𝄞")

print("*** Ejercicio 1: Estado de mi celular ***\n")

bateria = int(input("¿Cuánta batería tienes?  "))
espacio = int(input("¿Cuántos GB libres tienes?  "))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes?  "))

if bateria <= 20:
    print("Batería baja, conecta tu cargador")

if espacio < 5:
    print("Poco espacio, borra fotos o apps que no utilices")

if notificaciones > 0:
    print("Tienes", notificaciones, "notificaciones sin leer\n")
else:
    print("Estás al día, no tienes notificaciones\n")
