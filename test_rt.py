import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('../selenium-pytest_basics-master/chromedriver.exe')
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('https://b2c.passport.rt.ru/')
    myDynamicElement = pytest.driver.find_element(By.CLASS_NAME, "tabs-input-container")

    yield

    pytest.driver.quit()

email = 'test@mail.com'
phone = '+79000000000'
login = 'userlogin'
account = '850014706560'
tpass = 'userpass'


def test_auth_form(): #1 тест загрузки формы авторизации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__wrapper').is_displayed()
    assert pytest.driver.find_element(By.ID, 't-btn-tab-phone').is_displayed()
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').is_displayed()
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').is_displayed()
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').is_displayed()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#username').is_displayed()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#password').is_displayed()
    assert pytest.driver.find_element(By.CLASS_NAME, 'what-is-container').is_displayed()

def test_tabs_selection_phone(): #2 тест выбора табов авторизации в зависимости от ввода пользователя - по телефону
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"

    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_tabs_selection_email(): #3 тест выбора табов авторизации в зависимости от ввода пользователя - по почте
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"

    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"


def test_tabs_selection_login(): #4 тест выбора табов авторизации в зависимости от ввода пользователя - по логину
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"


def test_tabs_selection_account(): #5 тест выбора табов авторизации в зависимости от ввода пользователя - по лицевому счету
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_phone_editbox_pos(): #6 проверка поля телефон позитивный тест
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__mask').text == ''

    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')

    assert check_error() == False

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_phone_editbox_neg(): #7 проверка поля телефон негативный тест
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('+712345678907')
    assert len(pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]').get_attribute('value')) <= 11
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__mask').text == ''
    assert check_error() == False

    while len(pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]').get_attribute('value')):
        pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(Keys.BACK_SPACE) #метод .clear() не срабатывает

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('+7123456789')
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__mask').text != ''

    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')

    assert check_error() == True

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_login_phone_neg(): #8 проверка связки номер и пароль негативный тест
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    assert len(pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]').get_attribute('value')) <= 11
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__mask').text == ''
    assert check_error() == False

    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(tpass)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == True

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"


def test_login_phone_pos(): #9 проверка связки номер и пароль позитивный тест
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(
        '+71234568900') #нужно заменить на данные реального пользователя, для теста использовался личный аккаунт
    assert len(pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]').get_attribute('value')) <= 11
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input__mask').text == ''
    assert check_error() == False

    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(
        'Correctpass01') #нужно заменить на данные реального пользователя, для теста использовался личный аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == False

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'base-card.home__info-card')))

    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name.user-info__name').text != ''


def test_login_email_neg(): #10 проверка связки почта и пароль негативный тест
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(tpass)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == True

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"


def test_login_email_pos(): #11  проверка связки почта и пароль позитивный тест
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)  # нужно заменить на данные реального пользователя, для теста использовался личный аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(
        'skillfactorY01')  # нужно заменить на данные реального пользователя, для теста использовался личный аккаунт

    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == False

    element = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'base-card.home__info-card')))

    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name.user-info__name').text != ''


def test_login_login_neg(): #12 проверка связки логин и пароль негативный тест
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(tpass)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == True

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"


def test_login_account_neg(): #13 проверка связки счет и пароль негативный тест
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(tpass)
    pytest.driver.find_element(By.CSS_SELECTOR, '#password').submit()

    assert check_pass() == True

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_reg_form_open(): #14 тест загрузки формы регистрации
    pytest.driver.find_element(By.ID, 'kc-register').click()

    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    assert pytest.driver.find_element(By.CLASS_NAME, 'register-form').is_displayed()
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').get_attribute('name') == 'firstName'
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').get_attribute('name') == 'lastName'
    assert pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-select.rt-select--search.register-form__dropdown').is_displayed()
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="address"]').get_attribute('id') == 'address'
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="password"]').get_attribute('id') == 'password'
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="password-confirm"]').get_attribute('id') == 'password-confirm'
    assert pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.register-form__reg-btn').is_displayed()
    assert pytest.driver.find_element(By.ID, 'rt-footer-agreement-link').get_attribute('href')\
           == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'
    assert pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-logo.main-header__logo').is_displayed()


