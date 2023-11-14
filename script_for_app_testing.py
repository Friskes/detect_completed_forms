"""
Модуль для отправки POST запросов к get_form эндпоинту.
"""

def main():
    """
    Функция для отправки POST запросов к get_form эндпоинту использующая моковые данные.\n
    Запуск:
    #### python script_for_app_testing.py
    """
    from time import sleep

    import httpx

    from mock_data import (
        large_user_mock_data_dmy,
        medium_user_mock_data,
        small_user_mock_data
    )


    forms_data = [
        large_user_mock_data_dmy,
        medium_user_mock_data,
        small_user_mock_data
    ]

    for form_data in forms_data:
        response = httpx.post("http://127.0.0.1:8000/get_form", data=form_data)
        print(f'\nREQUEST FORM DATA: {form_data}')
        print(f'RESPONSE STATUS CODE: {response.status_code}')
        print(f'RESPONSE TEXT: {response.text}\n')
        sleep(1)


if __name__ == '__main__':
    main()
