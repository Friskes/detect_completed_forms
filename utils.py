"""
Модуль для получения тела из запроса.
"""

from json import JSONDecodeError

from fastapi import Request
from fastapi.exceptions import HTTPException


async def get_body(request: Request):
    """
    Функция получения тела из запроса.
    """
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        raise HTTPException(status_code=400, detail='No Content-Type provided!')
    elif content_type == 'application/json':
        try:
            return await request.json()
        except JSONDecodeError:
            raise HTTPException(status_code=400, detail='Invalid JSON data')
    elif (content_type == 'application/x-www-form-urlencoded' or
          content_type.startswith('multipart/form-data')):
        try:
            return await request.form()
        except Exception:
            raise HTTPException(status_code=400, detail='Invalid Form data')
    else:
        raise HTTPException(status_code=400, detail='Content-Type not supported!')
