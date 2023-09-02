import random

options = ("piedra", "papel", "tijera")  # esto es una tupla
user_win = 0
computer_win = 0

while computer_win < 2 and user_win < 2:
    user_option = input("Piedra, Papel o Tijera =>: ")
    user_option = user_option.lower()
    if not user_option in options:
        print("ingresaste una opcion errada")
        continue  # si hay un error el programa no validara lo demas y reinicia
    computer_option = random.choice(options)
    print(computer_option)
    print("\n")
    if computer_option == user_option:
        print("Hubo un empate!")
    elif computer_option == "papel":
        if user_option == "piedra":
            computer_win += 1
            print("Papel gana a piedra")
            print("La computadora gano!!,")
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
        else:
            user_option == "tijera"
            print("tijera gana a papel")
            print("el usuario gano!!")
            user_win += 1
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
    elif computer_option == "piedra":
        if user_option == "tijera":
            computer_win += 1
            print("piedra gana a tijera")
            print("La computadora gano!!,")
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
        else:
            user_option == "papel"
            print("papel gana a piedra")
            print("el usuario gano!!")
            user_win += 1
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
    elif computer_option == "tijera":
        if user_option == "papel":
            computer_win += 1
            print("tijera gana a papel")
            print("La computadora gano!!,")
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
        else:
            user_option == "piedra"
            print("piedra gana a tijera")
            print("el usuario gano!!")
            user_win += 1
            print(f"Marcadador: Computadora {computer_win} Usuario: {user_win}")
