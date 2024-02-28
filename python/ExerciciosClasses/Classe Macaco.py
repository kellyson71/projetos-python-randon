class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if self.bucho:
            alimento_digerido = self.bucho.pop(0)
            print(f"{self.nome} digeriu {alimento_digerido}.")
        else:
            print(f"{self.nome} está com fome.")

macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Nozes")

macaco2.comer("Peixe")
macaco2.comer("Folhas")
macaco2.comer("Insetos")

print("Bucho do Macaco1:", macaco1.verBucho())
print("Bucho do Macaco2:", macaco2.verBucho())

macaco1.digerir()
macaco2.digerir()

print("Bucho do Macaco1 após a digestão:", macaco1.verBucho())
print("Bucho do Macaco2 após a digestão:", macaco2.verBucho())
