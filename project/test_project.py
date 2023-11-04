from dotenv import load_dotenv
import pytest

from project import setup_api_key


@pytest.fixture(autouse=True)
def load_env_variables(monkeypatch):
    load_dotenv()
    monkeypatch.setenv('API_KEY', '')


def test_setup_api_key_with_existing_key(mocker, monkeypatch):
    monkeypatch.setenv('API_KEY', 'existing_key')

    mocker.patch('builtins.input', return_value='Y')
    result = setup_api_key()

    assert result == 'existing_key'


def test_setup_api_key_without_existing_key(mocker):
    mocker.patch('project.get_api_key_from_user', return_value='new_key')
    mocker.patch('project.confirm_api_key', return_value='new_key')

    result = setup_api_key()

    assert result == 'new_key'
