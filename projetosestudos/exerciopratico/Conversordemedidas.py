def exibir_menu():
    print("Escolha a conversao que deseja: ")
    print("1 - Celsius para Fahrenheit")
    print("2 - Quilometros para Milhas")
    print("3 - Quilogramas para Libras")


def celcius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def quilogramas_para_libras(quilogramas):
    return quilogramas * 2.20462

exibir_menu()
escolha = int(input("Digite o numero da opcao desejada: "))

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celcius_para_fahrenheit(celsius)
    print(f"{celsius}°C equivalem a {fahrenheit}°F.")
elif escolha == 2:
    quilometros = float(input("Fale os quilometros"))
    milhas = quilogramas_para_libras(quilometros)
    print(f"{quilometros} equivalem a {milhas}")  
elif escolha == 3:
    quilogramas = float(input("fale os quilograms"))
    libras = quilogramas_para_libras(quilogramas)
    print(f"{quilogramas} equivalem a {libras}")
else:
    print("Valor invalido!")