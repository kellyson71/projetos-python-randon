class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
