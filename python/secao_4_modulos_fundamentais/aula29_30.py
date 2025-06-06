# Importando a biblioteca os para obter o e-mail e senha
# que estão gravados como variáveis de ambiente em .env

import os
from dotenv import load_dotenv # type: ignore

load_dotenv(verbose=True)

# Dados do remetente
remetente = os.getenv("FROM_EMAIL", "")
destinatario = remetente

# Configurações do servidor SMTP

smtp_server = "smtp.google.com"
smtp_port = 587
smtp_user = os.getenv("FROM_EMAIL", "")
smtp_passw = os.getenv('EMAIL_PASSWORD')

 