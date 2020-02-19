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

Для того чтобы увидеть главную страницу нужно перейти на адрес:
```
http://127.0.0.1:8000/stats/
```

Для создания дома нужно перейти по адресу:
```
http://127.0.0.1:8000/building/
```

Для перехода на индивидуальную страницу дома нужно перейти по адресу:
```
http://127.0.0.1:8000/building/{id} ({id} - это id дома)
```

Для перехода на страницу создания задания на закладку кирпичей нужно перейти по адресу:
```
http://127.0.0.1:8000/building/{id}/add_bricks/ ({id} - это id дома, в который хотим положить кирпичи)
```
