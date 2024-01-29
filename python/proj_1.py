import os

def bytes_to_mb(bytes):
    return bytes / (1024 ** 2)

def calculate_percentage(total, used):
    return (used / total) * 100

def generate_report(users, total_space):
    report = "ACME Inc.           Uso do espaço em disco pelos usuários\n"
    report += "------------------------------------------------------------------------\n"
    report += "Nr.  Usuário        Espaço utilizado     % do uso\n"

    for i, (user, space) in enumerate(users, start=1):
        space_mb = bytes_to_mb(space)
        percentage = calculate_percentage(total_space, space)
        report += f"{i:<4} {user:<15} {space_mb:.2f} MB {' ' * (17 - len(str(space_mb)))} {percentage:.2f}%\n"

    report += f"\nEspaço total ocupado: {bytes_to_mb(total_space):.2f} MB\n"
    report += f"Espaço médio ocupado: {bytes_to_mb(total_space/len(users)):.2f} MB\n"

    return report

def read_users_file(file_path):
    users = []
    total_space = 0

    with open(file_path, 'r') as file:
        for line in file:
            user, space = line.strip().split()
            space = int(space)
            users.append((user, space))
            total_space += space

    return users, total_space

def main():
    file_path = "usuarios.txt"
    users, total_space = read_users_file(file_path)

    # Ordenar os usuários pelo percentual de espaço ocupado
    users.sort(key=lambda x: calculate_percentage(total_space, x[1]), reverse=True)

    # Mostrar apenas os n primeiros usuários
    n = int(input("Digite o número de usuários a serem exibidos: "))
    users = users[:n]

    report = generate_report(users, total_space)

    # Gerar o arquivo relatório.txt
    with open("relatorio.txt", 'w') as output_file:
        output_file.write(report)

if __name__ == "__main__":
    main()
