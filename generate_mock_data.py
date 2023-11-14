"""
Модуль для заполнения БД моковыми данными.
"""

from pymongo import MongoClient
from envparse import Env

from mock_data import user_db_mock_data


env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/form_templates_db")

client = MongoClient(MONGODB_URL)


def generate_mock_data():
    """
    Заполнение БД.
    """
    client.form_templates_db.templates.insert_many(user_db_mock_data)
    client.close()


def drop_db():
    """
    Удаление БД.
    """
    client.drop_database('form_templates_db')
    client.close()


def main():
    """
    Запуск заполнения БД.
    """
    generate_mock_data()


if __name__ == "__main__":
    main()
