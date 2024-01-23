import time
import webbrowser

def temporizador_pomodoro():
    print("Bem-vindo ao Temporizador Pomodoro!")
    for _ in range(4):
        print("Trabalhe por 25 minutos...")
        time.sleep(1500)  # 25 minutos em segundos
        print("Hora de uma pausa de 5 minutos!")
        time.sleep(300)   # 5 minutos em segundos

    print("Parabéns, você merece uma pausa mais longa!")
    time.sleep(900)  # 15 minutos em segundos
    print("Temporizador Pomodoro concluído. Hora de voltar ao trabalho!")

temporizador_pomodoro()
