import random
import string


def generar_contrasena(x):
  # string.ascii_lowercase = abcdefghijklmnopqrstuvwxyz
  # string.ascii_uppercase = ABCDEFGHIJKLMNOPQRSTUVWXYZ
  letras = string.ascii_letters 
  # combinación de ambos metodos
  numeros = string.digits 
  simbolos = string.punctuation
  caracteres = letras + numeros + simbolos
  #  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  contrasena = ""
  for i in range(x):
    contrasena += random.choice(caracteres)
  return contrasena  
  
def run():
  longitud_contrasena = int(input("Longitud de la contraseña: "))
  contrasena = generar_contrasena(longitud_contrasena)
  print(f" Tu nueva contraseña es: {contrasena}")
 

if __name__ == "__main__":
  run()