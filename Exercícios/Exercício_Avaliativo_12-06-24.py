# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

'''
Resolva as questões abaixo, usando lógica de programação

Variáveis e Condiçoês: if; elif; else; for; while

1 - Peça ao usuário para digitar uma quantidade de números, em seguida informe se o um número é positivo, negativo ou zero. Utilize a opção x para encerrar o programa.

2 - Peça ao usuário para digitar uma quantidade de números, em seguida informe se o um número é par ou ímpar. Utilize a opção x para encerrar o programa.

3 - Calcule a soma de todos os números de 1 a 100.

4 - Peça ao usuário para digitar um número e verifique se ele é par ou ímpar. Em seguida, exiba os primeiros 5 números ímpares.

5 - Peça ao usuário para digitar três números e exiba o menor deles. Em seguida, imprima os números de 1 até o menor número digitado pelo usuário, informando cada número, se é par ou ímpar.

6 - Solicite dois números ao usuário e mostre todos os números pares entre eles. Em seguida, some todos esses números pares e imprima o resultado calculado.

7 - Calcule a soma dos números impares de 01 a 100.

8 - Escreva um programa que advinhe um número secreto usando while, if, elif e else e pelo menos uma variável boleana.

9 - Escreva um programa onde fique dando um loop infinito até o usuário digitar X, mostre uma mensagem na tela indicando que o usuário parou o processamento.

10 - Digite um programa onde você deverá escrever o seu nome completo na tela, contar quantas vogais tem e quantas consoantes, indicando no final a quantidade de letras.
'''
def exercicio_1():
    print("Peça ao usuário para digitar uma quantidade de números, em seguida informe se o um número é positivo, negativo ou zero. Utilize a opção x para encerrar o programa.")
    
    # Entrada do usuario
    entrada = ""
    # Definição do loop até ser pressionado (X) para encerrar o programa
    while entrada.lower() != 'x':
        entrada = input("Informe um número ou digite [X] para encerrar o programa:  ")
        if entrada.lower() == 'x':
            print("O programa está encerrado!")
        else:
    # Definição se os números digitados são negativos ou positivos ou zero.
            if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):    
                numero = float(entrada)
                if numero > 0:
                    print(f"{numero} é um número positivo!")
                elif numero < 0:
                    print(f"{numero} é um número negativo!")
                elif numero == 0:
                    print(f"Este número é Zero!")
            else:
                print("Você não informou um número. Por favor digite novamente.")

def exercicio_2():
    print("Peça ao usuário para digitar uma quantidade de números, em seguida informe se o um número é par ou ímpar. Utilize a opção x para encerrar o programa.")

    # Entrada do usuario
    entrada = ""
    # Definição do loop até ser pressionado (X) para encerrar o programa
    while entrada.lower() != 'x':
        entrada = input("Informe um número ou digite [X] para encerrar o programa:  ")
        if entrada.lower() == 'x':
            print("O programa está encerrado!")
        else:
        # Definição se os números digitados são pares ou impares.
            if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
                numero = float(entrada)
                if numero % 2 == 0:
                    print(f"O número {numero} é par")
                else:
                    print(f"O número {numero} é impar")
            else:
                print("Você não informou um número por favor digite novamente.")

def exercicio_3():
    print("Calcule a soma de todos os números de 1 a 100.")

    # Entrada do usuario
    soma = 0
    for i in range(1, 101):
        soma += i
    # Print do resultado
    print(f"A soma de todos os números de 1 a 100 é: {soma}")

def exercicio_4():
    print("Peça ao usuário para digitar um número e verifique se ele é par ou ímpar. Em seguida, exiba os primeiros 5 números ímpares.")

    # Entrada do usuario
    numeroInt = int(input("Informe um número: "))
    
    # Verificação se é impar ou par
    if numeroInt % 2 == 0:
        print(f"O número {numeroInt} é par")
    else:
        print(f"O número {numeroInt} é impar")

    # Impressão dos números impares
    print("Os primeiros 5 números impares")
    for i in range(1, 10, 2):
        print(i)

def exercicio_5():
    print("Peça ao usuário para digitar três números e exiba o menor deles. Em seguida, imprima os números de 1 até o menor número digitado pelo usuário, informando cada número, se é par ou ímpar.")

    # Entrada do usuário
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    numero_3 = int(input("Digite o terceiro número: "))

    # Verifica o menor dos três números
    if numero_1 <= numero_2 and numero_1 <= numero_3:
        menor = numero_1
    elif numero_2 <= numero_1 and numero_2 <= numero_3:
        menor = numero_2
    else:
        menor = numero_3

    print(f"O menor número digitado é: {menor}")

    # Impressão dos resultados e informando se são par ou impar
    print(f"Os números de 1 até {menor} são:")
    for i in range(1, menor + 1):
        if i % 2 == 0:
            print(f"{i} é par")
        else:
            print(f"{i} é ímpar")

def exercicio_6():
    print("Solicite dois números ao usuário e mostre todos os números pares entre eles. Em seguida, some todos esses números pares e imprima o resultado calculado.")

    #Entrada do usuário
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    soma = 0
    
    # Verificação e impressão do resultado
    if numero_1 > numero_2:
        numero_1, numero_2 = numero_2 , numero_1
    for i in range(numero_1, numero_2 +1):
        if i % 2 == 0:
            print(f"{i} é par")
            soma += i

    print(f"A soma dos números é: {soma}")

