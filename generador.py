import random

'''
Aplicación que ayuda a generar una contraseña random a partir
de letras, números y signos. 
'''

#Se podría incluir más adelante la 'ñ' o la 'ç'...

letras = ['a', 'b', 'c', 'd',
          'e', 'f', 'g', 'h',
          'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p',
          'q', 'r', 's', 't',
          'u', 'v', 'w', 'x',
          'y', 'z']

# el 0 (cero) no lo incluyo. Puede confundirse con la letra 'o'.

numeros = ['1', '2', '3', '4',
           '5', '6', '7', '8',
           '9']

#Se podría incluir más adelante '¿' o '¡'

signos = ['@', "#", '$', '%',
           '&', '(', ')', '=',
           '?', '*', '+', '-'
           '!']



# Creamos un listado donde temporalmente guardaremos las letras escogidas
lista_letras = []

# Escogeremos 4 letras de manera aleatoria
for _ in range(4):
    # Y las guardarás en una lista llamada lista_letras[]
    lista_letras.append(random.choice(letras))

# Imprime lista_letras[]
print(lista_letras)


# Creamos un listado donde temporalmente guardaremos las letras escogidas
lista_numeros = []

#escogeremos 2 números
for _ in range(2):
    #Vamos guardando los números escogidos aleatoriamente en lista_numeros[]
    lista_numeros.append(random.choice(numeros))

print(lista_numeros)


# Hacemos los mismo con los signos
lista_signos = []
for sig in range(2):
    lista_signos.append(random.choice(signos))

print(lista_signos)

# Ahora coges y unes los 3 listados en uno sólo que se llamará acceso[]
acceso = lista_letras + lista_numeros + lista_signos
print(acceso)

# Ahora desordenas la lista acceso[]

random.shuffle(acceso)

# Imprimes la lista acceso[]

print(acceso)

# Concatena todos los elementos de la lista acceso[] en un string. Entre carácteres meto un espacio
# para poderlo leer mejor en la pantalla

password = " ".join(acceso)

# Imprime el string password

print(f"Tu contraseña generada es: {password}")
