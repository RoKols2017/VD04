# 🧠 Flask UI Switcher Project

## 📌 Описание

Проект на Flask с возможностью **переключения между двумя интерфейсами**:
- 🧼 Классический (Vanilla) с собственными стилями
- 🎨 Bootstrap 5 для адаптивного интерфейса

Все страницы поддерживают динамическое меню и содержат:
- Главная
- Блог
- Контакты
- Переключение UI
- Отображение текущих даты и времени на главной странице

---

## 🗂️ Структура проекта

```txt
flask_app/
│
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── bootstrap/
    │   ├── index.html
    │   ├── blog.html
    │   ├── contacts.html
    │   └── nav.html
    └── vanilla/
        ├── index.html
        ├── blog.html
        ├── contacts.html
        └── nav.html
```

---

## 🚀 Установка и запуск

### 🔧 1. Клонируй проект:
```bash
git clone https://github.com/your-username/flask-ui-switcher.git
cd flask-ui-switcher
```

### 🐍 2. Установи зависимости:
```bash
pip install flask flask-session
```

### 🏁 3. Запусти приложение:
```bash
python app.py
```

Открой [http://localhost:5000](http://localhost:5000) в браузере.

---

## 🔁 Переключение UI

На любой странице нажми **"Сменить UI"** в меню — Flask сохранит выбор в `session` и будет отрисовывать соответствующие шаблоны:
- `/templates/vanilla/` — обычная версия
- `/templates/bootstrap/` — с Bootstrap

---

## 📦 Зависимости

- Flask
- Flask-Session
- Bootstrap 5 (через CDN)

---

## 🕒 Особенности

- Поддержка отображения текущих даты и времени (`datetime.now`)
- Возможность динамического выбора темы
- Простая и масштабируемая архитектура

---

## 🧙 Автор

**Роман Кольский** — RoKols2017@gmail.com

---

## 📜 Лицензия

Свободно использовать, редактировать, распространять.

