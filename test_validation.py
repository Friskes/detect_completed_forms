"""
Модуль для теста функции валидации данных из формы.
"""

from starlette.datastructures import FormData
import pytest

from validate_form import validate_form
from mock_data import (
    large_user_mock_data_dmy,
    large_user_mock_data_ymd,
    medium_user_mock_data,
    small_user_mock_data,
    large_user_mock_validator_data,
    medium_user_mock_validator_data,
    small_user_mock_validator_data
)


# pytest
@pytest.mark.asyncio
async def test_validator_form():
    """
    Тест функции валидации.
    """
    assert await validate_form(FormData(large_user_mock_data_dmy)) == large_user_mock_validator_data
    assert await validate_form(FormData(large_user_mock_data_ymd)) == large_user_mock_validator_data
    assert await validate_form(FormData(medium_user_mock_data)) == medium_user_mock_validator_data
    assert await validate_form(FormData(small_user_mock_data)) == small_user_mock_validator_data
