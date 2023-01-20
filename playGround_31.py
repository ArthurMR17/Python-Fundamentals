person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'
person.update({'name': 'Felipe'})
del person['age']
listKeys = list(person.keys())
listValues = list(person.values())
print(listKeys)
print(listValues)
