from django.core import mail

def test_send_email():
    mail.send_mail('Subject here', 'Here is the message.',
                   '18732.test.websec@gmail.com', ['happinesstaker@gmail.com'],
                   fail_silently=False)

test_send_email()
