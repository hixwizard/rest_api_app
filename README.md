# API для приложения Yatube.
## Автор: Баринов Станислав
### Содержимое проекта:
### - модели обращения к базе данных
### - сериализаторы приведения данных (python/JSON)
### - view наборы для клиентов
### - api-роутер с эндпойнтами по названиям view-классов
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://git@github.com:hix9/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```