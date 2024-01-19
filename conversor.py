def converter_unidades(valor, unidade_origem, unidade_destino):
    fator_conversao = {
        ('km', 'mi'): 0.621371,
        ('C', 'F'): lambda c: c * 9/5 + 32,
    }

    try:
        if unidade_origem == 'C' and unidade_destino == 'F':
            resultado = fator_conversao[unidade_origem, unidade_destino](valor)
        else:
            resultado = valor * fator_conversao[unidade_origem, unidade_destino]
        return resultado
    except KeyError:
        return "Conversão não suportada."

valor_convertido = converter_unidades(20, 'km', 'mi')
print(f"20 km é aproximadamente {valor_convertido:.2f} milhas.")
