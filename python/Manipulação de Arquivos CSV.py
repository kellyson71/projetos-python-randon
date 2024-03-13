import csv

# Escrever em um arquivo CSV
with open('dados.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Idade', 'Cidade'])
    writer.writerow(['João', 25, 'São Paulo'])
    writer.writerow(['Maria', 30, 'Rio de Janeiro'])

# Ler de um arquivo CSV
with open('dados.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
