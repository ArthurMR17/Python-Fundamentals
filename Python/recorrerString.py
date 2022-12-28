from ast import main
from tokenize import Name
from unicodedata import name


def run():
  nombre = input("Escribe tu nombre: ")
  for letra in nombre:
    print(letra)

  frase = input("Escribe una frase: ")
  for caracter in frase:
    print(caracter.upper())
  pass

if __name__ == "__main__":
  run()
