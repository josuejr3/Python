
#### <span style="color:rgb(4, 255, 0)">Enviando emails para o Gmail</span>

O SMTP serve como uma forma para enviar e-mails. Porém, antes de enviarmos os e-mails é necessários fazer algumas configurações no Gmail.

-  Primeiramente, verificar nas configurações do Gmail se IMAP está ativado.
-  Em seguida, vá para a página "fazer login com senhas de app"
-  Gere uma senha de app através do gmail.

No arquivo ".env" inserir a senha criada. 

```Python
# Importando a biblioteca os para obter o e-mail e senha  
# que estão gravados como variáveis de ambiente em .env  
  
import os  
from dotenv import load_dotenv # type: ignore  
from pathlib import Path  
  
from aula18 import print_iter  
  
load_dotenv(verbose=True)  
  
# Dados do remetente  
remetente = os.getenv("FROM_EMAIL", "")  
destinatario = remetente  
  
# Configurações do servidor SMTP  
  
# smtp da google  
smtp_server = "smtp.gmail.com"  
smtp_port = 587  
smtp_user = os.getenv("FROM_EMAIL", "")  
smtp_passw = os.getenv('EMAIL_PASSWORD')  
  
# Configuração - Mensagem de Texto  
  
# Gerando caminho do arquivo  
CAMINHO_MSG = Path(__file__).parent / "aula29_30_email.html"  
  
with open(CAMINHO_MSG, 'r', encoding="utf-8") as f:  
    texto_arquivo = f.read()  
  
# Transformar mensagem em MIMEMultipart  
# MIMEMultipart basicamente eu passo informações de from, to e subject  
  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
  
mime_multipart = MIMEMultipart()  
mime_multipart["from"] = remetente  
mime_multipart["to"] = destinatario  
mime_multipart["subject"] = "Este é o assunto"  
  
# Criando o corpo do texto  
corpo_email = MIMEText(texto_arquivo, "html", "utf-8")  
# Anexa o corpo do texto  
mime_multipart.attach(corpo_email)  
  
# Abrindo o servidor smtp  
import smtplib  
  
# Enviando e-mail  
with smtplib.SMTP(smtp_server, smtp_port) as server:  
    server.ehlo()  
    server.starttls()  
    server.login(smtp_user, smtp_passw)  
    server.send_message(mime_multipart)  
    print('E-mail enviado com sucesso')
```


