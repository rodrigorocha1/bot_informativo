import pytest
from unittest.mock import patch, MagicMock
from email import message_from_bytes
from src.obsevardores.observador_email import GmailEmail
from src.config.config import Config


@patch("smtplib.SMTP")
def test_enviar_email(mock_smtp):
    mock_server = MagicMock()
    mock_smtp.return_value = mock_server

    assunto = "Teste de Email"
    texto = "<h1>Corpo de Email</h1>"
    email = GmailEmail(assunto)
    email.enviar_email(texto)

    mock_smtp.assert_called_with(Config.CONF_SMTP)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with(email._GmailEmail__rementente, email._GmailEmail__senha)
    mock_server.sendmail.assert_called_once()

    args = mock_server.sendmail.call_args[0]
    assert args[0] == email._GmailEmail__rementente
    assert args[1] == [email._GmailEmail__destinatario]


    raw_message = args[2]  # bytes
    msg = message_from_bytes(raw_message)


    if msg.is_multipart():
        payload = msg.get_payload(0).get_payload(decode=True).decode()
    else:
        payload = msg.get_payload(decode=True).decode()

    assert "<h1>Corpo de Email</h1>" in payload


@pytest.mark.real_email
def test_enviar_email_real():
    """
    Teste que envia um email real. Só execute quando quiser enviar de fato.
    """
    assunto = "Teste Real de Email via Pytest"
    corpo = "<h1>Este é um email enviado pelo pytest!</h1>"

    email = GmailEmail(assunto)

    try:
        email.enviar_email(corpo)
        enviado = True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        enviado = False

    assert enviado, "O email não foi enviado com sucesso"