# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios


myDic = {}


myDic = {
    'avion': 'bla bal bla',
    'name': 'Nicolas',
    'lastName': 'Molina Monroy',
    'age': 87

}

myDic2 = {
    'llave1': 1,
    'llave2': 2
}

print(myDic, myDic2)
print('impirmir cuantos elementos hay =>')
print(len(myDic))
# Impirmir el valor correspondiente a la clave
print('imprimiendo el valor de la clave "avion": ', myDic['avion'])
print(myDic['age'])
print(myDic['lastName'])

# .get() puede manejar el error si la clave no existe
print(myDic.get('un valor'))

# Saber si una clave esta dentro del diccionario
print('!!!!!!!!!!!')
print('avion' in myDic)
print('otroque no' in myDic)
