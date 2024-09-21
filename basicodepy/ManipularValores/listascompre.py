# listas Comprehensions
#  É uma forma concisa de criar listas a partir de sequências existentes.
# Sintaxe Basica

nova_lista = [expressao for item in sequencia if condicao] # type: ignore

# exemplo Quadros de 1 a 5

quadrados = [x**2 for x in range(1, 6)]
print(quadrados)

# numeros pares de uma lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [x for x in numeros if x % 2 == 0]
print(pares)