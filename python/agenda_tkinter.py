import tkinter as tk
from tkinter import messagebox
import csv

class AgendaContatos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contatos")

        # Lista para armazenar os contatos
        self.contatos = []

        # Componentes da interface
        self.label_nome = tk.Label(root, text="Nome:")
        self.entry_nome = tk.Entry(root)

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.entry_telefone = tk.Entry(root)

        self.btn_adicionar = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato)
        self.btn_listar = tk.Button(root, text="Listar Contatos", command=self.listar_contatos)

        # Posicionamento dos componentes
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefone.grid(row=1, column=0, padx=10, pady=10)
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=10)

        self.btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)
        self.btn_listar.grid(row=3, column=0, columnspan=2, pady=10)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()

        if nome and telefone:
            contato = {"Nome": nome, "Telefone": telefone}
            self.contatos.append(contato)
            self.limpar_campos()
            messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    def listar_contatos(self):
        if not self.contatos:
            messagebox.showinfo("Lista de Contatos", "A agenda está vazia.")
        else:
            lista_contatos = "\n".join([f"{contato['Nome']}: {contato['Telefone']}" for contato in self.contatos])
            messagebox.showinfo("Lista de Contatos", lista_contatos)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaContatos(root)
    root.mainloop()
