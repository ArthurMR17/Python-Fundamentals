"""if True:
    print("Deberia ejecutarse")

if False:
    print("Nunca deberia Ejecutarse")
"""

pet = input("¿Cual es tu mascota favorita? ")
if pet == "perro":
    print("genial tienes buen gusto")

elif pet == "gato":
    print("espero que tengas suerte")

elif pet == "pez":
    print("espero que tengas suerte")

else:
    print("no tienes nunguna mascota interesante")
stock = int(input("digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("el stock es el correcto")
else:
    print("el stock es incorrecto")


print(1 == "1")  # False
print(1 is "1")  # False

if not es_fin_de_semana:
    print("A trabajar")
else:
    print("A disfrutar del fin de semana")
