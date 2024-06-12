# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

'''
Exercícios
1 - Faça um programa que receba dois números e mostre qual deles é o maior.

2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.

3 - Leia um número real. Se o número for positivo imprima a raiz quadrada. do contrário, imprima o número ao quadrado.

4 - Faça um programa que leia um número e, caso ele seja positivo, calcula e mostre:
    * O número digitado ao quadrado
    * A raiz quadrada do número digitado

5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
'''

def exercicio_1():
    print("Mostre o maior número entre os digitados.")

# Definição dos números
    numero_1 = float(input("Informe o 1º número: "))
    numero_2 = float(input("Informe o 2º número: "))

#Impressão do número maior
    resultado = max(numero_1, numero_2)
    print(f"O maior número entre {numero_1} e {numero_2} é: {resultado}")

def exercicio_2():
    print("Calcular raiz de um número positivo ou informar que um número negativo é invalido")

# Definição do número pelo usuário
    numero = float(input("Informe o número a ser verificado: "))

# Definição se vai calcular a raiz ou informar erro
    if numero > 0:
        raiz_quadrada = (numero ** (1/2))
        print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
    else:
        print("Este é um número invalido.")

def exercicio_3():
    print("Imprimir uma raiz quadrada de um número ou ele elevado quadrado")

# Definição do número
    numeroReal = float(input("Informe um número real: "))

# Definição do calculo
    if numeroReal > 0:
        raiz_quadrada = (numeroReal ** (1/2))
        print(f"A raiz quadrada de {numeroReal} é: {raiz_quadrada}")
    else:
        numeroQuadrado = (numeroReal ** 2)
        print(f"O {numeroReal} ao quadrado é: {numeroQuadrado:.2f}")


def exercicio_4():
    print("Mostrar um número ao quadrado e sua raiz caso seja positivo")

# Definição do número pelo usuário
    numero = float(input("Informe um número: "))

# Classificação do número informado e impressão do resultado
    if numero > 0:
        raiz_quadrada = (numero ** (1/2))
        numeroQuadrado = (numero ** 2)
        print(f"O número {numero} ao quadrado é: {numeroQuadrado:.2f}")
        print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
    else:
        print(f"O número {numero} não é positivo.")

def exercicio_5():
    print("Verificar se número inteiro é par ou impar")

# Definição do número pelo usuário
    numeroInt = int(input("Digite um número inteiro: "))

# Classificação se o número digitado é par ou impar
    if numeroInt % 2 == 0:
        print(f"O número {numeroInt} é par")
    else:
        print(f"O número {numeroInt} é impar")

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
        else:
            input("Opção inválida! Pressione ENTER para tentar novamente.")

        input('Aperte ENTER para voltar ao Menu de Exercícios.')
        limpar_terminal()

menu()