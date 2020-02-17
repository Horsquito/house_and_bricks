Установка зависимостей:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Запуск:

Находясь в корневой папке проекта 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```