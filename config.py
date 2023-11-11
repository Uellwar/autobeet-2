from dotenv import dotenv_values

envs = dotenv_values(".env")

SQLALCHEMY_DATABASE_URI = envs['DATABASE_URI']

SECRET_KEY = envs['SECRET_KEY']

