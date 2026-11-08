import os
import sys
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from src.data.db import get_db_engine

def test_connection():
    print("🔍 Проверка подключения к базе данных...\n")

    # 1. Проверяем, существует ли .env файл
    if not os.path.exists('.env'):
        print("❌ ОШИБКА: Файл .env не найден в корне проекта!")
        print("👉 Решение: Скопируйте шаблон командой `cp .env.example .env` и заполните его данными.")
        sys.exit(1)

    # 2. Загружаем переменные
    load_dotenv()
    
    # 3. Проверяем, что все переменные заполнены
    required_vars = ['DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ ОШИБКА: В файле .env не заполнены переменные: {', '.join(missing_vars)}")
        print("👉 Решение: Откройте .env и укажите недостающие данные.")
        sys.exit(1)

    # 4. Пробуем подключиться
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            # Проверяем таблицу
            count = conn.execute(text("SELECT COUNT(*) FROM afrr_prices;")).scalar()
            avg_price = conn.execute(text("SELECT AVG(target_vwap_up) FROM afrr_prices;")).scalar()
            
            print("✅ УСПЕХ! Подключение установлено.")
            print(f"�� Таблица 'afrr_prices' найдена.")
            print(f"📈 Количество строк: {count}")
            print(f"💰 Средняя цена (target_vwap_up): {avg_price:.2f} €/МВт·ч")
            print("\n🎉 Всё готово к работе!")

    except OperationalError as e:
        print("❌ ОШИБКА ПОДКЛЮЧЕНИЯ К СЕРВЕРУ!")
        if "password authentication failed" in str(e):
            print("👉 Неверный пароль. Проверьте DB_PASSWORD в .env")
        elif "Connection refused" in str(e) or "timeout" in str(e):
            print("👉 Сервер недоступен. Проверьте DB_HOST и DB_PORT, а также интернет-соединение.")
        else:
            print(f"Детали ошибки: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ НЕИЗВЕСТНАЯ ОШИБКА: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
