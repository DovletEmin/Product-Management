# Product Management

Простое веб-приложение на **Django**, предназначенное для управления товарами на складе.  
Позволяет добавлять, редактировать, удалять и просматривать товары, а также отображает общее количество и стоимость всех товаров.

---

## 🚀 Возможности

- Добавление, редактирование и удаление товаров
- Подсчёт общего количества товаров
- Подсчёт общей стоимости товаров
- Интерфейс на HTML

---

## 🛠️ Технологии

- **Python 3.10+**
- **Django 5+**
- **SQLite3** (по умолчанию)
- **HTML / CSS (Bootstrap)**

---

## ⚙️ Установка и запуск

### 1️⃣ Клонировать проект

```bash
git clone https://github.com/DovletEmin/Product-Management.git
cd product-management
```

### 2️⃣ Создать и активировать виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Установить зависимости

```bash
pip install -r requirements.txt
```

### 4️⃣ Провести миграции

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5️⃣ Запустить сервер

```bash
python manage.py runserver
```

Теперь приложение доступно по адресу:  
👉 **http://127.0.0.1:8000/**
