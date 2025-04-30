import re
from unittest.mock import patch

import pytest
import requests

from test_ingestion_infra.utils import add, capitalize_words, to_uppercase


def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Test123") == "TEST123"


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected


@pytest.fixture
def sample_data():
    return {"name": "Network Rail", "code": "NR"}


def test_sample_data(sample_data):
    assert sample_data["code"] == "NR"


def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()


@patch("requests.get")
def test_get_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    result = get_data()
    assert result == {"key": "value"}

    from unittest.mock import patch

import requests


def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()


@patch("requests.get")
def test_get_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    result = get_data()
    assert result == {"key": "value"}


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"
    assert capitalize_words("") == ""
    assert capitalize_words("123 abc") == "123 Abc"
    assert capitalize_words("ALL CAPS") == "All Caps"


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None
