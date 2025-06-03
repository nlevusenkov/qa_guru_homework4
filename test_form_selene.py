from selene import browser, have


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
    #browser.element('#subjectsContainer').type('English').click()
    browser.element('#hobbies-checkbox-1').click()


