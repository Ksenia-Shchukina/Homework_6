from datetime import time
import random


def test_dark_theme_by_time():
    night_hours = list(range(22, 24)) + list(range(0, 7))
    random_time = random.choice(night_hours)
    current_time = time(hour=random_time)
    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def is_dark(random_hour, dark_theme_enabled_by_user):
    current_time = time(hour=random_hour)
    dark_theme_enabled_by_user = dark_theme_enabled_by_user
    if dark_theme_enabled_by_user is True:
        return True
    elif dark_theme_enabled_by_user is False:
        return False
    elif dark_theme_enabled_by_user is None:
        if time(0) <= current_time < time(6) or current_time == (time(23)):
            return True
        else:
            return False


def test_dark_theme_by_time_and_user_choice():
    assert is_dark(5, True) is True
    assert is_dark(5, False) is False
    assert is_dark(5, None) is True
    assert is_dark(6, True) is True
    assert is_dark(6, False) is False
    assert is_dark(6, None) is False
    assert is_dark(22, True) is True
    assert is_dark(22, False) is False
    assert is_dark(22, None) is False
    assert is_dark(23, True) is True
    assert is_dark(23, False) is False
    assert is_dark(23, None) is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suitable_users = users[3]
    assert suitable_users == {"name": "Olga", "age": 45}
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_func_name(func_name, *args):
    func_name = func_name.__name__.replace('_', ' ').title()
    args_value = ", ".join([*args])
    print(f'{func_name} [{args_value}]')
    return f'{func_name} [{args_value}]'


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_func_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_func_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_func_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
