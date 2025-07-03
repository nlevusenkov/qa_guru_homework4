import time
import allure
from selene import browser, have
import os


class RegistrationForm:
    @allure.step("Заполнение имени")
    def fill_first_name(self, user):
        with allure.step(f"Вводим имя: {user.first_name}"):
            browser.element('#firstName').type(user.first_name)
    @allure.step("Заполнение фамилии")
    def fill_last_name(self, user):
        with allure.step(f"Вводим фамилию: {user.last_name}"):
            browser.element('#lastName').type(user.last_name)

    @allure.step("Заполнение email")
    def fill_email(self, user):
        with allure.step(f"Вводим почту: {user.email}"):
            browser.element('#userEmail').type(user.email)

    @allure.step("Выбор пола")
    def select_gender(self, user):
        with allure.step(f"Выбралали пол: {user.gender}"):
            browser.all('[name=gender]').element_by(have.value(user.gender)).element('./following-sibling::label').click()
    @allure.step("Заполнение номера телефона")
    def fill_phone_number(self, user):
        with allure.step(f"Вводим номер телефона: {user.user_number}"):
            browser.element('#userNumber').type(user.user_number)

    @allure.step("Заполнение даты рождения")
    def fill_date_of_birth(self, user):
        browser.element('#dateOfBirthInput').click()
        with allure.step(f"Выбераем месяц: {user.month}"):
            browser.element('.react-datepicker__month-select').type(user.month).click()
        with allure.step(f"Выбераем год: {user.year}"):
            browser.element('.react-datepicker__year-select').type(user.year).click()
        with allure.step(f"Выбераем день: {user.day}"):
            browser.element(f'.react-datepicker__day--0{user.day:02}').click()

    @allure.step("Выбор предмета")
    def select_subject(self, user):
        with allure.step(f"Выбрали предмет: {user.subjects}"):
            browser.element('#subjectsInput').type(user.subjects).press_enter()

    @allure.step("Выбор хобби")
    def select_hobby(self, user):
        with allure.step(f"Выбрали предмет: {user.hobbies}"):
            browser.all('label.custom-control-label').element_by(have.text(user.hobbies)).click()

    @allure.step("Загрузка изображения")
    def upload_picture(self, user):
        with allure.step(f"Загрузили изображение: {user.upload_picture}"):
            image_dir = '../image'
            image_path = os.path.abspath(os.path.join(image_dir, user.upload_picture))
            browser.element('#uploadPicture').send_keys(image_path)
    @allure.step("Заполнение адреса")
    def fill_address(self, user):
        with allure.step(f"Выбрали адрес: {user.current_address}"):
            browser.element('[placeholder="Current Address"').type(user.current_address)

    @allure.step("Выбор штата")
    def select_state(self, user):
        with allure.step(f"Выбрали штат: {user.state}"):
            browser.element('#state').click()
            browser.all('.css-26l3qy-menu div').element_by(have.exact_text(user.state)).click()

    @allure.step("Выбор города")
    def select_city(self, user):
        with allure.step(f"Выбрали город: {user.city}"):
            browser.element('#city').click()
            browser.all('.css-26l3qy-menu div').element_by(have.exact_text(user.city)).click()
    @allure.step("Отправка формы")
    def submit_form(self):
        browser.element('[type=submit]').click()

    def user_registration(self, user):
        self.fill_first_name(user)
        self.fill_last_name(user)
        self.fill_email(user)
        self.fill_phone_number(user)
        self.fill_date_of_birth(user)
        self.select_gender(user)
        self.select_subject(user)
        # time.sleep(0.5)
        self.select_hobby(user)
        self.upload_picture(user)
        self.fill_address(user)
        self.select_state(user)
        self.select_city(user)
        self.submit_form()

    @allure.step("Проверка заполненных данных")
    def should_registreded_user_with(self, user):
        rows = browser.element('.table-responsive').all('td').even

        with allure.step(f"Поверка имени и фамилии: {user.first_name} {user.last_name}"):
            rows[0].should(have.exact_text(f'{user.first_name} {user.last_name}'))

        with allure.step(f"Проверка email: {user.email}"):
            rows[1].should(have.exact_text(user.email))

        with allure.step(f"Проверка пола: {user.gender}"):
            rows[2].should(have.exact_text(user.gender))

        with allure.step(f"Проверка номера телефона: {user.user_number}"):
            rows[3].should(have.exact_text(user.user_number))

        with allure.step(f"Проверка даты рождения: {user.date_birthday}"):
            rows[4].should(have.exact_text(user.date_birthday))

        with allure.step(f"Проверка предметов: {user.subjects}"):
            rows[5].should(have.exact_text(user.subjects))

        with allure.step(f"Проверка хобби: {user.hobbies}"):
            rows[6].should(have.exact_text(user.hobbies))

        with allure.step(f"Проверка имени загруженной картинки: {user.upload_picture}"):
            rows[7].should(have.exact_text(user.upload_picture))

        with allure.step(f"Проверка адреса: {user.current_address}"):
            rows[8].should(have.exact_text(user.current_address))

        with allure.step(f"Проверка региона и города: {user.state} {user.city}"):
            rows[9].should(have.exact_text(f'{user.state} {user.city}'))

