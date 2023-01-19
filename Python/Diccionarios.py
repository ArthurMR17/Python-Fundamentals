def run():
    mi_diccionario = {
        "llave 1": 1,
        "llave 2": 2,
        "llave 3": 3,
    }

    print(mi_diccionario["llave 1"])
    # print(mi_diccionario["llave 2"])
    # print(mi_diccionario["llave 3"])

    poblacion_paises = {
        "Argentina":  44938712,
        "Brazil": 210147125,
        "Colombia": 50372424,
    }
    # print(poblacion_paises["Argea"])
    for pais in poblacion_paises.keys():
        print(pais)


if __name__ == "__main__":
    run()

mi_tupla = ("casa", 12354, True)
mi_lista = ["jajaja", True, 9999]

# Diccionarios
mi_diccionario = {
    "Pedro": 3,  # Llave, Valor
    123: "A",  # Llave, valor
    True: True,  # Llave, valor
    "Carlos": 7,  # Llave, valor
    "Altura": 3  # Llave, valor
}

print(f"ANTES: \n{mi_diccionario}")

mi_diccionario["Lorena"] = 78  # Agregar elemento al diccionario
print(f"DESPUES: \n{mi_diccionario}")
mi_diccionario["Lorena"] = 1
print(f"MODIFICANDO: \n{mi_diccionario}")      # modifcando el diccionario

# metodo get igual al if
if "Lorena" in mi_diccionario:
    print(f"\nEl valor de Lorena es: {mi_diccionario['Lorena']}")


print(f"Metodo Get, el valor de Lorena es: {mi_diccionario.get('Lorena')}\n")

salarios = {
    "Finanzas": {
        "Jairo": 700000,
        "Patricia": 50000
    },
    "Recursos Humanos": {
        "Jairo": 3650000,
        "Pedro": 25916541
    }
}


for elemento in mi_diccionario.values():
    print(f"Valor: {elemento}")
for elemento in mi_diccionario.keys():
    print(f"Key: {elemento}")
print("\n")

for k, v in salarios.items():
    print(k, v)

salarios.pop("Finanzas")
print(f"\n{salarios}")

print("\n")
print(f"Tamaño diccionario Salarios: {len(salarios)}")

print(f"Metodo Get, el valor de Pedro es: {salarios.get('Finanzas')}\n")

# REVISAR GRABACION DICCIONARIOS 28 / 06 / 2021
