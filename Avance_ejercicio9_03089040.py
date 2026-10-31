print("\n** Renata Zoé Valdés García  T03089040**")
print("\n** Grecia Avril Gutierrez Torres  T07252385 **")

print("* Ejercicio 9 TAMAÑO DE TU BEBIDA *")

#Mostramos el menú para que el usuario sepa qué puede elegir
print("\n. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. MENÚ DE TAMAÑOS . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.")
print("1 = Chico  ($45) ")
print("2 = Mediano ($65) ")
print("3 = Grande  ($75) ")

#input() pregunta y guarda la respuesta como TEXTO
#int() la convierte a número entero para poder comprarla con 1, 2 y 3
opcion = int(input("\n¿Qué tamaño quieres Escribe 1, 2 o 3:  "))
#Si el usuario escribe 2, ahora opción vale 2

#PREGUNTA 1: ¿2 es igual a 1? Respuesta: False, entonces pasa a la siguiente pregunta
if opcion == 1:
    print("Elegiste tamaño CHICO, son $45")

#PREGUNTA 2: ¿2 es igual a 2? Respuesta: True, entonces muestra este mensaje
#y Python YA NO revisa las preguntas de abajo
elif opcion == 2:
    print("Elegiste tamaño MEDIANO, son $65")

#PREGUNTA 3: solo se revisa si las dos anteriores fueron False
elif opcion == 3:
    print("Elegiste tamaño GRANDE, son $75")

#else: entra aquí solo si NINGUNA pregunta fue True (escribió 4, 7, 0, etc.)
else:
    print("Opción no válida, elige 1, 2 o 3")

#Esta línea no tiene sangría, no pertenece al if, por eso se muestra siempre
print("\n¡Gracias por tu compra!")
