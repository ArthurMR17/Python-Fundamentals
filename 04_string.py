name = "Arturo"
lastName= "Merlano"
print(name)
print(lastName)

fullName = name + " " + lastName
print(fullName)

#Comillas en string
quote = "I'm Arturo"  
print(quote)

quote2 = 'She said: "hello" '

#format usando las {}
template = "Hola, mi nombre es " + name + " y mi apellido es " + lastName
print(template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastName)
print(template2)

template3= f"Hola mi nombre es {name} y mi apellido es {lastName}"
print(template3)