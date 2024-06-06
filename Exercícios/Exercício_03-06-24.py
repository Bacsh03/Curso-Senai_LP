# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

#Exercício em sala dia 03/06/24

def exercicio_1():
    #01- Verificar se uma letra é vogal ou consoante:
    print("Verificação de vogal ou consoante")
    #Definição para aceitar que o usuario digite somente letras.
    letra = input("Digite uma letra: ").lower()
    if letra.isalpha():
        if letra in "a, e, i, o, u":
            print("É uma vogal.")
        else:
                print("É uma consoante.")
    else:
        print("Por favor insira apenas letras")
def exercicio_2():
    #02 - Verificar maior número
    while True: # Loop para previnir que o usuário digite dados errados.
        
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            primeiro_numero = int(input("Informe o primeiro número: "))
            segundo_numero = int(input("Informe o segundo número: "))
            terceiro_numero = int(input("Informe o terceiro número: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números.")
        else:
            # Verificação dos números e impressão do resultado.
            maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
            print(f"O maior número entre os informados é: {maior_numero}")
            break
def exercicio_3():
    #03 - Verificar maior e menor número.
    while True: # Loop para previnir que o usuário digite dados errados.
        
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            primeiro_numero = int(input("Informe o primeiro número: "))
            segundo_numero = int(input("Informe o segundo número: "))
            terceiro_numero = int(input("Informe o terceiro número: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números.")
        else:
            # Verificação dos números e impressão do resultado.
            maior_numero = max(primeiro_numero, segundo_numero, terceiro_numero)
            print(f"O maior número entre os informados é: {maior_numero}")
            menor_numero = min(primeiro_numero, segundo_numero, terceiro_numero)
            print(f"O menor número entre os informados é: {menor_numero}")
            break
def exercicio_4():
    #04 - Trocar valor de duas variaveis.
    while True: # Loop para previnir que o usuário digite dados errados.

        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            numero_1 = int(input("Informe o primeiro número: "))
            numero_2 = int(input("Informe o segundo número: "))

        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
                print("Por favor digite apenas números.")
            # Troca das variáveis
        troca = numero_1
        numero_1 = numero_2
        numero_2 = troca
            # Impressão do resultado
        print("O primeiro número agora é:", numero_1)
        print("O segundo número agora é:", numero_2)
        break

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
        elif escolha == '0':
            break
        else:
            input("Opção inválida! Pressione ENTER para tentar novamente.")

        input('Aperte ENTER para voltar ao Menu de Exercícios.')
        limpar_terminal()

menu()