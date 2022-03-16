import smtplib
import ssl


class Sms:
    def __init__(self, number, phone_carrier, username, password, email_domain, email_port):
        self.CARRIERS = {
            'att': '@mms.att.net',
            'tmobile': '@tmomail.net',
            'verizon': '@vtext.com',
            'sprint': '@messaging.sprintpcs.com',
            'virgin': '@vmobl.com',
            'boost': '@smsmyboostmobile.com',
            'cricket': '@sms.cricketwireless.net',
            'metro': '@mymetropcs.com',
            'us cellular': '@email.uscc.net',
            'xfinity': '@vtext.com'
        }
        self.EMAIL_DOMAIN = email_domain
        self.EMAIL_PORT = email_port

        self.receiver_email = f'{number}{self.CARRIERS.get(phone_carrier)}'
        self.username = username
        self.password = password

        self.initialize_server()

    def initialize_server(self):
        context = ssl.create_default_context()
        self.server = smtplib.SMTP(self.EMAIL_DOMAIN, self.EMAIL_PORT)
        self.server.ehlo()
        self.server.starttls(context=context)
        self.server.ehlo()
        self.server.login(self.username, self.password)

    def send(self, message):
        self.server.sendmail(self.username, self.receiver_email, message)
