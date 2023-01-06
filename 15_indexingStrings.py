text = "Ella sabe Python"
print(text[0])


size = len(text)  # metodo para tomar el tamaño de una string

# se resta uno porque el metodo devuelve el total de desde 1 pero la posicion inicia en 0
print(f"ultima posición de {text}")
print(text[size-1])
print(text[-1])  # ultima letra de la cadena

# Slicing
print("# Slicing..")
print(text[0:5])
print("# Sacando palabra 'Python' de text")
print(text[10:16])
# Obviando parametro inicial del slicing :X
print("# Imprimiendo 'ella sabe'")
print(text[:10])
# Obiviando parametro final
print("# imprimiendo 'sabe python'")
print(text[5:])
# Obiviando parametro inicial y final
print("# imprimiendo todo el texto obviando parametros inicial y final")
print(text[:])
# saltando
print("# Saltando caracteres de 2 en 2")
print(text[::2])
