
from selene import browser
from data.user import User
from qa_guru_homework4_test.registration_page import RegistrationForm


def test_form_selene_1(setting_browser):
    form_registration = RegistrationForm()
    browser.open('/')
    Nikita = User(
        first_name = 'John',
        last_name =  'Doe',
        email = 'test@test.ru',
        gender = 'Male',
        userNumber = '7999999999',
        DateBithday = '10 May,2000',
        subjects = 'English',
        Hobbies = 'Reading',
        uploadPicture = 'fabula-ai.png',
        CurrentAddress = 'test',
        state = 'Uttar Pradesh',
        city = 'Merrut'
    )
    form_registration.user_registration(Nikita)
    form_registration.should_registreded_user_with(Nikita)