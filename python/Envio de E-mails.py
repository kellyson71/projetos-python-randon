import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Configurações do servidor SMTP (use um servidor SMTP válido)
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'seu_email@example.com'
    smtp_password = 'sua_senha'

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adiciona o corpo da mensagem
    msg.attach(MIMEText(body, 'plain'))

    # Conecta-se ao servidor SMTP e envia o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

# Exemplo de uso
send_email('Assunto do E-mail', 'Corpo do E-mail', 'destinatario@example.com')
