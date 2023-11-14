"""
Основной модуль с эндпоинтами.
"""

import os

import uvicorn
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
    AsyncIOMotorCursor
)
from fastapi import FastAPI, Depends
from starlette.requests import Request
from envparse import Env

from validate_form import validate_form
from generate_mock_data import generate_mock_data


if not os.path.exists('data/'):
    generate_mock_data()

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/form_templates_db")

app = FastAPI()
client = AsyncIOMotorClient(MONGODB_URL)
app.state.mongo_client = client


@app.get("/get_records")
async def get_records(request: Request, length: int = 10) -> list[dict[str, str]]:
    """
    Возвращает length документов из коллекции templates.
    """
    adb: AsyncIOMotorDatabase = request.app.state.mongo_client.form_templates_db
    cursor: AsyncIOMotorCursor = adb.templates.find({})

    records = []
    for document in await cursor.to_list(length):
        document["_id"] = str(document["_id"])
        records.append(document)

    return records


@app.post("/get_form")
async def get_form(request: Request, field_types: dict[str, str] = Depends(validate_form)):
    """
    Возвращает название формы либо названия переданных полей
    с их типами, в зависимости от переданных полей.
    """
    adb: AsyncIOMotorDatabase = request.app.state.mongo_client.form_templates_db
    templates: AsyncIOMotorCollection = adb.templates

    fields_to_check = list(field_types.keys())

    collection_fields = await templates.find_one({}, projection=fields_to_check)

    query = {field_name: field_type for field_name, field_type in field_types.items()
             if field_name in collection_fields}

    if query:
        response: list[dict] = await templates.find(query).to_list(length=None)

        del response[0]['_id']
        form_name = response[0].pop('name')

        if (len(response[0].keys() & field_types.keys()) == 4
        and set(response[0].values()) == set(field_types.values())):

            return form_name

    return field_types


def main():
    """
    Запуск uvicorn сервера при запуске файла.
    """
    # uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
