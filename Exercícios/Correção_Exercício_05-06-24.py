# Limpar tela após cada exercício
import os

def limpar_terminal():
    os.system('cls')
limpar_terminal()

'''
Atividade de Logica de Programação feito a mão em uma folha. 
Aqui estará a verificação e correção do codigo feito a mão.

Exercício 1 - Uma empresa precisa pagar 10% de imposto sobre seu faturamento como ISS. Além disso, sobre o lucro da empresa, ela precisa pagar 20% de IR e 5% de CSLL. Qual o total de imposto a ser pago em um mês que a empresa tenha R$ 5000 de faturamento e R$ 1000 de lucro?

Exercício 2 - Sua empresa vende 5 produtos, Iphone, Ipad, Airpod, Macbook, e Apple Watch. Mês passado ela vendeu, 1000, 300, 200, 50, 250 unidades de cada respectivamente. Qual foi o total de produtos vendidos e quantas unidades vendeu o produto mais vendido?

Exercício 3 - Contar a quantidade de vogais em uma palavra: Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra.

Exercício 4 - 
def __________ (palavra):
    _______ = "aeiou"
    return len ([letra for letra in palavra.lower() if letra in vogais])

# Exemplo de uso:
palavra_exemplo = "desenvolvimento"
quantidade_______ = __________(palavra_exemplo)
print(f"A palavra '{palavra_exemplo}' tem {quantidade_vogais} vogais.")

No programa acima está faltando três variáveis, complete e diga o que vai imprimir na tela do usuário.
'''
def exercicio_1():
    print("Calculo imposto sobre faturamento e lucro")

    faturamento = 5000
    lucro = 1000
    imposto_iss = (10/100) * 5000
    imposto_ir = (20/100) * 1000
    imposto_csll = (5/100) * 1000
    soma_imposto = imposto_iss + imposto_ir + imposto_csll
    print(f"O imposto ISS é: {imposto_iss}")
    print(f"O imposto IR é: {imposto_ir}")
    print(f"O imposto CSLL é: {imposto_csll}")
    print(f"O total dos impostos é: {soma_imposto}")

def exercicio_2():
    print("Calculo total de produtos vendidos e produto mais vendido")

    iphone = 1000
    ipad = 300
    airpod = 200
    macbook = 50
    apple_watch = 250

    total_vendas = iphone + ipad + airpod + macbook + apple_watch
    print(f"O total de vendas foi: {total_vendas}")

    maior_venda = max(iphone, ipad, airpod, macbook, apple_watch)
    print(f"O produto com maior venda é: {maior_venda}")

def exercicio_3():
    print("Contar quantidade de vogais")

    def contar_vogais(palavra):
        vogais = "aeiou"
        return len([letra for letra in palavra.lower() if letra in vogais])
    # Exemplo de uso:
    palavra_exemplo = "desenvolvimento"
    quantidade_vogais = contar_vogais(palavra_exemplo)
    print(f"A palavra '{palavra_exemplo}' tem {quantidade_vogais} vogais.")

def exercicio_4():
    print("Completar programa e dizer o que será impresso")
    
    def contar_vogais(palavra):
        vogais = "aeiou"
        return len([letra for letra in palavra.lower() if letra in vogais])
    palavra_exemplo = "desenvolvimento"
    quantidade_vogais = contar_vogais(palavra_exemplo)
    print(f"A palavra '{palavra_exemplo}' tem {quantidade_vogais} vogais.")
          
          # Será impresso: A palavra 'desenvolvimento' tem 6 vogais


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