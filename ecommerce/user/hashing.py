from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password, hasing_password):
    return pwd_content.verify(plain_password, hasing_password)

def get_password_hasing(password):
    return pwd_content.hash(password)