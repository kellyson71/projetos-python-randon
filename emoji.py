# mapeamento de palavras para emojis
def tradutor_emoji(frase):
    mapa_emojis = {
        "feliz": "😃", "triste": "😢", "amor": "❤️", "comida": "🍕", "gato": "😺", "cachorro": "🐶", "legal": "👍", "bom": "👌",
        "surpreso": "😲", "risos": "😂", "amo-você": "💖", "olá": "👋", "adeus": "👋🏼👋🏼", "obrigado": "🙏", "por favor": "🙏",
        "ok": "👌", "sim": "✅", "não": "❌", "bem": "🆗", "emoji": "😃", "python": "🐍", "divertido": "😄", "projeto": "🚀",
        "sol": "☀️", "lua": "🌙", "estrela": "⭐", "arco-íris": "🌈", "floresta": "🌳", "oceano": "🌊", "montanha": "⛰️",
        "avião": "✈️", "carro": "🚗", "trem": "🚂", "navio": "🚢", "telefone": "☎️", "computador": "💻", "livro": "📚",
        "pintura": "🎨", "musical": "🎵", "dança": "💃", "esportes": "⚽", "cinema": "🎬", "café": "☕", "chocolate": "🍫",
        "rosa": "🌹", "fogo": "🔥", "água": "💧", "terra": "🌍", "foguete": "🚀", "tv": "📺", "dinheiro": "💰", "tempo": "⏰",
        "relógio": "🕰️", "dormir": "😴", "soluço": "🤢", "palmas": "👏", "silêncio": "🤫", "luz": "💡", "comédia": "😆",
        "louco": "🤪", "anjo": "😇", "demônio": "😈", "nuvem": "☁️", "chuva": "🌧️", "neve": "❄️", "trovão": "⚡",
        "bomba": "💣", "bandeira": "🚩", "clima": "🌦️", "tornado": "🌪️", "terremoto": "🌋",
    }

    palavras = frase.split()

    emojis = [mapa_emojis.get(palavra.lower(), palavra) for palavra in palavras]

    frase_traduzida = ' '.join(emojis)

    return frase_traduzida

frase_usuario = input("Digite uma frase para traduzir para emojis: ")
resultado = tradutor_emoji(frase_usuario)
print("Frase traduzida:", resultado)
