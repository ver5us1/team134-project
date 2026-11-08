import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

def get_db_engine():
    """Возвращает SQLAlchemy engine для подключения к базе данных."""
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    
    # Используем драйвер psycopg (3-я версия)
    db_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db_name}"
    
    return create_engine(db_url)
