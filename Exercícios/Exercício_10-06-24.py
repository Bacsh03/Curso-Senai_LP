# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

'''
Exercícios
1 - Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da corrida do táxi, sendo R$ 5,90 pela bandeira e R$ 2,70 por km rodado.

2 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassou 100km/h. Mostre a mensagem dizendo "você foi multado". A multa vai custar R$50,00 + R$8,00 por cada km a mais de 100km/h.

3 - Faça um programa que leia um ano qualquer e diga se ele é Bissexto.

4 - Escreva um programa que pergunte o salário do usuário e calcule o valor do seu aumento; para salários superiores a R$ 1.420,00 calcule um aumento de 15%, para valores inferiores ou iguais aumento de 30%.
'''

def exercicio_1():
    print("Programa para calcular valor de uma corrida de taxi.")

# Definição de valores e distância da viagem
    distancia = float(input("Digite o valor da viagem em KM: "))
    bandeira = 5.90
    km_rodado = 2.70

# Calculo da corrida
    preco_corrida = (distancia * km_rodado) + bandeira
    print(f"O valor da sua corrida será de: R$ {preco_corrida:.2f}")

def exercicio_2():
    print("Analisando se o carro foi multado.")

# Definição da velocidade e valores
    velocidade = float(input("Insira a velocidade que o carro passou no radar em KM/H: "))
    multa_minima = 50
    multa_por_km = 8

# Calculo da multa
    if velocidade > 100:
        velocidade_extra = velocidade - 100
        valor_multa = (velocidade_extra * multa_por_km) + multa_minima
        print (f"Você foi multado em: R$ {valor_multa:.2f}")
    else:
        print("Você não foi multado!")
        

def exercicio_3():
    print("Dizer se ano é bissexto")

# Definição do ano a ser verificado
    ano = int(input("Digite um ano: "))

# Verificando se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")


def exercicio_4():
    print("Calculo de aumento de salário")

# Definição do valor do salário
    salario = float(input("Informe qual é o seu salário: "))

# Calculo de aumento do salário
    if salario > 1420:
        salario_aumento = salario * (15 / 100)
        novo_salario = salario + salario_aumento
        print(f"O seu novo salário com o aumento é: {novo_salario:.2f}")
    else:
        salario_aumento = salario * (30 / 100)
        novo_salario = salario + salario_aumento
        print(f"O seu novo salário com o aumento é: {novo_salario:.2f}")


def menu():
    while True:
        limpar_terminal()
        print("╔═════════════════════════════╗")
        print("║     Menu de Exercícios      ║")
        print("╠═════════════════════════════╣")
        print("║ 1. Exercício 1              ║")
        print("║ 2. Exercício 2              ║")
        print("║ 3. Exercício 3              ║")
        print("║ 4. Exercício 4              ║")
        print("║ 0. Sair                     ║")
        print("╚═════════════════════════════╝")
        
        escolha = input("Selecione o exercício que deseja executar (0 para sair): ")

        if escolha == '1':
            limpar_terminal()
            exercicio_1()
        elif escolha == '2':
            limpar_terminal()
            exercicio_2()
        elif escolha == '3':
            limpar_terminal()
            exercicio_3()
        elif escolha == '4':
            limpar_terminal()
            exercicio_4()
        else:
            input("Opção inválida! Pressione ENTER para tentar novamente.")

        input('Aperte ENTER para voltar ao Menu de Exercícios.')
        limpar_terminal()

menu()