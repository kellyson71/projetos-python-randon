class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]

    def exibir_tarefas(self):
        if self.tarefas:
            print("Lista de Tarefas:")
            for indice, tarefa in enumerate(self.tarefas, start=1):
                print(f"{indice}. {tarefa}")
        else:
            print("Nenhuma tarefa na lista.")

# Exemplo de uso
lista_tarefas = ListaDeTarefas()

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nova_tarefa = input("Digite a nova tarefa: ")
        lista_tarefas.adicionar_tarefa(nova_tarefa)
    elif opcao == '2':
        if lista_tarefas.tarefas:
            lista_tarefas.exibir_tarefas()
            indice_remover = int(input("Digite o número da tarefa a ser removida: ")) - 1
            lista_tarefas.remover_tarefa(indice_remover)
        else:
            print("Não há tarefas para remover.")
    elif opcao == '3':
        lista_tarefas.exibir_tarefas()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
