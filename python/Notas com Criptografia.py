from cryptography.fernet import Fernet
import os
import pickle

class SecureNotesApp:
    def __init__(self):
        self.key = self.load_or_generate_key()
        self.notes = self.load_notes()

    def load_or_generate_key(self):
        key_file = "secret.key"

        if os.path.exists(key_file):
            with open(key_file, "rb") as key_file:
                key = key_file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as key_file:
                key_file.write(key)

        return key

    def load_notes(self):
        notes_file = "secure_notes.dat"

        if os.path.exists(notes_file):
            with open(notes_file, "rb") as notes_file:
                encrypted_notes = notes_file.read()
                decrypted_notes = self.decrypt_data(encrypted_notes)
                return pickle.loads(decrypted_notes)
        else:
            return {}

    def save_notes(self):
        notes_file = "secure_notes.dat"
        encrypted_notes = self.encrypt_data(pickle.dumps(self.notes))

        with open(notes_file, "wb") as notes_file:
            notes_file.write(encrypted_notes)

    def encrypt_data(self, data):
        cipher = Fernet(self.key)
        return cipher.encrypt(data)

    def decrypt_data(self, data):
        cipher = Fernet(self.key)
        return cipher.decrypt(data)

    def display_menu(self):
        print("1. Visualizar Notas")
        print("2. Adicionar Nota")
        print("3. Editar Nota")
        print("4. Excluir Nota")
        print("5. Sair")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.edit_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                self.save_notes()
                break
            else:
                print("Opção inválida. Tente novamente.")

    def view_notes(self):
        if not self.notes:
            print("Nenhuma nota encontrada.")
        else:
            print("Notas:")
            for title, content in self.notes.items():
                print(f"\n{title}:\n{content}")

    def add_note(self):
        title = input("Digite o título da nota: ")
        content = input("Digite o conteúdo da nota: ")
        self.notes[title] = content
        print("Nota adicionada com sucesso.")

    def edit_note(self):
        title = input("Digite o título da nota que deseja editar: ")
        if title in self.notes:
            content = input("Digite o novo conteúdo da nota: ")
            self.notes[title] = content
            print("Nota editada com sucesso.")
        else:
            print("Nota não encontrada.")

    def delete_note(self):
        title = input("Digite o título da nota que deseja excluir: ")
        if title in self.notes:
            del self.notes[title]
            print("Nota excluída com sucesso.")
        else:
            print("Nota não encontrada.")

if __name__ == "__main__":
    secure_notes_app = SecureNotesApp()
    secure_notes_app.run()
