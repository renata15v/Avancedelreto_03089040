print("\n++++ Renata Zoé Valdés García T03089040 ໋++++")
print("++++ Grecia Avril Gutierrez Torres T07252385 ໋++++")

print("++++ Ejercicio 4 MIS ESTADÍSTICAS ++++")

usuario = input("¿Cuál es tu usuario?")
seguidores = int(input("¿Cuántos seguidores tienes?"))
likes = int(input("¿Cuántos likes tuvo tu ultimo video?"))

if seguidores >= 1000:
    print("Yapuedes hacer lives")
else:
    print("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes> seguidores:
    print(("¡Tu último video se hizo viral!\n"))
else:
    print("Sigue publicado, vas bien\n")