# ⚡ Прогнозирование цен на рынке электроэнергии Day-Ahead

<div align="center">

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Checkpoint](https://img.shields.io/badge/checkpoint-1%2F4-blue)
![Track](https://img.shields.io/badge/track-ML-orange)
![Level](https://img.shields.io/badge/level-base%2Fmiddle-red)
![Team](https://img.shields.io/badge/team-4%20members-purple)
![License](https://img.shields.io/badge/license-MIT-green)

**Тема №121 · Трек: Machine Learning · Уровень: base / middle**

</div>

---

## 📌 О проекте

Точное прогнозирование цен на рынке электроэнергии **Day-Ahead** позволяет участникам рынка принимать более эффективные торговые решения и снижать финансовые риски.

В рамках проекта мы разрабатываем и сравниваем модели машинного и глубокого обучения для прогнозирования почасовых цен на следующие сутки на основе исторических рыночных данных и внешних факторов.

---

## 🎯 Цель и задачи

**Цель:** разработка моделей прогнозирования цен на рынке электроэнергии Day-Ahead на следующие сутки.

**Задачи:**
- [ ] Сбор и анализ рыночных данных
- [ ] Построение признаков на основе исторических данных и внешних факторов
- [ ] Обучение моделей машинного обучения и глубокого обучения
- [ ] Сравнение качества прогнозов

---

## 👥 Состав команды

| № | ФИО | Роль | GitHub |
|:-:|-----|------|--------|
| 1 | Крамсков Даниил Павлович | 🧭 Капитан | [@username](https://github.com/username) |
| 2 | Танташев Руслан Рафаильевич | 💻 ML-инженер | [@RusTantas](https://github.com/RusTantas) |
| 3 | Давыдов Николай Александрович | 💻 ML-инженер | [@username](https://github.com/username) |
| 4 | Бунтин Владислав Романович | 💻 ML-инженер | [@username](https://github.com/username) |

### 🎓 Руководители проекта

- **Сулейманов Нихат**
- **Александр Голубев**

---

## 🧠 Подход и модели

### ML-этап (baseline)
| Модель | Назначение |
|--------|-----------|
| Linear Regression | Базовая линейная модель, benchmark |
| Random Forest | Устойчивая к выбросам ансамблевая модель |
| CatBoost | Градиентный бустинг с категориальными признаками |
| XGBoost | Классический градиентный бустинг |
| LightGBM | Быстрый бустинг для больших данных |

### DL-этап
| Модель | Особенность |
|--------|-------------|
| LSTM | Учёт долгосрочных зависимостей во временных рядах |
| TCN (Temporal Convolutional Networks) | Параллельная обработка временных окон |
| Transformers для временных рядов | Attention-механизм для долгих зависимостей |

### 🔬 Дополнительные направления
- Прогнозирование **ценовых скачков** (spikes)
- **Вероятностное** прогнозирование (интервальные оценки)
- Использование **погодных данных** и прогнозов генерации **ВИЭ**

---

## 🗓 План работы на год

### ✅ Чекпоинт 1 — до 6 октября
- [x] Создан чат команды и добавлен куратор
- [x] Проведено знакомство с руководителями
- [x] Зафиксирована тема №121 и план работы
- [x] Создан репозиторий, оформлен README

### 🔄 Чекпоинт 2 — _<даты>_
- [ ] Сбор и предобработка рыночных данных
- [ ] EDA, анализ сезонности и аномалий
- [ ] Формирование признаков (лаги, скользящие, календарные, погодные)
- [ ] Baseline-модели: Linear Regression, Random Forest

### 🔄 Чекпоинт 3 — _<даты>_
- [ ] Обучение бустингов: CatBoost, XGBoost, LightGBM
- [ ] Тюнинг гиперпараметров, кросс-валидация по времени
- [ ] Метрики: MAE, RMSE, MAPE, sMAPE
- [ ] Сравнение ML-моделей

### 🔄 Чекпоинт 4 — _<даты>_
- [ ] DL-модели: LSTM, TCN, Transformers
- [ ] Эксперименты с вероятностным прогнозированием
- [ ] Прогнозирование ценовых скачков
- [ ] Учёт погоды и генерации ВИЭ

### 🏁 Итоговая защита — _<даты>_
- [ ] Финальное сравнение всех моделей
- [ ] Презентация и демо
- [ ] Итоговый отчёт

---

## 🛠 Технологический стек

**Язык и окружение:**
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Git](https://img.shields.io/badge/Git-VCS-red?logo=git)

**Данные и ML:**
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn)
![CatBoost](https://img.shields.io/badge/CatBoost-yellow)
![XGBoost](https://img.shields.io/badge/XGBoost-green)
![LightGBM](https://img.shields.io/badge/LightGBM-blue)

**Deep Learning:**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow)

**Визуализация и метрики:**
Matplotlib · Seaborn · Plotly · scikit-learn metrics

---

## 📂 Структура репозитория
```text
team134-project/
│
├── 📄 README.md                    # описание проекта
├── 📄 requirements.txt             # зависимости Python
├── 📄 .gitignore                   # исключения Git
│
├── 📁 data/                        # данные
│   ├── 📁 raw/                     # исходные сырые данные
│   ├── 📁 processed/               # очищенные и обработанные данные
│   └── 📁 external/                # погода, календарь, ВИЭ
│
├── 📁 notebooks/                   # Jupyter-ноутбуки
│   ├── 📓 01_eda.ipynb             # разведочный анализ
│   ├── 📓 02_features.ipynb        # построение признаков
│   ├── 📓 03_ml_models.ipynb       # ML-модели
│   └── 📓 04_dl_models.ipynb       # DL-модели
│
├── 📁 src/                         # исходный код
│   ├── 📁 data/                    # загрузка и препроцессинг
│   │   ├── 🐍 loader.py
│   │   └── 🐍 preprocess.py
│   ├── 📁 features/                # генерация признаков
│   │   └── 🐍 build_features.py
│   ├── 📁 models/                  # модели
│   │   ├── 🐍 linear.py
│   │   ├── 🐍 boosting.py
│   │   └── 🐍 lstm.py
│   └── 📁 evaluation/              # метрики и валидация
│       └── 🐍 metrics.py
│
├── 📁 models/                      # сохранённые веса моделей
│   └── 📦 best_model.pkl
│
├── 📁 reports/                     # графики и отчёты
│   ├── 🖼 figures/
│   └── 📄 final_report.md
│
└── 📁 tests/                       # тесты
    └── 🐍 test_pipeline.py
```

---

## 🔗 Полезные ссылки

- 🌐 [Репозиторий проекта](https://github.com/ver5us1/team134-project)
- 📝 [Peer-reviewer — Чекпоинт 1](_<ссылка>_)

---

<div align="center">

**Команда 134** · Тема №121 · Годовой проект · 2024–2025

Сделано с ❤️ и ⚡

</div>