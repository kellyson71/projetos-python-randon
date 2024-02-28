from PIL import Image, ImageDraw, ImageFont

def criar_meme(imagem_path, texto_superior, texto_inferior, font_path='arial.ttf', output_path='meme.png'):
    imagem = Image.open(imagem_path)
    desenho = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype(font_path, 30)

    # Adicionar texto superior
    desenho.text((10, 10), texto_superior, font=fonte, fill='white')

    # Adicionar texto inferior
    desenho.text((10, imagem.size[1] - 40), texto_inferior, font=fonte, fill='white')

    imagem.save(output_path)

# Exemplo de uso
criar_meme('imagem.jpg', 'Texto Superior', 'Texto Inferior')
