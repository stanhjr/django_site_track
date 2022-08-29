import binascii
import os
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import Celery
from django.utils import timezone
from django.conf import settings

from email_sender.config import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_site_track.settings")
app = Celery(
    "email_sender",
    broker="redis://localhost:6379/5",
)

app.config_from_object(config)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_auction_win.s(), name='add every 60')
    # sender.add_periodic_task(10.00, send_mail_contact_us.s("dfdf@dfdf.cc", "subject", "text"))


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


@app.task
def send_registration_link_to_email(code: str, email_to):
    password = settings.EMAIL_HOST_PASSWORD
    sender_email = settings.EMAIL_HOST_USER

    receiver_email = email_to
    text = f"""\
    Hi,
    How are you?
    This is your registration link:
    {settings.CELERY_SEND_MAIL_HOST}auth/account-activate/?code={code}"""

    # http://92.38.241.95/auth/account-activate/?code=365b2f4a3ec0117c4cf7f54fd826a84b0d84d872

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = email_to
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


@app.task
def send_reset_password_link_to_email(code: str, email_to):
    password = settings.EMAIL_HOST_PASSWORD
    sender_email = settings.EMAIL_HOST_USER

    receiver_email = email_to
    text = f"""\
    Hi,
    How are you?
    This is your restore password link:
    {settings.CELERY_SEND_MAIL_HOST}auth/restore-password/?code={code}"""

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = email_to

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


@app.task(queue='contact_us')
def send_mail_contact_us(email_from, subject, text):
    password = settings.EMAIL_HOST_PASSWORD
    sender_email = settings.EMAIL_HOST_USER
    receiver_email = "stanhjrpower@gmail.com"
    text = f"""\
    email_from: {email_from}\n
    text: {text}
  """

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


@app.task
def send__make_offer_mail(email_from, email_to, price, phone_number, first_name, text):
    password = settings.EMAIL_HOST_PASSWORD
    sender_email = settings.EMAIL_HOST_USER
    receiver_email = email_to
    text = f"""\
        Congratulations,
        You received an offer to buy!
        Contacts:
        Name: {first_name}
        email: {email_from}
        Phone number: {phone_number}
        Offer price: {price}
        Message: {text}"""

    message = MIMEMultipart("alternative")
    message["Subject"] = "You received an offer to buy"
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


@app.task
def send_win_auction_mail(pk: str, email_to, contact_data_owner: str, price: int):
    password = settings.EMAIL_HOST_PASSWORD
    sender_email = settings.EMAIL_HOST_USER

    receiver_email = email_to
    text = f"""\
    Congratulations,
    you won this auction!
    {settings.CELERY_SEND_MAIL_HOST}auth/vehicle/posted-detail/{pk}
    owner contact details:
    {contact_data_owner}
    price: {price}
    
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = email_to

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


@app.task
def send_auction_win():
    from site_track.models import SaleAds
    objects = SaleAds.objects.filter(sale_end_time__gte=timezone.now(), send_email_to_winner=False).all()
    for sale in objects:
        send_win_auction_mail.delay(pk=sale.pk,
                                    email_to=sale.user_bet.email,
                                    contact_data_owner=sale.user.get_contact_data(),
                                    price=sale.last_price)
        sale.send_email_to_winner = True
        sale.save()

# /home/stan/freelance/django_site_track/venv/bin/celery --app=email_sender.tasks beat --loglevel=INFO -Q contact_us,celery
# /home/stan/freelance/django_site_track/venv/bin/celery --app=email_sender.tasks flower --address=127.0.0.6 --port=5566 --basic_auth=stan:1
