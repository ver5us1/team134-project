# Инструкция по установке и подключению к базе данных

Проект использует менеджер зависимостей **uv** и базу данных **PostgreSQL 16**,
развёрнутую на удалённом сервере.

---

## 1. Требования

- **uv** (версия 0.5+). Проверить: `uv --version`
- **Python 3.14+** — версия указана в `pyproject.toml` (`requires-python = ">=3.14"`).
  Отдельно устанавливать Python не обязательно: uv сам скачает нужную версию.
- Доступ в интернет для загрузки пакетов с PyPI.
- Реквизиты базы данных (хост, порт, имя БД, логин, пароль) — запросите у капитана команды.

Если uv ещё не установлен:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# или через Homebrew
brew install uv
```

После установки перезапустите терминал (или выполните `source ~/.zshrc`).

---

## 2. Установка зависимостей через uv

### 2.1. Клонировать репозиторий и перейти в него

```bash
git clone https://github.com/ver5us1/team134-project.git
cd team134-project
```

### 2.2. Синхронизировать окружение

```bash
uv sync
```

Команда:
- создаёт виртуальное окружение `.venv/` в корне проекта;
- устанавливает Python нужной версии (если его нет);
- ставит все зависимости строго по `uv.lock`.

Для полного соответствия зафиксированным версиям (например, в CI) используйте:

```bash
uv sync --frozen
```

### 2.3. Активировать окружение

```bash
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows
```

### 2.4. Полезные команды uv

```bash
uv run python script.py     # запуск скрипта в окружении проекта
uv run jupyter lab          # запуск Jupyter
uv add <package>            # добавить зависимость (+ обновит pyproject.toml и uv.lock)
uv remove <package>         # удалить зависимость
uv lock --upgrade           # обновить версии в uv.lock
```

> Пакет `python-dotenv` (используется в `src/data/db.py`) сейчас приходит
> транзитивно через `mlflow`. Чтобы сделать зависимость явной, выполните:
> `uv add python-dotenv`.

---

## 3. Настройка переменных окружения

Скопируйте шаблон и заполните реальными значениями:

```bash
cp .env.example .env
```

Содержимое `.env`:

```dotenv
DB_HOST=адрес_сервера
DB_PORT=5432
DB_NAME=team134_db
DB_USER=team134_user
DB_PASSWORD=ваш_пароль
```

> `.env` добавлен в `.gitignore` и содержит секреты. **Не коммитьте его.**
> В репозитории хранится только безопасный шаблон `.env.example`.

---

## 4. Подключение к базе данных

Параметры подключения:

| Параметр | Значение |
|----------|----------|
| СУБД | PostgreSQL 16 |
| Host | `***.***.***.***` |
| Port | `5432` |
| Database | `team134_db` |
| User | `team134_user` |
| Таблица с данными | `afrr_prices` |

### 4.1. Проверка подключения

```bash
python src/data/test_connection.py
```

Скрипт `src/data/test_connection.py`:
- проверяет наличие `.env` и заполненность переменных;
- подключается к серверу;
- проверяет наличие таблицы `afrr_prices`;
- выводит число строк и среднюю цену `target_vwap_up`.

Ожидаемый результат:

```text
🔍 Проверка подключения к базе данных...

✅ УСПЕХ! Подключение установлено.
📊 Таблица 'afrr_prices' найдена.
📈 Количество строк: 26304
💰 Средняя цена (target_vwap_up): 23.44 €/МВт·ч

🎉 Всё готово к работе!
```

Альтернативный простой скрипт в корне проекта:

```python
python test_db.py
```

### 4.2. Использование в коде

Готовый SQLAlchemy-engine находится в `src/data/db.py`:

```python
from src.data.db import get_db_engine
from sqlalchemy import text

engine = get_db_engine()

with engine.connect() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM afrr_prices;")).scalar()
    print(count)
```

Строка подключения собирается из `.env` в формате:

```text
postgresql+psycopg://DB_USER:DB_PASSWORD@DB_HOST:DB_PORT/DB_NAME
```

Используется драйвер `psycopg` (версия 3). Пакет `psycopg2-binary` также
установлен для совместимости с инструментами, требующими psycopg2.

### 4.3. Чтение всей витрины данных через pandas

```python
import pandas as pd
from src.data.db import get_db_engine

engine = get_db_engine()
df = pd.read_sql("SELECT * FROM afrr_prices;", engine)
print(df.head())
```

---

## 5. Частые проблемы

| Ошибка | Причина / решение |
|--------|-------------------|
| `Файл .env не найден` | Выполните `cp .env.example .env` в корне проекта |
| `не заполнены переменные` | Проверьте, что в `.env` заданы все `DB_*` переменные |
| `password authentication failed` | Неверный `DB_PASSWORD` |
| `Connection refused` / `timeout` | Неверные `DB_HOST`/`DB_PORT` или нет доступа к сети/VPN |
| `ModuleNotFoundError: dotenv` | Выполните `uv add python-dotenv` и повторите `uv sync` |
| `ModuleNotFoundError: src` | Запускайте команды из корня проекта через `uv run python -m ...` |

Проверить состояние окружения:

```bash
uv run python -c "import sys; print(sys.executable); print(sys.version)"
```
