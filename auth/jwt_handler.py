import jwt
import datetime

SECRET_KEY = "finance_secret_key"

def generate_token(email):

    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token