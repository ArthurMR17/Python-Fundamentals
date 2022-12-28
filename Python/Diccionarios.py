def run():
  mi_diccionario = {
      "llave 1" : 1,
      "llave 2" : 2,
      "llave 3" : 3,
  }

  print(mi_diccionario["llave 1"])
  # print(mi_diccionario["llave 2"])
  # print(mi_diccionario["llave 3"])

  poblacion_paises = {
    "Argentina" :  44938712,
    "Brazil" : 210147125,
    "Colombia" : 50372424,
  }
  # print(poblacion_paises["Argea"])  
  for pais in poblacion_paises.keys():
    print(pais)

if __name__ == "__main__":
  run()
