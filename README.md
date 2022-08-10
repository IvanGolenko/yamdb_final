![example workflow](https://github.com/IvanGolenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# yamdb_final
Описание проекта:
```
Проект представляет из себя социальную сеть в которой можно оставлять отзывы на 
фильмы, книги и музыку и ставить оценки.
```

# Как запустить проект:
Клонировать репозиторий:
```
git clone https://github.com/IvanGolenko/yamdb_final.git
```

Выполнить сборку контейнера:
```
docker-compose up -d --build 
```

Выполнить миграции, создать суперпользователя и собрать статику
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic
```

Загрузить дамп базы командой:
```
python manage.py loaddata fixtures/fixtures.json
```

#### Работа на сервере:

Перед отправкой на боевой сервер добавьте в Secrets GitHub Actions следующие переменные окружения:
```
DB_ENGINE
DB_HOST
DB_NAME
DB_PORT

DOCKER_PASSWORD=<Docker password>
DOCKER_USERNAME=<Docker username>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ(cat ~/.ssh/id_rsa)>

TG_CHAT_ID=<ID чата, в который поступит сообщение>
TELEGRAM_TOKEN=<токен вашего бота>
```

Установите Docker, а вместе с ним Docker Compose на сервер:
```
sudo apt install docker.io docker-compose -y
```

Скопируйте файлы docker-compose.yaml и nginx/default.conf из проекта на сервер:
```
scp docker-compose.yaml <username>@<host>/home/<username>/docker-compose.yaml
scp default.conf <username>@<host>/home/<username>/nginx/default.conf
```

Сервер и REDOC по API:
```
Адрес приложения: http://{ваш IP}/api/v1/
REDOC: http://{ваш IP}/redoc/
```

Технологии, которые использовались:
- Python ![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
- Django ![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
- Django REST Framework ![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
- PostgresSQL ![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)
- Nginx ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat-square&logo=nginx&logoColor=white)

Автор:
```
Иван Голенко
```