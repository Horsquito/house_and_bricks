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

Для того чтобы увидеть статистику:
```
http://127.0.0.1:8000/stats/
```

Для того чтобы создать дом нужно перейти по адресу:
```
http://127.0.0.1:8000/building/
```

Для перехода на индивидуальную страницу дома нужно перейти по адресу:
```
http://127.0.0.1:8000/building/{id} ({id} - это id дома)
```

Для того чтобы заложить кирпич:
```
http://127.0.0.1:8000/building/{id}/add_bricks/ ({id} - это id дома, в который хотим положить кирпичи)
```
