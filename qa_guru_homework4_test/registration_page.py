import time

from selene import browser, have
import os
class RegistrationForm:
    def fill_firstname(self, firstname):
        browser.element('#firstName').type(firstname)
    def fill_lastname(self, lastname):
        browser.element('#lastName').type(lastname)
    def fill_email_address(self, email):
        browser.element('#userEmail').type(email)
    def fill_phone_number(self, phone):
        browser.element('#userNumber').type(phone)
    @property
    def fill_DateBithday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('May').click()
        browser.element('.react-datepicker__year-select').type('2000').click()
        browser.element('.react-datepicker__day--010').click()
    @property
    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()
    def fill_subjectsInput(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
    @property
    def fill_Hobbies(self):
        time.sleep(0.5)
        browser.element('[for="hobbies-checkbox-2"]').click()
    @property
    def upload_image(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../image/fabula-ai.png'))
    def fill_CurrentAddress(self, Address):
        browser.element('[placeholder="Current Address"').type(Address)
    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('.css-26l3qy-menu div').element_by(have.exact_text(state)).click()
    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('.css-26l3qy-menu div').element_by(have.exact_text(city)).click()

    @property
    def form_sibmit(self):
        browser.element('[type=submit]').click()

    def should_registreded_user_with(self, full_name, email, gender, phone_number, date_of_birth, subjects, hobbies, image, adress, country):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subjects,
                hobbies,
                image,
                adress,
                country,
            )
        )

