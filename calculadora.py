import math
import tkinter as tk
from tkinter import messagebox

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(x)

def calcular():
    escolha = choice_var.get()

    try:
        num1 = float(entry_num1.get())

        if escolha != '6':
            num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida. Por favor, digite um número.")
        return

    try:
        if escolha == '1':
            resultado = adicionar(num1, num2)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
        elif escolha == '4':
            resultado = dividir(num1, num2)
        elif escolha == '5':
            resultado = potencia(num1, num2)
        elif escolha == '6':
            resultado = raiz_quadrada(num1)

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

def fechar_calculadora():
    root.destroy()

root = tk.Tk()
root.title("Calculadora")

choice_var = tk.StringVar()
choice_var.set('1')  
label_num1 = tk.Label(root, text="Digite o primeiro número:")
entry_num1 = tk.Entry(root)

label_num2 = tk.Label(root, text="Digite o segundo número:")
entry_num2 = tk.Entry(root)

label_operacao = tk.Label(root, text="Selecione a operação:")
menu_operacao = tk.OptionMenu(root, choice_var, '1', '2', '3', '4', '5', '6')

button_calcular = tk.Button(root, text="Calcular", command=calcular)
label_resultado = tk.Label(root, text="Resultado:")

button_sair = tk.Button(root, text="Sair", command=fechar_calculadora)

label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)

label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)

label_operacao.grid(row=2, column=0)
menu_operacao.grid(row=2, column=1)

button_calcular.grid(row=3, column=0, columnspan=2)
label_resultado.grid(row=4, column=0, columnspan=2)

button_sair.grid(row=5, column=0, columnspan=2)

root.mainloop()
