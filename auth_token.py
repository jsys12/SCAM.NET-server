import random, string

def generate_token():
    token = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    return token
