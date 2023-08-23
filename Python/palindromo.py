def palindromo(palabra):
  palabra = palabra.replace(" ", "") # eliminar espacios vacios 
  palabra = palabra.lower()
  palabra_invertida = palabra[::-1]
  # [indice inicio, indice final, cuanto aumenta el indice]
  if palabra_invertida == palabra:
    return True
  else:
    return False

# Crear funcion principal run
def run():
  palabra = input("Escribe una palabra: ")
  es_palindromo = palindromo(palabra)
  if es_palindromo == True:
    print("Es palindromo")
  else:
    print("No es Palindromo")
  
# punto de entrada, buena practica
if __name__ == "__main__":
  run()