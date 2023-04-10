from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

# для корректного отображения кириллицы в параметризаторах


def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--language', action='store',
                     default="en", help="Choose any language:")


# Запуск браузера(для каждой функции)
# по умолчанию запускается для каждой функции
@pytest.fixture(scope="function")
def browser(request):
    # получаем параметр командной строки browser_name
    language = request.config.getoption("language")
    Options().add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=Options())
    yield browser
    print("\nquit browser..")
    browser.quit()
