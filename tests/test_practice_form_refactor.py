from demoqa_tests.model.pages.registration_page import RegistrationPage
from selene import have
import allure

@allure.title('Успешная регистрация пользователя')
def test_practice_form_filling(browser_settings):
    with allure.step('Открыть форму регистрации'):
       registration_page = RegistrationPage()
       registration_page.open()
    # Заполняем поля
    with allure.step('Заполнить поле First_name'):
       registration_page.fill_first_name('Андрей')
    with allure.step('Заполнить поле Last_name'):
        registration_page.fill_last_name('Смирнов')
    with allure.step('Заполнить поле email'):
        registration_page.fill_email('name123@example.com')
    with allure.step('Выбрать значение для Gender'):
        registration_page.choose_gender('Male')
    with allure.step('Заполнить поле Mobile'):
        registration_page.fill_phone_number('1234567891')
    with allure.step('Заполнить поле Date of Birth'):
        registration_page.fill_birthday('1990','April','20')
    with allure.step('Заполнить поле Subjects'):
        registration_page.select_subjects('Computer Science')
    with allure.step('Выбрать значение для Hobbies'):
        registration_page.choose_hobbies('Sports')
    with allure.step('Выбрать файл для Picture'):
        registration_page.upload_picture('beautiful_tropical_beach_sea_ocean.png')
    with allure.step('Заполнить поле Current Address'):
        registration_page.fill_address('Street, 15 house')
    with allure.step('Выбрать значение для State'):
        registration_page.select_state('Haryana')
    with allure.step('Выбрать значение для City'):
        registration_page.select_city('Karnal')

    #Подтверждаем заполнение данных
    with allure.step('Нажать на кнопку для отправки формы'):
        registration_page.submit()

    #Проверка после нажатия на кнопку submit
    with allure.step('Проверить результат заполнения формы регистрации'):
        registration_page.registered_user_with.should(
        have.texts(
        'Андрей Смирнов',
        'name123@example.com',
        'Male',
        '1234567891',
        '20 April,1990',
        'Computer Science',
        'Sports',
        'beautiful_tropical_beach_sea_ocean.png',
        'Street, 15 house',
        'Haryana Karnal'
    )
    )