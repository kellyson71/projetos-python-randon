import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Criação de threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Inicia as threads
thread1.start()
thread2.start()

# Aguarda até que ambas as threads terminem
thread1.join()
thread2.join()
