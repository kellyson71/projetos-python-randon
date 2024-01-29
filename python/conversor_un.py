import tkinter as tk
from tkinter import messagebox

class ConversorUnidades:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Unidades")

        # Variáveis de controle
        self.valor_var = tk.DoubleVar()
        self.resultado_var = tk.StringVar()
        self.unidade_origem_var = tk.StringVar()
        self.unidade_destino_var = tk.StringVar()

        # Componentes da interface
        self.label_valor = tk.Label(root, text="Valor:")
        self.entry_valor = tk.Entry(root, textvariable=self.valor_var)

        self.label_unidade_origem = tk.Label(root, text="De:")
        self.entry_unidade_origem = tk.Entry(root, textvariable=self.unidade_origem_var)

        self.label_unidade_destino = tk.Label(root, text="Para:")
        self.entry_unidade_destino = tk.Entry(root, textvariable=self.unidade_destino_var)

        self.btn_converter = tk.Button(root, text="Converter", command=self.converter)

        self.label_resultado = tk.Label(root, textvariable=self.resultado_var)

        # Posicionamento dos componentes
        self.label_valor.grid(row=0, column=0, padx=10, pady=10)
        self.entry_valor.grid(row=0, column=1, padx=10, pady=10)

        self.label_unidade_origem.grid(row=1, column=0, padx=10, pady=10)
        self.entry_unidade_origem.grid(row=1, column=1, padx=10, pady=10)

        self.label_unidade_destino.grid(row=2, column=0, padx=10, pady=10)
        self.entry_unidade_destino.grid(row=2, column=1, padx=10, pady=10)

        self.btn_converter.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

    def converter(self):
        try:
            valor = float(self.valor_var.get())
            unidade_origem = self.unidade_origem_var.get().lower()
            unidade_destino = self.unidade_destino_var.get().lower()

            if unidade_origem == 'km' and unidade_destino == 'mi':
                resultado = valor * 0.621371
            elif unidade_origem == 'mi' and unidade_destino == 'km':
                resultado = valor / 0.621371
            else:
                messagebox.showwarning("Unidades Inválidas", "Conversão entre estas unidades não é suportada.")
                return

            self.resultado_var.set(f"Resultado: {resultado:.2f} {unidade_destino}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorUnidades(root)
    root.mainloop()
