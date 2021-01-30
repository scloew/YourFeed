import os


def get_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    with open(env_path, 'r') as env:
        data = env.read().split('\n')
        key = data[0]
        email = data[1]
        pw = data[2]
        db_uri = data[3]
    return key, email, pw, db_uri


class Config:

    SECRET_KEY, MAIL_USERNAME, MAIL_PASSWORD, SQLALCHEMY_DATABASE_URI = get_env()

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
