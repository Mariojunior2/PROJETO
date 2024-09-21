# Padrao de colocacao
meu_dicionario = {
    "nome1":"Mario"
}

# Exemplo

estudante = {
    "nome":"mario",
    "idade":16,
    "curso":"Informatica"
}

# Acesando valores

nome = estudante["nome"]

# get() pergar algum valor

altura = estudante.get("altura", "Nao falada")

# Modificar Valores

estudante["idade"] = 23

# adicionando mais uma chave-valor

estudante["altura"] = 1.68

# removendo itens

del estudante["curso"]

# iterando no dicionario
# chaves

for chave in estudante.keys():
    print(chave)
    
# Valores

for valor in estudante.values():
    print(valor)
    
# ambos

for chave, valor in estudante.items():
    print(f"{chave}: {valor}")