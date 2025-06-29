
from selene import browser, have, be

from qa_guru_homework4_test.registration_page import RegistrationForm


def test_form_selene_1(setting_browser):
    form_registration = RegistrationForm()
    browser.open('/')
    form_registration.fill_firstname('John')
    form_registration.fill_lastname('Doe')
    form_registration.fill_email_address('test@test.ru')
    form_registration.fill_gender
    form_registration.fill_phone_number('7999999999')
    form_registration.fill_DateBithday
    form_registration.fill_subjectsInput('English')
    form_registration.fill_Hobbies
    form_registration.upload_image
    form_registration.fill_CurrentAddress('test')
    form_registration.fill_state("Uttar Pradesh")
    form_registration.fill_city('Merrut')
    form_registration.form_sibmit
    form_registration.should_registreded_user_with(full_name='John Doe',
                                                   email='test@test.ru',
                                                   gender='Male',
                                                   phone_number='7999999999',
                                                   date_of_birth='10 May,2000',
                                                   subjects='English',
                                                   hobbies='Reading',
                                                   image='fabula-ai.png',
                                                   adress='test',
                                                   country='Uttar Pradesh Merrut')
