def solicitar_nome():
    while True:
        nome = input("Digite o nome da pessoa: ")
        if nome.isalpha():
            return nome.capitalize()
        else:
            print("O nome deve conter apenas letras. Tente novamente.")

def solicitar_idade():
    while True:
        idade = input("Digite a idade da pessoa: ")
        if idade.isdigit():
            return int(idade)
        else:
            print("A idade deve conter apenas números. Tente novamente.")

# Solicita o nome e a idade da primeira pessoa
print("Primeira pessoa.")
nome1 = solicitar_nome()
idade1 = solicitar_idade()

# Solicita o nome e a idade da segunda pessoa
print("Segunda pessoa.")
nome2 = solicitar_nome()
idade2 = solicitar_idade()

# Verifica quem é mais velho
if idade1 > idade2:
    print(nome1, "é mais velho.")
elif idade2 > idade1:
    print(nome2, "é mais velho.")
else:
    print(nome1, "e", nome2, "têm a mesma idade.")
