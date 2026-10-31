print("\n** Ejemplo 2: if y else, ¿qué me pongo? **\n")
 
#LEER TEMPERATURA (paralelogramo verde). Si el usuario escribe 10, ahora temperatura vale 10
temperatura = int(input("¿Cuántos grados hace? "))
 
#LA PREGUNTA (rombo amarillo). ¿10 es menor que 15? Respuesta: True, entonces va por el camino del if
if temperatura < 15:
    #CAMINO DEL SÍ (rectángulo azul de la izquierda)
    print("Hace frío, ponte sudadera")
#else significa "si no": aquí entra solo si la respuesta fue False
else:
    #CAMINO DEL NO (rectángulo rosa de la derecha)
    print("Hace calor, ponte playera")
 
#CAMINO PRINCIPAL: los dos caminos se juntan aquí
print("¡Que tengas buen día!")