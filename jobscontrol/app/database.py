from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Exemplo de URL de banco de dados (SQLite)
DATABASE_URL = "sqlite:///./database.db"

# Cria a engine do banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy
Base = declarative_base()