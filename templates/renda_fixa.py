import tkinter as tk
from tkinter import messagebox

class SimuladorRendaFixa:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Renda Fixa")

        # Variáveis de controle
        self.principal_var = tk.DoubleVar()
        self.taxa_var = tk.DoubleVar()
        self.periodo_var = tk.IntVar()

        # Componentes da interface
        self.label_principal = tk.Label(root, text="Principal:")
        self.entry_principal = tk.Entry(root, textvariable=self.principal_var)

        self.label_taxa = tk.Label(root, text="Taxa de Juros (% ao ano):")
        self.entry_taxa = tk.Entry(root, textvariable=self.taxa_var)

        self.label_periodo = tk.Label(root, text="Período (anos):")
        self.entry_periodo = tk.Entry(root, textvariable=self.periodo_var)

        self.btn_simular = tk.Button(root, text="Simular", command=self.simular)

        # Posicionamento dos componentes
        self.label_principal.grid(row=0, column=0, padx=10, pady=10)
        self.entry_principal.grid(row=0, column=1, padx=10, pady=10)

        self.label_taxa.grid(row=1, column=0, padx=10, pady=10)
        self.entry_taxa.grid(row=1, column=1, padx=10, pady=10)

        self.label_periodo.grid(row=2, column=0, padx=10, pady=10)
        self.entry_periodo.grid(row=2, column=1, padx=10, pady=10)

        self.btn_simular.grid(row=3, column=0, columnspan=2, pady=10)

    def simular(self):
        try:
            principal = float(self.principal_var.get())
            taxa_juros = float(self.taxa_var.get()) / 100
            periodo = int(self.periodo_var.get())

            resultado = principal * (1 + taxa_juros) ** periodo

            messagebox.showinfo("Resultado", f"O montante ao final do período será: R$ {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha os campos corretamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorRendaFixa(root)
    root.mainloop()
