from selene import browser, have, be
import os

def test_form_selene_1(setting_browser_from_selene):
    browser.open('/')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May').click()
    browser.element('.react-datepicker__year-select').type('2000').click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/fabula-ai.png'))
    browser.element('[placeholder="Current Address"').type('test')
    browser.element('#state').click()
    browser.all('.css-26l3qy-menu div').element_by(have.exact_text("Uttar Pradesh")).click()
    browser.element('#city').click()
    browser.all('.css-26l3qy-menu div').element_by(have.exact_text("Merrut")).click()
    browser.element('[type=submit]').click()
    browser.element('.table-responsive').all('td').should(
        have.exact_texts(
    'Student Name', 'John Doe',
            'Student Email', 'test@test.ru',
            'Gender', 'Male',
            'Mobile', '7999999999',
            'Date of Birth', '10 May,2000',
            'Subjects', 'English',
            'Hobbies', 'Reading',
            'Picture', 'fabula-ai.png',
            'Address', 'test',
            'State and City', 'Uttar Pradesh Merrut',
        )
    )