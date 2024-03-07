import datetime

class RastreadorHabitos:
    def __init__(self):
        self.habitos = {}

    def adicionar_habito(self, habito):
        self.habitos[habito] = {'dias': set(), 'concluido': False}

    def marcar_concluido(self, habito, data):
        if habito in self.habitos:
            self.habitos[habito]['dias'].add(data)
            self.habitos[habito]['concluido'] = True

    def gerar_estatisticas(self):
        for habito, info in self.habitos.items():
            total_dias = len(info['dias'])
            print(f"{habito}: Concluído {total_dias} dias. Concluído: {info['concluido']}")

# Exemplo de uso
rastreador = RastreadorHabitos()
rastreador.adicionar_habito('Fazer exercícios')
rastreador.marcar_concluido('Fazer exercícios', '2024-02-23')
rastreador.gerar_estatisticas()
