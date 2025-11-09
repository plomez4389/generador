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


def escoger_elementos(fuente, cantidad):
    """Escoge una cantidad de elementos aleatorios de una lista fuente."""
    return [random.choice(fuente) for _ in range(cantidad)]





# Usamos la función para generar las listas de caracteres
lista_letras = escoger_elementos(letras, 4)
print(lista_letras)

lista_numeros = escoger_elementos(numeros, 2)
print(lista_numeros)

lista_signos = escoger_elementos(signos, 2)
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
