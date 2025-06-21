from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User
import allure
from allure_commons.types import Severity

@allure.tag("web")
@allure.title("Successful fill registration form")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Maksim")
@allure.feature("Student Registration Form")
@allure.link("'https://demoqa.com'", name="Testing")

def test_practice_form_filling():
    with allure.step('Open registration page'):
        registration_page = RegistrationPage()
        registration_page.open()

    test_user = User(
    first_name='Андрей',
    last_name = 'Смирнов',
    email = 'name123@example.com',
    gender = 'Male',
    phone_number = '1234567891',
    year = '1990',
    month = 'April',
    day = '20',
    subjects = 'Computer Science',
    hobbies = 'Reading',
    picture = 'beautiful_tropical_beach_sea_ocean.png',
    address = 'Street, 15 house',
    state = 'Haryana',
    city = 'Karnal'
    )

    with allure.step("Fill form and send"):
        registration_page.registers_user(test_user)
    with allure.step("Check registered user"):
        registration_page.should_registered_user_with(test_user)