text = "ella sabe programar en Python"
"""
print("Java" in text)
print("Python" in text)

if "Python" in text:
    print("Elegiste bien ")
else:
    print("tambien pues")
"""
size = len(text)
print(size)

print(text.upper())
print(text.lower())
print(text.count("a"))

print(text.swapcase())
print(text.startswith("ella"))
print(text.endswith("Rust"))
print(text.replace("Python", "Go"))

text2 = "este es un titulo"
print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
