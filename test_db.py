import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Собираем строку подключения (используем psycopg для SQLAlchemy 2.x)
DB_URL = f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

print("Подключаемся к базе данных...")
engine = create_engine(DB_URL)

try:
    with engine.connect() as conn:
        # 1. Проверяем таблицу
        result = conn.execute(text("SELECT COUNT(*) FROM afrr_prices;"))
        count = result.scalar()
        print(f"✅ Подключение успешно! Строк в таблице afrr_prices: {count}")
        
        # 2. Смотрим первые 3 строки
        print("\nПервые 3 строки:")
        df = pd.read_sql("SELECT * FROM afrr_prices LIMIT 3;", conn)
        print(df.to_string())
        
        # 3. Смотрим среднюю цену
        result = conn.execute(text("SELECT AVG(target_vwap_up) FROM afrr_prices;"))
        avg_price = result.scalar()
        print(f"\n💰 Средняя цена (target_vwap_up): {avg_price:.2f} €/МВт·ч")

except Exception as e:
    print(f"❌ Ошибка подключения: {e}")

