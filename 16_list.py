# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

numbers = [1, 2, 3, 4]
n = numbers.copy()  # copia de valor en memoria
n = list(numbers)  # copia de valor en memora
# n = numbers  # Referencia a memoria
n.pop(1)
print('imprimiendo n', n)
print('imprimiendo numbers', numbers)
print(type(numbers))

types = [1, True, 'hola']
print("Types => ")
print(types)


# inmutables
# Packing
info_usuario = ("Carlos Perez", 45, 1.72, True, "NuevaEPS")
print(info_usuario, "\n")

for elemento in info_usuario:
    print(elemento)
print("\n")


nombre = input("nombre paciente")
edad = input("edad paciente")
print("\n")


# info_usuario2 = (nombre, edad, 1.72, True, "Nueva EPS", 346546)


# Unpacking
nombre, edad, altura, covid, eps = info_usuario
print("Unpacking de una tupla:")
print(f"nombre: {nombre}")
print(f"edad: {edad}")
print(f"altura: {altura}")
print(f"covid: {covid}")
print(f"eps: {eps}")
print("\n")


info_pareja = ("Pedro", 20, 1.58, 78)
info_hogar = (8, 20, "Cali", True, info_pareja)
info_usuario3 = (nombre, edad, 1.72, info_hogar, True, "Nueva EPS", 346546)
# print(info_usuario3)

info_usuario1 = ("Pedro", 50, 1.72, True)
info_usuario2 = ("Gabriela", 50, 1.75)
info_usuario3 = ("Lorena", 20)

infoTotalA = (info_usuario1, info_usuario2, info_usuario3)
infoTotalB = info_usuario1 + info_usuario2 + info_usuario3
print(infoTotalA)
print("###########")
print(infoTotalB)


texto = "bienvenidos para irnos a la calle mañana"
print("INTERCAMBIO DE TEXTO, FUNCION REPLACE \n")
textocambio = texto.replace("calle", "'cambiamos calle por' autopista")
print(texto, "\n")
print(textocambio, "\n")


my_tuple = (56, "Blue", True, 3.141516, "Yellow")
print(f"My tupla: {my_tuple}", "\n")

my_list = [56, 'Yellow', "Blue", True, 3.141516, "Yellow"]
print(f"Antes: {my_list}")

my_list.insert(2, "Gold")
print(f"Despues: {my_list}")

my_list.append("Magenta")
my_list.append("Gray")
my_list.append("Black")
print(f"DESPUES de append: {my_list}")

vacunas = ["Pfizer", "Moderna", "Aztrazeneca", "Spunik"]
my_list.extend(vacunas)
print("\n")
print(f"Despues de Extended: {my_list}")


indice = 0
while indice < len(my_list):
    elemento = my_list[indice]
    print(elemento)
    indice += 1
print("\n")


for elemento in my_list:
    print(elemento)
print("\n")

for elemento in range(0, len(my_list)):
    print(elemento)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(i)
    print(thislist[i])
print('\n')
print(my_list.count('Yellow'))
