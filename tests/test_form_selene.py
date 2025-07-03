import time

import allure
from allure_commons.types import Severity
from selene import browser
from data.user import User
from qa_guru_homework4_test.registration_page import RegistrationForm

@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Заполнение формы")
@allure.story("Заполнение формы")
@allure.link("https://demoqa.com/automation-practice-form", name="Форма регистрации")
def test_form_selene(setting_browser):
    form_registration = RegistrationForm()
    browser.open('https://demoqa.com/automation-practice-form')
    Nikita = User(
        first_name = 'John',
        last_name =  'Doe',
        email = 'test@test.ru',
        gender = 'Female',
        user_number = '7999999999',
        day='10',
        month='May',
        year='2000',
        subjects = 'English',
        hobbies = 'Reading',
        upload_picture = 'fabula-ai.png',
        current_address = 'test',
        state = 'Uttar Pradesh',
        city = 'Merrut'
    )
    form_registration.user_registration(Nikita)
    form_registration.should_registreded_user_with(Nikita)