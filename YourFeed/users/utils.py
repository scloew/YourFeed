import os
import secrets
from flask import url_for, current_app
from flask_mail import Message
from YourFeed import mail

sender = "YourFeed@demo"
env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
with open(env_file, 'r') as env:
    sender = env.read().split('\n')[1]


def send_reset_request(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender=sender, recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request. Simply ignore this email and no changes will be made.
    '''
    mail.send(msg)
