def conversor(tipo_pesos, valor_dolar):
  pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes? ")
  pesos = float(pesos)
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  # print(f'Tienes ${dolares} dolares')
  print("Tienes $" + dolares + " dolares")

menu = """ 
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

print(menu)
seleccion = int(input())
if(seleccion == 1):
  conversor("Colombianos", 4450)
elif(seleccion == 2):
  conversor("Argentinos", 65)
elif seleccion == 3:
  conversor("Mexicanos", 24)