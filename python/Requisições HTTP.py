import requests

# Fazer uma requisição GET para uma API pública
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

if response.status_code == 200:
    data = response.json()
    print("Dados da API:", data)
else:
    print("Erro na requisição.")
