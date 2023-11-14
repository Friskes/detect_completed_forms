"""
Модуль для тестов эндпоинтов.
"""

from httpx import AsyncClient
import pytest

from main import app
from mock_data import (
    large_user_mock_data_dmy,
    large_user_mock_data_ymd,
    medium_user_mock_data,
    small_user_mock_data
)


# pytest
@pytest.mark.asyncio
async def test_get_form_endpoint():
    """
    Тест эндпоинта проверки формы.
    """
    async with AsyncClient(app=app, base_url="http://test") as aclient:

        response1 = await aclient.post("get_form", data=large_user_mock_data_dmy)
        response2 = await aclient.post("get_form", data=large_user_mock_data_ymd)
        response3 = await aclient.post("get_form", data=medium_user_mock_data)
        response4 = await aclient.post("get_form", data=small_user_mock_data)

    assert response1.status_code == 200
    assert response1.json() == "UserForm"

    assert response2.status_code == 200
    assert response2.json() == "UserForm"

    assert response3.status_code == 200
    assert response3.json() == "UserForm"

    assert response4.status_code == 200
    assert response4.json() == {"user_email": "email", "user_phone": "phone"}
