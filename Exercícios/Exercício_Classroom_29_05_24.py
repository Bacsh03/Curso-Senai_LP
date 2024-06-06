# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

    #Exercícios para fixação Algoritmos e Logica
def exercicio_1():
    #Exercicio - 1
    print('Exercício - 1')

    #Requerimento dos dados de A, B, C
    A = float(input('Digite o valor para A: '))
    B = float(input('Digite o valor para B: '))
    C = float(input('Digite o valor para C: '))

    #Calculo de A + B
    soma = A + B
    print(f'A + B = {soma}')

    #Verificação de condição (Se soma de A+B é menor que C) e impressão do resultado
    if soma < C:
        print('O resultado da soma é menor que C.')
    else:
        print('O resultado da soma é maior que C.')

def exercicio_2():
    #Exercício - 2
    print('Exercício - 2')

    #Requerimento dos dados de A e B
    A = int(input('Digite o valor para A: '))
    B = int(input('Digite o valor para B: '))

    #Verificação se A e B são iguais e impressão do resultado
    if A == B:
        C = A + B
    else:
        C = A * B

    print(f'O valor de C é: {C}')

def exercicio_3():
    #Exercício - 3
    print('Exercício - 3')
    #Requerimento do número ao usuário
    numero = int(input('Digite um número inteiro: '))

    #Calculo de antecessor e sucessor e impressão do resultado
    antecessor = numero - 1
    sucessor = numero + 1

    print(f'O antecessor de {numero} é {antecessor}.\n O sucessor de {numero} é {sucessor}.')

def exercicio_4():
    #Exercício - 4
    print('Exercício - 4')
    #Requerimento dos dados
    salario_minimo = 1412.00
    print(f'O valor do salário minímo atual é: {salario_minimo:.2f}')
    salario_usuario = float(input('Digite o valor do seu salário: '))

    #Calculo de quantos salários minimos o usuário recebe e impressão do resultado
    quantidade_salarios_minimos = salario_usuario / salario_minimo
    print(f'Você recebe {quantidade_salarios_minimos:.2f} salários minímos')

def exercicio_5():
    #Exercício - 5
    print('Exercício - 5')
    #Requerimento de dados
    valor = float(input('Digite um valor: '))

    #Calculo do reajuste e impressão do resultado
    reajuste = valor * 0.05
    valor_reajustado = reajuste + valor

    print(f'O valor reajustado em 5% é: {valor_reajustado:.2f}')

def exercicio_6():
    #Exercício - 6
    print('Exercício - 6')
    #Requerimento dos dados
    numero_1 = int(input('Digite um número inteiro: '))
    numero_2 = int(input('Digite outro número inteiro: '))

    #Definição de qual número é maior e impressão do resultado
    if numero_1 > numero_2:
        print(f'O maior número é: {numero_1}')
    elif numero_2 > numero_1:
        print(f'O maior número é: {numero_2}')
    else:
        print('Os dois números são iguais')

def exercicio_7():
    #Exercício - 7
    while True:
        print('Exercício - 7')
        #Requerimento dos dados
        valor_1 = int(input('Digite o primeiro número inteiro: '))
        valor_2 = int(input('Digite o segundo número inteiro: '))
        valor_3 = int(input('Digite o terceiro número inteiro: '))

        #Verificação dos valores
        if valor_1 == valor_2 or valor_1 == valor_3 or valor_2 == valor_3:
            input('Os números inteiros não podem ser iguais entre si. Pressione ENTER, e tente novamente.')
            limpar_terminal()
        else:
        #Colocando os valores em lista, ordenando e imprimindo resultado
            valores = [valor_1, valor_2, valor_3]
            valores.sort(reverse=True)
            print('Os números inteiros em ordem decrescente são:')
            for lista in valores:
                print(lista)
            break

def exercicio_8():
    #Exercício - 8
    print('Exercicio - 8')
    #Requerimento de dados
    num_1 = float(input('Digite o primeiro número: '))
    num_2 = float(input('Digite o terceiro número: '))
    num_3 = float(input('Digite o segundo número: '))

    #Calculo da média e impressão do resultado
    media = (num_1 + num_2 + num_3) / 3

    print('A média aritmética dos números é:', media)

def exercicio_9():
    #Exercicio - 9
    print('Exercicio - 9')
    #Requerimento dos dados
    while True: 
    #Loop em caso de erro do usuario digitando numero negativo

        numero_int = int(input('Digite um número inteiro não negativo: '))

    #Verificação do número
        if numero_int >= 0:
            break #Finaliza o loop caso o número seja positivo.
        else:
            input("Aperte ENTER e digite um número inteiro não negativo.")
            limpar_terminal()

    #Inicializa fatorial como 1
    fatorial = 1

    #Caso digite o número 0, o fatorial de 0 é 1
    if numero_int == 0:
        print('O fatorial de 0 é 1')
    else:
        #Calculo do fatorial e impressão do resultado
        for i in range(1, numero_int + 1):
            fatorial *= i
        print(f'O fatorial de {numero_int} é {fatorial}')

def exercicio_10():
    #Exercicio - 10
    print('Exercicio - 10')
    #Requerimento dos dados do usuario
    numero_primo = int(input('Digite um número inteiro positivo: '))

    #Verifica se o número é menor que 2
    if numero_primo <= 1:
        print(f'\n O {numero_primo} não é primo!')
    else:
    #Verifica todos os números de 2 até a raiz quadrada do numero + 1
        for i in range(2, int(numero_primo ** 0.5) + 1):
        #Se o número é divisivel por qualquer número entre 2 e a raiz quadrada dele, ele não é primo
            if numero_primo % i == 0:
                print(f'O {numero_primo} não é primo!')
                break
        else:
        #Se não foi encontrado nenhum divisor entre 2 e a raiz quadrada do número, ele é primo
            print(f'O {numero_primo} é primo!')

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
        print("║ 5. Exercício 5              ║")
        print("║ 6. Exercício 6              ║")
        print("║ 7. Exercício 7              ║")
        print("║ 8. Exercício 8              ║")
        print("║ 9. Exercício 9              ║")
        print("║ 10. Exercício 10            ║")
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
        elif escolha == '5':
            limpar_terminal()
            exercicio_5()
        elif escolha == '6':
            limpar_terminal()
            exercicio_6()
        elif escolha == '7':
            limpar_terminal()
            exercicio_7()
        elif escolha == '8':
            limpar_terminal()
            exercicio_8()
        elif escolha == '9':
            limpar_terminal()
            exercicio_9()
        elif escolha == '10':
            limpar_terminal()
            exercicio_10()
        elif escolha == '0':
            break
        else:
            input("Opção inválida! Pressione ENTER para tentar novamente.")

        input('Aperte ENTER para limpar a tela!')
        limpar_terminal()

menu()