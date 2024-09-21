def nome_da_funcao(parâmetros):
    # bloco de codigo 
    return valor_de_retorno # type: ignore # ignore
# def inidica quando comeca uma funcao

# nome_da_funcao nome que voce pega para funcao

# parametro variaveis que recebem valores quando a funcao e chamada

# return especifica o valor que a funcao da 

def saudacao():
    print("Hello Word!")
    
    
saudacao() # Aqui chama a funcao



def saudacao_personalizada(nome):
    print(f"Hello, {nome}! Welcome.")

saudacao_personalizada("Carlos")

# Valores de Retorno

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Soma = ", resultado)

# Exemplo de funcao do resultado
# Escopo de variaveis


# Escopo local variaveis definidas uma funcao somente dela mesma
def minha_funcao_local():
    x = 10
    print("Dentro da funcao, x =", x)
# Escopo Global variaveis definidas fora de funcao sao acessiveis em todo o programa
x = 20
minha_funcao_local()
print("Fora da funcao, x =", x)

# Padrao para parametros ARGUMENTOS PADRAO

def apresentar(nome, idade=18):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    
apresentar("Maria")

apresentar("Joao", 25)


# Argumentos Nomeados especifica os padraos


def calcular_area(largura, altura):
    return largura * altura

area = calcular_area(altura=5, largura=3)
print("Area:",area)


# Funcoes Recursivas uma funcao chamndo outra

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial de 5 ser:", fatorial(5))


# Funcoes lambda funcoes anonimas, em uma linha

lambda argumentos: expressao # type: ignore

dobro = lambda x: x * 2
print(dobro(5))



