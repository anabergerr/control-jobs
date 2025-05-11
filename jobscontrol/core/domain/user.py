from passlib.context import CryptContext

# Criando o contexto para criptografar a senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User:
    def __init__(
        self, id, name, email, password_hash, created_at=None, updated_at=None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at

    # Método para verificar a senha
    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password_hash)

    # Método para criar o hash da senha
    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)
