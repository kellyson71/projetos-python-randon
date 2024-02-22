while True:
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    if usuario != senha:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")
