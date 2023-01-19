def run():
    """ CONTINUE """


for contador in range(10):
    if contador % 2 != 0:     # % modulo (lo que queda de la div) != diferente
        continue
      # break
    print(contador)


""" BREAK """
for i in range(100):
    if i == 0:
        break
    print(i)

texto = input("Escribe un texto: ")
for letra in texto:
    if letra == "o":
        # continue
        break
    print(letra)


if __name__ == "__main__":
    run()
