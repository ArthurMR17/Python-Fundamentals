
def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero+1):
    if numero != i and numero % i == 0:
      return False
  return True  


def run ():
  numero = input("Ingresa un número: ")
  while numero.isdigit() == False:
    numero = input("""No has ingresado un número..
Ingresa un número: """)
  numero = int(numero)
  if es_primo(numero) == False:
    print(f"{numero} no es un numero primo")
  else: 
    print(f"{numero} si es un numero primo")


if __name__ == "__main__":
  run()


