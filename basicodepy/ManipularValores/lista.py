minha_lista = [1] # Valore ficam dentro dos []

# EXEMPLOS

numeros = [1, 2, 3, 4, 5]
palavras = ["Hello", "Word"]
misturas = [1, "Python", True]

# ACESSAR ELEMNTOS

primeiro_elemento = numeros[0] # 1
ultimo_elemento = numeros[-1] # 5

# MODIFICAR OS VALORES

numeros[0] = 10 # [10, 2, 3, 4, 5]

numeros.append(6) # [10, 2, 3, 4, 5, 6] append adiciona ao fila da lista

numeros.insert(1, 15) #  [10, 15, 2, 3, 4, 5, 6] inset adiciona em lugar especifico

numeros.remove(3) # Retira elementos o remove no caso o 3

ultimo = numeros.pop() # Remove e retorna o ultimo elemento

# Fatiamento

sublista = numeros[1:4] # Elementos do indice 1 ao 3

# Iterando elementos na lista

for numero in numeros:
    print(numero)
    
    
# len() Retorna o tamanho da lista

tamanho = len(numeros)
print(tamanho)

# sorted() retorna uma nova lista ordenada

ordenada = sorted(numeros)

# sum() retorna a soma dos elementos se forem numeros

total = sum(numeros)