def exercicio_7():
    print("Calcule a soma dos números impares de 1 a 100.")

    # Entrada do usuário
    soma = 0
    for i in range(1, 101):
        if i % 2 != 0:
            soma += i
    # Print do resultado
    print(f"A soma dos números impares de 1 a 100 é: {soma}")

def exercicio_8():
    print("Escreva um programa que advinhe um número secreto usando while, if, elif e else e pelo menos uma variável boleana.")

    # Criando aleatoriedade ao número secreto
    print("Para gerar o número secreto, siga as instruções abaixo:")
    Random_1 = int(input(" - Digite um número entre 1 e 100: "))
    Random_2 = int(input(" - Digite um número entre 1 e 40: "))
    Random_3 = int(input(" - Escolha entre 1 e 2: "))
    Random_4 = int(input(" - Informe um número inteiro entre 0 e 20: "))

    #Informação sobre numero secreto
    print("O número secreto poderá ser positivo ou negativo.")

    # Verificação se as entradas estão dentro das instruções
    if not (1 <= Random_1 <= 100 and 1 <= Random_2 <= 40 and Random_3 in [1, 2] and Random_4 in range(0, 21)):
        print("Por favor, insira valores válidos dentro dos intervalos especificados.")
    else:
        # Definindo valor inicial da variavel (numero_secreto)
        numero_secreto = 0

        # Verificando as condições e calculando o número secreto
        if Random_1 in range(1, 50) and Random_2 in range(1, 20):
            if Random_3 == 1 and Random_4 <= 10:
                numero_secreto = ((Random_1 * Random_3) + (Random_2 * Random_4)) * 2
            elif Random_3 == 2 and Random_4 > 10:
                numero_secreto = ((Random_1 * Random_3) - (Random_4 * Random_2)) + 10
            else:
                numero_secreto = ((Random_4 * Random_2) + (Random_1 * Random_3)) - 5
        elif Random_1 in range(1, 50) and Random_2 in range(21, 41):
            if Random_3 == 1 and Random_4 <= 10:
                numero_secreto = ((Random_1 * Random_3) + (Random_2 * Random_4)) * 3
            elif Random_3 == 2 and Random_4 > 10:
                numero_secreto = ((Random_1 * Random_3) + (Random_4 * Random_2)) // 2
            else:
                numero_secreto = ((Random_2 * Random_3) - (Random_4 * Random_1)) + 7
        elif Random_1 in range(51, 101) and Random_2 in range(1, 20):
            if Random_3 == 1 and Random_4 <= 10:
                numero_secreto = ((Random_1 * Random_3) + (Random_2 * Random_4)) * 4
            elif Random_3 == 2 and Random_4 > 10:
                numero_secreto = ((Random_1 * Random_3) - (Random_4 * Random_2)) // 3
            else:
                numero_secreto = ((Random_4 * Random_3) + (Random_1 * Random_2)) * 2
        elif Random_1 in range(51, 101) and Random_2 in range(21, 41):
            if Random_3 == 1 and Random_4 <= 10:
                numero_secreto = ((Random_1 * Random_3) - (Random_2 * Random_4)) * 5
            elif Random_3 == 2 and Random_4 > 10:
                numero_secreto = ((Random_1 * Random_3) + (Random_4 * Random_2)) // 4
            else:
                numero_secreto = ((Random_3 * Random_2) + (Random_4 * Random_1)) - 10
        else:
            numero_secreto = (Random_1 + Random_2 + Random_3 + Random_4) * 3

    acertou = False
    # Entrada do usuário para tentar encontrar o número secreto e impressão do resultado
    while acertou == False:
        chute = int(input("Qual será o número secreto? "))
        if chute < numero_secreto:
            print("Acho que você está abaixo.\nContinue tentando!")
        elif chute > numero_secreto:
            print("Hmm, acho que você está acima.\nTente de novo!")
        else:
            chute == numero_secreto
            print(f"PARABÉNS!\nO número secreto é {numero_secreto}.\nVocê acertou.")
            acertou = True

def exercicio_9():
    print("Escreva um programa onde fique dando um loop infinito até o usuário digitar X, mostre uma mensagem na tela indicando que o usuário parou o processamento.")
    
    # Entrada do usuário
    entrada = ""

    # Definição do loop até o usuário pressionar (x) para encerrar o processamento.
    while entrada.lower() != "x":
        entrada = input("Pressione qualquer tecla para continuar ou (X) para parar: ")
        if entrada.lower() == "x":
            print("Você parou o processamento.")

def exercicio_10():
    print("Digite um programa onde você deverá escrever o seu nome completo na tela, contar quantas vogais tem e quantas consoantes, indicando no final a quantidade de letras.")

    # Entrada do nome pelo usuário
    nome_completo = input("Informe seu nome completo: ")

    # Contagem de vogais, consoantes, e total de letra
    vogais = 0
    consoantes = 0
    total_letras = 0

    # Definição da quantidade vogais, consoantes, e total de letras
    for letra in nome_completo.lower():
        if letra in "aeiou":
            vogais += 1
            total_letras += 1
        elif letra in "bcdfghjklmnpqrstvxyz":
            consoantes += 1
            total_letras += 1
    
    # Impressão do resultado
    print(f" - Seu nome completo é: {nome_completo.title()}")
    print(f" - Seu nome contém: {vogais} vogais.")
    print(f" - Seu nome contém: {consoantes} consoantes.")
    print(f" - Seu nome contém: {total_letras} total de letras.")

# Menu de escolha dos Exercícios
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

        input('Aperte ENTER para voltar ao Menu de Exercícios.')
        limpar_terminal()

menu()