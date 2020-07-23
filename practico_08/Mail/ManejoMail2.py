# import os
import smtplib
from email.message import EmailMessage

# esto es para mejorar la seguridad
# EMAIL_ADDRESS  = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# contacts = ['email1', 'email'2]

msg = EmailMessage()
msg['Subject'] = 'Esto es el asunto'
msg['From'] = 'turnosconfesiones@gmail.com'
msg['To'] = 'ariasramirox@gmail.com' # contacts
# ', '.join(contacts)
msg.set_content('Esto es texto plano')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color SlateGray;"> Esto es html! </h1>
    </body>
</html>    
""", subtype='html')

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('turnosconfesiones@gmail.com', 'sgdpv2020')

smtp.send_message(msg)
