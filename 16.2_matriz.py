def diagonal_matrix(casX):
    Y = []
    for i in range(len(casX)):
        Y.append(casX[i][i])
        print(Y)
    return Y


print(diagonal_matrix([[1, -6, 6], [8, 9, .4], [7, 5, -7]]))
print('\n')
matriz = [[1, -6, 6], [8, 9, .4], [7, 5, -7]]
empty = []
for contador in range(len(matriz)):
    print(f" una {matriz[contador][contador]}")
    empty.append(matriz[contador][contador])
print(empty)

print("\n")


# conocer posicion del numero mayor dentro de la lista o arreglo
def pos_maximo(Ab):
    m = 0
    for i in range(0, len(Ab)):
        if Ab[i] > Ab[m]:
            m = i
    return m


print(pos_maximo([111, 99, 44, 1, 6]))
