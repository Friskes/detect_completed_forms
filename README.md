# Web-приложение для определения заполненных форм.

## Задание
#### https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I

## 1. Зависимости
Для запуска этого проекта потребуется:
- Python 3.11
- Docker Desktop
- Git

## 2. Установка
```shell script
# Запуск контейнера
docker compose up -d

# Остановка контейнера
docker compose down
```

## 3. Использование
> Все дальнейшие действия должны производится при запущенном контейнере.

### Вариант - 1
- Вы можете протестировать работу приложения с помощью встроенного скрипта который посылает `POST` запросы аналогично тому как это делает `Postman`, информация о запросах будет выводится в терминал.

Из директории проекта запустите скрипт командой:
```shell script
python script_for_app_testing.py
```
В терминале вы увидите сообщения о сделанных запросах и полученных ответах от приложения.

### Вариант - 2
- Вы можете протестировать работу приложения с помощью `Postman`.

Введите в адресной строке адрес:
```
http://127.0.0.1:8000/get_form
```

Сделайте первый `POST` запрос с `x-www-form-urlencoded`:
```
user_email:        sharpchristopher@example.net
user_phone:        +7 775 063 46 04
user_birthday:     05.01.1999
user_description:  Care deep gas trouble doctor give institution. Attorney low analysis.
user_name:         Alex
user_height:       180
user_age:          19
```
Приложение должно вернуть: `"UserForm"`
<br/>
Сделайте второй `POST` запрос с `x-www-form-urlencoded`:
```
user_email:        sharpchristopher@example.net
user_phone:        +7 775 063 46 04
user_birthday:     05.01.1999
user_description:  Care deep gas trouble doctor give institution. Attorney low analysis.
```
Приложение должно вернуть: `"UserForm"`
<br/>
Сделайте третий `POST` запрос с `x-www-form-urlencoded`:
```
user_email:  sharpchristopher@example.net
user_phone:  +7 775 063 46 04
```
Приложение должно вернуть:
```json
{
    "user_email": "email",
    "user_phone": "phone"
}
```

#### Бонусом вы можете получить список всех данных из БД сделав GET запрос по адресу:
```
http://127.0.0.1:8000/get_records
```

## 4. Запуск тестов
### Вариант - 1
- Выполните тесты внутри контейнера:
```
docker exec -it app pytest ./test_endpoint.py ./test_validation.py
```
### Вариант - 2
- Для запуска тестов без контейнера необходим установленный MongoDB сервер на ПК и прочие зависимости для запуска без контейнера.

Создайте виртуальное окружение:
```
py -3.11 -m venv venv
```
Активируйте виртуальное окружение:
```
venv\Scripts\activate.bat
```
Установите зависимости:
```
pip install -r requirements.txt
```
Создайте моковую БД:
```
python generate_mock_data.py
```
Выполните тесты:
```
pytest
```

### Полезная информация
Для просмотра БД которая лежит в Docker контейнере с помощью приложения MongoDB Compass, при подключении к БД необходимо указать локальный IP адресс вашего компьютера (НЕ localhost).
