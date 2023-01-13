# CRUD Create, Read, Update, Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

# Agregar elemento al final de la lista
numbers.append(700)
print(numbers)

# Agregar en posicion (0) el dato "hola"
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, 'change')
print(numbers)

# Unir dos Listas
task = ['todo1', 'todo2', 'todo3']
newList = numbers + task
print(newList)

# Buscar elemento en la lista
index = newList.index('todo2')
print(index)
newList[index] = 'cambiamos todo2 por esto'
print(newList)

# Eliminar elementos de la lista
newList.remove('todo1')
print(newList)

# Eliminar ultimo elemento de la lista
newList.pop()
print(newList)

newList.pop(0)
print(newList)

# Cambiar el orden de la lista
newList.reverse()
print(newList)

# Ordenas array de numeros
numbers1 = [2, 6, 4, 3]
numbers1.sort()
print(numbers1)

listString = ['ab', 'bd', 'bc', 'ac']
listString.sort()
print(listString)
