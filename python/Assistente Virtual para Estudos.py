import datetime

class AssistenteEstudos:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, data_entrega):
        self.tarefas.append({'descricao': descricao, 'data_entrega': data_entrega, 'concluida': False})

    def mostrar_tarefas(self):
        for tarefa in self.tarefas:
            print(f"{tarefa['descricao']} - Data de Entrega: {tarefa['data_entrega']} - Concluída: {tarefa['concluida']}")

# Exemplo de uso
assistente = AssistenteEstudos()
assistente.adicionar_tarefa('Estudar Python', '2024-03-01')
assistente.mostrar_tarefas()
