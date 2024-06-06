def solicitar_nomes():
    while True:
        nome = input("Informe o nome: ")
        if nome.isalpha():
            return nome.capitalize
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