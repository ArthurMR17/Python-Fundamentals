# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

numbers = (1, 2, 3, 4)
strings = ('casa', 'casa', 'zapato', 'calle')
print(numbers)
print('0 =>', numbers[0])
print(type(numbers))

print(strings)
print(type(strings))

print(strings.index('zapato'))
print(strings.count('casa'))

# Pasando de Tupla a Lista
print('Pasando de Tupla a Lista')
my_list = list(strings)
print(my_list)
print(type(my_list))

# Pasando de Lista  a Tupla
my_list[my_list.index('casa')] = 'otraaa'
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_list, my_tuple)
