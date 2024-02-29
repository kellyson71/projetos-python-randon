class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

def main():
    ladoA = float(input("Digite a medida do lado A do local: "))
    ladoB = float(input("Digite a medida do lado B do local: "))

    local = Retangulo(ladoA, ladoB)

    area = local.calcularArea()
    perimetro = local.calcularPerimetro()

    print(f"\nÁrea do local: {area} metros quadrados")
    print(f"Perímetro do local: {perimetro} metros")

    qtd_pisos = area
    qtd_rodapes = perimetro * 0.1

    print(f"\nSerão necessários {qtd_pisos:.2f} pisos e {qtd_rodapes:.2f} metros de rodapé.")

if __name__ == "__main__":
    main()