def test_fill_user_data(): #15 тест ввода данных пользователя в форме регистрации
    pytest.driver.find_element(By.ID, 'kc-register').click()

    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input').send_keys('Новый')

    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input').send_keys('Пользователь')

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container.rt-select__input').click()

    dropdown = pytest.driver.find_elements(By.CLASS_NAME, 'rt-select__list-item')
    for item in dropdown:
        if item.text == 'Республика Казахстан':
            item.click()
            break

    assert check_reg_error() == False


def test_fill_account_data_pos(): #16 позитивный тест ввода учетных данных пользователя в форме регистрации
    test_fill_user_data()

    pytest.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(email) #для теста фактически использовался реальный email
    pytest.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('skillfactorY01')
    pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('skillfactorY01')

    assert check_error() == False


def test_fill_account_data_neg(): #17 негативный тест ввода учетных данных пользователя в форме регистрации
    test_fill_user_data()

    email_field = pytest.driver.find_element(By.XPATH, '//*[@id="address"]')
    email_field.send_keys(email[0:-3])
    email_field.send_keys(Keys.TAB)
    assert check_error() == True

    while len(email_field.get_attribute('value')):
        email_field.send_keys(Keys.BACK_SPACE)

    email_field.send_keys(email) #вводим правильный email, чтобы ниже убедиться в ошибках, относяшихся только к паролям

    bad_passwords = ['плохойпароль', 'shortPW', 'nouppercasepw', 'passwordwithmorethan20symBOLS']

    for item in bad_passwords:

        pass_field = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
        pass_field.send_keys(item)
        pass_conf_field = pytest.driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
        pass_conf_field.send_keys(item)
        assert check_error() == True

        while len(pass_field.get_attribute('value')):
            pass_field.send_keys(Keys.BACK_SPACE)

        while len(pass_conf_field.get_attribute('value')):
            pass_conf_field.send_keys(Keys.BACK_SPACE)


def test_pass_recovery(): #18 тест формы восстановления пароля
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__wrapper').is_displayed()
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"


def test_pass_recovery_neg(): #19 негативный тест восстановления пароля без ввода кода каптчи
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"

    pytest.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(phone)
    pytest.driver.find_element(By.CSS_SELECTOR, '#reset').click()
    assert check_conf() == True #не введен код подтверждения


def test_pass_visibility(): #20 тест работы кнопки отображения пароля при авторизации
    tabs = {'Телефон': 'phone', 'Почта': 'mail', 'Логин': 'login', 'Лицевой счёт': 'ls'}

    for item in tabs.keys():
        pytest.driver.find_element(By.ID, f't-btn-tab-{tabs.get(item)}').click()
        assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == item

        pass_field = pytest.driver.find_element(By.CSS_SELECTOR, '#password')
        pass_field.send_keys(tpass)
        assert pass_field.get_attribute('type') == 'password'

        eye_btn = pytest.driver.find_element(By.CLASS_NAME,
                                   'rt-base-icon.rt-base-icon--fill-path.rt-eye-icon.rt-input__eye.rt-input__eye')
        eye_btn.click()
        assert pass_field.get_attribute('type') == 'text'

        eye_btn.click()
        assert pass_field.get_attribute('type') == 'password'


#вспомогательные функции

def check_error():
    try:
        message = pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-input-container__meta.rt-input-container__meta--error')
    except NoSuchElementException:
        return False #нет сообщения об ошибке
    return True #есть сообщение об ошибке


def check_pass():
    try:
        message = pytest.driver.find_element(By.ID, 'form-error-message')
        message = pytest.driver.find_element(By.CLASS_NAME,
                                             'rt-link.rt-link--orange.login-form__forgot-pwd.login-form__forgot-pwd--animated')
    except NoSuchElementException:
        return False #нет сообщения об ошибке
    return True #есть сообщение об ошибке


def check_reg_error():
    try:
        message = pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')
    except NoSuchElementException:
        return False #нет сообщения об ошибке
    return True #есть сообщение об ошибке


def check_conf():
    try:
        message = pytest.driver.find_element(By.ID, 'form-error-message')
    except NoSuchElementException:
        return False #нет сообщения об ошибке
    return True #есть сообщение об ошибке