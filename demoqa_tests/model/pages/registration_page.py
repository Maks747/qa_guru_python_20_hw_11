from selene import browser, command, have
import os



class RegistrationPage:
    def __init__(self):
        self.registered_user_with = browser.element('.table').all('td').even

    def open(self):
            browser.open('https://demoqa.com/automation-practice-form')

            browser.driver.execute_script("$('#fixedban').remove()")
            browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def select_subjects(self, value):
            browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self, value):
        #browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).click()
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(f'resources/{file}')
            )

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_open_form_with_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))