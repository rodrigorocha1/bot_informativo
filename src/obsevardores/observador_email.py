import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config.config import Config
from src.obsevardores.iobservador import IObservador


class ObservadorGmailEmail(IObservador):
    def __init__(self, assunto: str):
        self.__rementente = Config.EMAIL_REMENTENTE
        self.__destinatario = Config.EMAIL_DESTINATARIO
        self.__senha = Config.SENHA_EMAIL
        self.__mensagem = MIMEMultipart()
        self.__assunto = assunto
        self.__servico_email = smtplib.SMTP(Config.CONF_SMTP, Config.PORTA_SMTP)

    def atualizar(self, dados: str):
        if not dados:
            self.__mensagem['Subject'] = self.__assunto
            self.__mensagem['From'] = self.__rementente
            self.__mensagem['To'] = self.__destinatario
            corpo = MIMEText(dados, 'html')
            self.__mensagem.attach(corpo)
            self.__servico_email.starttls()
            self.__servico_email.login(self.__mensagem['FROM'], self.__senha)
            self.__servico_email.sendmail(
                self.__mensagem['From'],
                [self.__mensagem['To']],
                self.__mensagem.as_string().encode('utf-8')
            )
        else:
            print('Sem dados para enviar no email')
