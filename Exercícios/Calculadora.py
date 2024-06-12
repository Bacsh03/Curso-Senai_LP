#Importando toda a biblioteca TKinter
from tkinter import *

#Estrutura da janela
calculadora = Tk()
calculadora.title("Calculadora - Victor Augusto")
calculadora.geometry('475x500+450+50')
calculadora.config(bg = '#0f132a')
calculadora.resizable(width = False, height = False)

# Funções para ativar botões
def btNumeros(numero):
    if numero == '.' and '.' in entrada.get():
        return
    clickBt = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(clickBt) + str(numero))
    return

def limpaEntrada():
    entrada.delete(0, END)
    return

def soma():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'soma'
    entrada.delete(0, END)
    return

def subtracao():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'subtracao'
    entrada.delete(0, END)
    return

def multiplicacao():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'multiplicacao'
    entrada.delete(0, END)
    return

def divisao():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'divisao'
    entrada.delete(0, END)
    return

def porcentagem():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'porcentagem'
    entrada.delete(0, END)
    return

def potencia():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'potencia'
    entrada.delete(0, END)
    return

def raiz():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    global primeiroNumero
    global operacao
    primeiroNumero = float(clickBt)
    operacao = 'raiz'
    entrada.delete(0, END)
    return

def igual():
    clickBt = entrada.get()
    if clickBt == "":
        entrada.insert(0, "")
        return
    entrada.delete(0, END)
    try:
        if operacao == 'soma':
            entrada.insert(0, primeiroNumero + float(clickBt))
        elif operacao == 'subtracao':
            entrada.insert(0, primeiroNumero - float(clickBt))
        elif operacao == 'multiplicacao':
            entrada.insert(0, primeiroNumero * float(clickBt))
        elif operacao == 'divisao':
            if float(clickBt) == 0:
                entrada.insert(0, "Erro: Divisão por 0")
            else:
                entrada.insert(0, primeiroNumero / float(clickBt))
        elif operacao == 'porcentagem':
            entrada.insert(0, (primeiroNumero * float(clickBt)) /100)
        elif operacao == 'potencia':
            entrada.insert(0, primeiroNumero ** float(clickBt))
        elif operacao == 'raiz':
            entrada.insert(0, primeiroNumero ** (1/2))
    except ValueError:
        entrada.insert(0, "")
    return
    

#entry (caixa de texto)
entrada = Entry(calculadora, width = 30, font=('OCR A Extended', 14), bg ='#1c3655', fg='#ffffff')
entrada.place(x = 75, y = 25)

#Botões
Bt1 = Button(calculadora, text='1', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(1))
Bt1.place(x = 50, y = 150)

Bt2 = Button(calculadora, text='2', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(2))
Bt2.place(x = 150, y = 150)

Bt3 = Button(calculadora, text='3', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(3))
Bt3.place(x = 250, y = 150)

Bt4 = Button(calculadora, text='4', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(4))
Bt4.place(x = 50, y = 225)

Bt5 = Button(calculadora, text='5', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(5))
Bt5.place(x = 150, y = 225)

Bt6 = Button(calculadora, text='6', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(6))
Bt6.place(x = 250, y = 225)

Bt7 = Button(calculadora, text='7', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(7))
Bt7.place(x = 50, y = 300)

Bt8 = Button(calculadora, text='8', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(8))
Bt8.place(x = 150, y = 300)

Bt9 = Button(calculadora, text='9', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(9))
Bt9.place(x = 250, y = 300)

Bt0 = Button(calculadora, text='0', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros(0))
Bt0.place(x = 50, y = 375)

BtPonto = Button(calculadora, text='.', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=lambda : btNumeros('.'))
BtPonto.place(x = 150, y = 375)

BtIgual = Button(calculadora, text='=', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=igual)
BtIgual.place(x = 250, y = 375)

BtDivisao = Button(calculadora, text='÷', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=divisao)
BtDivisao.place(x = 350, y = 150)

BtMultiplicacao = Button(calculadora, text='*', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=multiplicacao)
BtMultiplicacao.place(x = 350, y = 225)

BtSoma = Button(calculadora, text='+', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=soma)
BtSoma.place(x = 350, y = 300)

BtSubtracao = Button(calculadora, text='-', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=subtracao)
BtSubtracao.place(x = 350, y = 375)

BtC = Button(calculadora, text='C', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=limpaEntrada)
BtC.place(x = 50, y = 75)

BtPorcentagem = Button(calculadora, text='%', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=porcentagem)
BtPorcentagem.place(x = 150, y = 75)

BtPotencia = Button(calculadora, text='xⁿ', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=potencia)
BtPotencia.place(x = 250, y = 75)

BtRaiz = Button(calculadora, text='√', relief=FLAT, width=7, height=2, font=('OCR A Extended', 14), bg='#1c3655', fg='#ffffff', command=raiz)
BtRaiz.place(x = 350, y = 75)

# Texto informativo
criadoPor = Label(calculadora, text='Desenvolvido por Victor Augusto', font=('OCR A Extended', 14), bg ='#1c3655', fg='#ffffff')
criadoPor.place(x=65, y=455)

calculadora.mainloop()