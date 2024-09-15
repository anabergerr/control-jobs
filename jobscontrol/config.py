import os

class Config:
    """Configurações padrão para a aplicação."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Use uma chave secreta forte
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações para evitar avisos

    # Configurações para desenvolvimento
    DEBUG = True
    TESTING = False


