import time
from selene import browser, have
import os


class RegistrationForm:
    def user_registration(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.userNumber)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('May').click()
        browser.element('.react-datepicker__year-select').type('2000').click()
        browser.element('.react-datepicker__day--010').click()
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        time.sleep(0.5)
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('../image/fabula-ai.png'))
        browser.element('[placeholder="Current Address"').type(user.CurrentAddress)
        browser.element('#state').click()
        browser.all('.css-26l3qy-menu div').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('.css-26l3qy-menu div').element_by(have.exact_text(user.city)).click()
        browser.element('[type=submit]').click()

    def should_registreded_user_with(self, user):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.userNumber,
                user.DateBithday,
                user.subjects,
                user.Hobbies,
                user.uploadPicture,
                user.CurrentAddress,
                f'{user.state} {user.city}'
            )
        )
