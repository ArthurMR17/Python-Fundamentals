# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios


myDic = {}


myDic = {
    'avion': 'bla bal bla',  # Llave, valor
    'name': 'Nicolas',      # Llave, valor
    'lastName': 'Molina Monroy',  # Llave, valor
    'age': 87  # Llave, valor

}

myDic2 = {
    'llave1': 1,
    'llave2': 2
}


# print(myDic, myDic2)
# print('impirmir cuantos elementos hay =>')
# print(len(myDic))


# Impirmir el valor correspondiente a la clave
print('imprimiendo el valor de la clave "avion": ', myDic['avion'])
print(myDic['age'])
print(myDic['lastName'])


# .get() puede manejar el error si la clave no existe
print(myDic.get('un valor', 'Esta clave no existe .get() metodo'))

# # Saber si una clave esta dentro del diccionario
# print('!!!!!!!!!!!')
# print('avion' in myDic)
# print('otroque no' in myDic)


# Manipular Diccionarios
person = {
    'name': 'Arturo',
    'lastName': 'Merlano',
    'langs': ['python', 'javascript'],
    'age': 99
}

# Copiar diccionario como referencia a memoria
person1 = person

# Copiar diccionario como valores en memoria
person1 = dict(person)
dic1 = myDic2.copy()
# print(person1)
# print(person)
# print('\n')


# Actualizando valores del diccioanrio
print(person)
person['name'] = 'Kevin'
person['age'] -= 40

# Agregando con append porque el valor es una lista
# person1['langs'] = person1.append('cas')
# print(person1)
person1['langs'] = list(person['langs'])
person1['langs'].append('rust')
print(person1)
print(person)


# Eliminando atributo del diccionario
del person['lastName']
# print(person)

person.pop('age')
# print(person)
# print(person1)

print('Items: ')
print(person1.items())
print(person.items())
