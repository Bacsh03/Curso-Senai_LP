# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

#Exercício para fixação de Logica de Programação.

def exercicio_1():
    print("Exercício 1 - Calcule a média das notas para saber se foi aprovado ou reprovado.")

    while True: # Loop para previnir que o usuário digite dados errados.

        # Verificação se o usuário digitará apenas números entre 0 e 10.
        try:
            # Requisição de dados para o usuário.
            nota_1 = float(input("Digite sua primeira nota (valor de 0 a 10): "))
            if not 0 <= nota_1 <= 10:
                raise ValueError
            nota_2 = float(input("Digite sua segunda nota (valor de 0 a 10): "))
            if not 0 <= nota_2 <= 10:
                raise ValueError
            nota_3 = float(input("Digite sua terceira nota (valor de 0 a 10): "))
            if not 0 <= nota_3 <= 10:
                raise ValueError
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números de 0 a 10.") # Mensagem de erro em caso do usuário digitar algo fora do que foi pedido.
        else:
        # Verificação e processamento das notas para calcular média e impressão do resultado.
            soma_notas = nota_1 + nota_2 + nota_3
            media_notas = soma_notas/3
            if media_notas >= 7:
                print(f"A média de suas notas é: {media_notas:.2f}. Você está aprovado!")
            else:
                print(f"A média de suas notas é: {media_notas:.2f}. Você está reprovado!")        
            break  # Sair do loop.

