# Django Inventory App

Простое веб-приложение на **Django**, предназначенное для управления товарами на складе.  
Позволяет добавлять, редактировать, удалять и просматривать товары, а также отображает общее количество и стоимость всех товаров.

---

## 🚀 Возможности

- Добавление, редактирование и удаление товаров  
- Подсчёт общего количества товаров  
- Подсчёт общей стоимости товаров  
- Интерфейс на HTML (без отдельного фронтенда)

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
git clone https://github.com/yourusername/inventory-app.git
cd inventory-app
```

### 2️⃣ Создать и активировать виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Установить зависимости

```bash
pip install django
```

### 4️⃣ Провести миграции

```bash
python manage.py migrate
```

### 5️⃣ Запустить сервер

```bash
python manage.py runserver
```

Теперь приложение доступно по адресу:  
👉 **http://127.0.0.1:8000/**

---

## 📂 Структура проекта

```
inventory_project/
│
├── inventory_app/
│   ├── migrations/
│   ├── templates/
│   │   └── inventory_app/
│   │       ├── index.html
│   │       ├── add_item.html
│   │       └── edit_item.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── inventory_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

## 🧮 Пример вывода

Главная страница отображает список всех товаров и внизу:

```
Общее количество товаров: 42
Общая стоимость товаров: 12345.00 ₸
```

---

## 📜 Лицензия

MIT License © 2025 Dovlet Eminov
