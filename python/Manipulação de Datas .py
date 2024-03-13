from datetime import datetime, timedelta

# Obter a data e hora atual
current_datetime = datetime.now()
print("Data e Hora Atuais:", current_datetime)

# Adicionar 3 dias à data atual
future_datetime = current_datetime + timedelta(days=3)
print("Data e Hora daqui a 3 dias:", future_datetime)
