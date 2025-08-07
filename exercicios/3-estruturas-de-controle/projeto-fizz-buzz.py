numeros = []

for numero in range(1000):
    if numero % 3 == 0 and numero % 5 == 0:
        numeros.append('Nicolas')
    elif numero % 3 == 0:
        numeros.append('É')
    elif numero % 5 == 0:
        numeros.append('Viado')
    else:
        numeros.append(numero)

print(numeros)



