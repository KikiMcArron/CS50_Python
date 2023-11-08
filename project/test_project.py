from dotenv import load_dotenv
import pytest

from project import setup_api_key, is_valid_api_key, confirm_api_key, select_model, get_user_prompt


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


def test_valid_api_key():
    api_key = 'sk-' + 'a' * 48
    assert is_valid_api_key(api_key) == True


def test_api_key_too_short():
    api_key = 'sk-' + 'a' * 47
    assert is_valid_api_key(api_key) == False


def test_api_key_too_long():
    api_key = 'sk-' + 'a' * 49
    assert is_valid_api_key(api_key) == False


def test_api_key_wrong_prefix():
    api_key = 'pk-' + 'a' * 48
    assert is_valid_api_key(api_key) == False


def test_api_key_non_alphanumeric():
    api_key = 'sk-' + 'a' * 47 + '#'
    assert is_valid_api_key(api_key) == False


def test_confirm_api_key_yes(mocker):
    mocker.patch('builtins.input', return_value='Y')
    api_key = 'sk-' + 'a' * 48
    result = confirm_api_key(api_key)
    assert result == api_key


def test_confirm_api_key_no(mocker):
    mocker.patch('builtins.input', side_effect=['N', 'Y'])
    new_key = 'sk-' + 'b' * 48
    mocker.patch('project.get_api_key_from_user', return_value=new_key)
    api_key = 'sk-' + 'a' * 48
    result = confirm_api_key(api_key)
    assert result == new_key


def test_confirm_api_key_invalid(mocker):
    mocker.patch('builtins.input', side_effect=['invalid', 'Y'])
    api_key = 'sk-' + 'a' * 48
    result = confirm_api_key(api_key)
    assert result == api_key


def test_select_model_valid(mocker):
    mocker.patch('builtins.input', return_value='1')
    result = select_model()
    assert result == "gpt-3.5-turbo-16k"


def test_select_model_invalid_number(mocker):
    mocker.patch('builtins.input', side_effect=['3', '1'])
    result = select_model()
    assert result == "gpt-3.5-turbo-16k"


def test_select_model_non_integer(mocker):
    mocker.patch('builtins.input', side_effect=['invalid', '1'])
    result = select_model()
    assert result == "gpt-3.5-turbo-16k"


def test_get_user_prompt(mocker):
    mocker.patch('builtins.input', return_value='Can you bring me a pizza?')
    result = get_user_prompt()
    assert result == 'Can you bring me a pizza?'
