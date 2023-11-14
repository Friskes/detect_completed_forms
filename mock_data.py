user_db_mock_data = [
    {
        "name": "UserForm",
        "user_email": "email",
        "user_phone": "phone",
        "user_birthday": "date",
        "user_description": "text"
    },
    {
        "name": "CompanyForm",
        "company_email": "email",
        "company_phone1": "phone",
        "company_phone2": "phone",
        "founding_company": "date",
        "company_description": "text"
    },
    {
        "name": "DeclarationForm",
        "started_working": "date",
        "ended_working": "date",
        "workplace": "text",
        "profit": "text"
    }
]

large_user_mock_data_dmy = {
    "user_email": "sharpchristopher@example.net",
    "user_phone": "+7 775 063 46 04",
    "user_birthday": "05.01.1999",
    "user_description": "Care deep gas trouble doctor give institution. Attorney low analysis.",
    "user_name": "Alex",
    "user_height": "180",
    "user_age": "19"
}

large_user_mock_data_ymd = {**large_user_mock_data_dmy}
large_user_mock_data_ymd["user_birthday"] = "1999-01-05"

medium_user_mock_data = {
    "user_email": "sharpchristopher@example.net",
    "user_phone": "+7 775 063 46 04",
    "user_birthday": "1999-01-05",
    "user_description": "Care deep gas trouble doctor give institution. Attorney low analysis."
}

small_user_mock_data = {
    "user_email": "sharpchristopher@example.net",
    "user_phone": "+7 775 063 46 04",
}

large_user_mock_validator_data = {
    "user_email": "email",
    "user_phone": "phone",
    "user_birthday": "date",
    "user_description": "text",
    "user_name": "text",
    "user_height": "text",
    "user_age": "text"
}

medium_user_mock_validator_data = {
    "user_email": "email",
    "user_phone": "phone",
    "user_birthday": "date",
    "user_description": "text"
}

small_user_mock_validator_data = {
    "user_email": "email",
    "user_phone": "phone"
}
