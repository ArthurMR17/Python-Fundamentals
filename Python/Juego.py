import random

def run():
  print("""Adivina un número del 1 al 100

Mucha Suerte!!

 """)
  random_numero = random.randint(1,100)
  numero =int(input("Ingresa tu respuesta: "))
  while random_numero != numero:
    if numero > random_numero:
      print("""
Fallaste!! :(
Elige un número mas pequeño: """)
    elif numero < random_numero:
      print("""
Fallaste!! :(
Elige un número mas grande: """)
    numero = int(input(": "))
  
  print(f"GANASTE!! con el numero {numero}")
  

if __name__ == "__main__":
  run()