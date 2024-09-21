a = int(input('Valor 1: '))
b = int(input('Valor 2: '))

def calcular_mdc(x, y):
    while y != 0:
        x, y = y, x % y
    return x

mdc = calcular_mdc(a, b)
print(f"O MDC de {a} e {b} é {mdc}")
