"""
Модуль для валидации данных формы.
"""

import re

from fastapi import Depends
from starlette.datastructures import FormData

from utils import get_body


dmy_pattern = r'\b(?:0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}\b' # DD.MM.YYYY
ymd_pattern = r'\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b' # YYYY-MM-DD
phone_pattern = r'\+7 \d{3} \d{3} \d{2} \d{2}' # +7 xxx xxx xx xx
email_pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)' # xxx@xxx.xxx

patterns = {
    'date': rf'{dmy_pattern}|{ymd_pattern}',
    'phone': phone_pattern,
    'email': email_pattern
}


async def get_value_type(field_value: str) -> str:
    """
    Возвращает тип поля формы на основе его значения.
    """
    for value_type, pattern in patterns.items():
        if re.fullmatch(pattern, field_value):
            return value_type
    return 'text'


async def validate_form(body: FormData = Depends(get_body)) -> dict[str, str]:
    """
    Возвращает словарь с названиями полей и типами значений.
    """
    return {field_name: await get_value_type(field_value) 
            for field_name, field_value in body._dict.items()}