def exercicio_2():
    print("Exercício 2 - Conversão de temperatura Celsius para Fahrenheit.")

    while True: # Loop para previnir que o usuário digite dados errados.

        # Verificação se o usuário digitará apenas números para a temperatura.
        try:
            # Requisição dos dados ao usuário.
            celsius = float(input("Digite a temperatura em Celsius: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números para a temperatura.")
        else:
            # Calculo da conversão e impressão do resultado.
            fahrenheit = (celsius * 9/5) + 32 
            print(f"{celsius:.2f} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
            break # Sair do loop.

def exercicio_3():
    print("Exercício 3 - Verificação se número inteiro é positivo, negativo, ou zero.")

    while True: #Loop para previnir que o usuário digite dados errados.
    
        # Verificação se o usuário digitará apenas números inteiros
        try:
            # Requisição dos dados ao usuário.
            numero_int = int(input("Digite um número inteiro: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números inteiros.")
        else:
            # Verificação dos dados e impressão do resultado.
            if numero_int > 0:
                print(f"{numero_int} é um número inteiro positivo.")
            elif numero_int == 0:
                print(f"{numero_int} é zero.")
            else:
                print(f"{numero_int} é um número inteiro negativo.")
            break # Sair do loop.

def exercicio_4():
    print("Exercício 4 - Calculo de aumento de salário")

    while True: # Loop para previnir que o usuário digite dados errados.

        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            salario_atual = float(input("Digite seu salário atual: "))
            aumento_salario = float(input("Digite o valor a ser acrescentado ao salário: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números.")
        else:
            # Soma dos dados e impressão do resultado.
            novo_salario = salario_atual + aumento_salario
            print(f"O seu novo salário será de: {novo_salario}")
            break # Sair do loop.

def exercicio_5():
    print("Exercício 5 - Verificação de se é maior de idade ou menor de idade")

    while True: # Loop para previnir que o usuário digite dados errados.

        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            idade = int(input("Digite sua idade: "))
        except  ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números inteiros para idade.")
        else:
            # Verificação da idade e impressão do resultado.
            if idade >= 18:
                print(f"Sua idade é: {idade} anos. Você é maior de idade!")
            else:
                print(f"Sua idade é: {idade} anos. Você é menor de idade!")
            break

def exercicio_6():
    print("Exercício 6 - Verificação do maior número.")

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

def exercicio_7():
    print("Exercício 7 - Calculo de IMC")

    while True: # Loop para previnir que o usuário digite dados errados.
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            peso = float(input("Informe seu peso em kg: "))
            altura = float(input("Informe sua altura em metros: "))
            
            # Condição para previnir entrada do número zero em peso e altura.
            if altura <= 0 or peso <= 0:
                raise ValueError
            
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números maiores que zero para peso e altura.")
        else:
            # Calculo do IMC.
            imc = peso/(altura * altura)
            # Verificação do IMC.
            if imc < 18.5:
                print(f"Seu IMC é: {imc:.2f}. Você está abaixo do peso.")
            elif imc < 24.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com peso normal.")
            elif imc < 29.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com sobrepeso.")
            elif imc < 39.9:
                print(f"Seu IMC é: {imc:.2f}. Você está com obesidade.")
            else:
                print(f"Seu IMC é: {imc:.2f}. Você está com obesidade mórbida.")
            break # Saindo do Loop

def exercicio_8():
    print("Exercício 8 - Realizar operações básicas.")

    while True: # Loop para previnir que o usuário digite dados errados.
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            numero_1 = int(input("Informe o primeiro número: "))
            numero_2 = int(input("Informe o segundo número: "))
            # Previnindo erro de divisão por zero.
            if numero_2 == 0:
                raise ZeroDivisionError 
            # Realizando as operações e imprimindo resultado.
            soma = numero_1 + numero_2
            print(f"O resultado da soma dos dois números é: {soma}")
            subtracao = numero_1 - numero_2
            print(f"O resultado da subtração dos dois números é: {subtracao}")
            multiplicacao = numero_1 * numero_2
            print(f"O resultado da multiplicação dos dois números é: {multiplicacao}")
            divisao = numero_1 / numero_2
            print(f"O resultado da divisão dos dois números é: {divisao}")
            break # Saindo do Loop.

        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números.")
        except ZeroDivisionError:
            print("Erro de divisão por zero. Por favor digite um número diferente de zero para o segundo número.")

def exercicio_9():
    print("Exercício 9 - Classificando como bebê, criança, adolescente, adulto ou idoso de acordo com a idade.")

    while True: # Loop para previnir que o usuário digite dados errados.
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            idade = int(input("Informe a idade: "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor digite apenas números para informar sua idade.")
        else:
            # Verificação da idade e classificando de acordo como (bebê, criança, adolescente, adulto, idoso).
            if idade <= 2:
                print(f"A idade informada é: {idade}. Você é um bebê")
            elif idade <= 12:
                print(f"A idade informada é: {idade}. Você é uma criança.")
            elif idade <= 17:
                print(f"A idade informada é: {idade}. Você é um adolescente.")
            elif idade <= 64:
                print(f"A idade informada é: {idade}. Você é um adulto.")
            else:
                print(f"A idade informada é: {idade}. Você é um idoso.")
            break # Saindo do Loop.

def exercicio_10():
    print("Exercício 10 - Formando um triângulo e classificando como equilátero, isósceles ou escaleno.")

    while True: # Loop para previnir que o usuário digite dados errados.
        try:
            #Requisição dos dados.
            lado_1 = float(input("Informe o primeiro lado do triângulo em (cm): "))
            lado_2 = float(input("Informe o segundo lado do triângulo em (cm): "))
            lado_3 = float(input("Informe o terceiro lado do triângulo em (cm): "))
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor, insira um número valído.")
        else:
            # Verificação se os numeros podem formar um triângulo
            if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
                # Verificar o tipo de triângulo
                if lado_1 == lado_2 == lado_3:
                    print("Os lados formam um triângulo equilátero.")
                elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
                    print("Os lados formam um triângulo isósceles.")
                else:
                    print("Os lados formam um triângulo escaleno.")
                break
            else:
                print("Não é possível formar um triângulo com esses lados informados.")
     
def exercicio_11():
    print("Exercício 11 - Calculo valor de produto com desconto.")

    while True: # Loop para previnir que o usuário digite dados errados.
        # Verificação se o usuário digitará apenas números.
        try:
            # Requisição dos dados ao usuário.
            preco_atual = float(input("Informe o valor atual do produto: "))
            desconto_produto = float(input("Informe o desconto desejado em (%): "))
            # Indicando que o valor do desconto tem de estar entre 0 e 100.
            if desconto_produto < 0 or desconto_produto > 100:
                raise ValueError
            
            #Calculo do preço final com desconto.
            preco_final = preco_atual * (1 - desconto_produto / 100)
            print(f"O valor ajustado do produto com desconto é: R${preco_final:.2f}")
            
        except ValueError: # Mensagem de erro informada caso usuário digite algo fora do que foi pedido.
            print("Por favor informe somente números para o valor e desconto.")
        break
            
def exercicio_12():
    print("Exercício 12 - Definir quem é mais velho entre duas pessoas.")

    # Definição para as variaveis de nome conterem apenas letras.
    def solicitar_nomes():
        while True:
            nome = input("Informe o nome: ")
            if nome.isalpha():
                return nome.capitalize()
            else:
                print("O nome deve conter apenas letras. Por favor informe novamente.")

    # Definição para as variaveis de idade conterem apenas números.
    def solicitar_idades():
        while True:
            idade = input("Informe a idade: ")
            if idade.isdigit():
                return int(idade)
            else:
                print("A idade deve conter apenas números. Por favor informe novamente.")

    # Solicitação dos dados
    print("Dados da primeira pessoa.")
    nome_1 = solicitar_nomes()
    idade_1 = solicitar_idades()

    print("Dados da segunda pessoa.")
    nome_2 = solicitar_nomes()
    idade_2 = solicitar_idades()

    # Verificação de quem é mais velho, e impressão do resultado.
    if idade_1 > idade_2:
        print(f"{nome_1} é mais velho que {nome_2}.")
    elif idade_2 > idade_1:
        print(f"{nome_2} é mais velho que {nome_1}.")
    else:
        print(f"{nome_1} e {nome_2} tem a mesma idade.")
            
def exercicio_13():
    print("Exercício 13 - Calcular valor de troco em uma compra.")

    while True: # Loop para previnir que o usuário digite dados errados.
        # Verificação se o usuário digitará apenas números.
        try:
            valor_compra = float(input("Informe o valor da compra: "))
            valor_pago = float(input("Informe o valor pago: "))
        except ValueError:
            print("Por favor insira somente números.")

        if valor_pago > valor_compra:
            troco_compra = valor_pago - valor_compra
            print(f"O troco da sua compra é: R${troco_compra:.2f}!")
        elif valor_compra > valor_pago:
            troco_compra = valor_compra - valor_pago
            print(f"Está faltando: R${troco_compra:.2f}!")
        else:
            print("Você não tem troco a receber.")
        break

# Menu de Exercícios
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
        print("║ 11. Exercício 11            ║")
        print("║ 12. Exercício 12            ║")
        print("║ 13. Exercício 13            ║")
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
        elif escolha == '11':
            limpar_terminal()
            exercicio_11()
        elif escolha == '12':
            limpar_terminal()
            exercicio_12()
        elif escolha == '13':
            limpar_terminal()
            exercicio_13()
        elif escolha == '0':
            limpar_terminal()
            break
        else:
            input("Opção inválida! Pressione ENTER para tentar novamente.")

        input('Aperte ENTER para voltar ao Menu de Exercícios.')
        limpar_terminal()

menu()