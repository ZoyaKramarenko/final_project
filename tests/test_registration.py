from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import url

base_url = url

def check_field(driver, field, field_value):
   # будем нажимать на это поле для вызова валидации тестируемого поля
   password_confirm = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'password-confirm'))
   )

   field.send_keys(field_value)
   password_confirm.click()

   error_text = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta--error'))
   ).text

   field.send_keys("\b\b\b\b\b\b")
   field.clear()
   password_confirm.click()

   return error_text

def enter_register(driver):
   driver.get(base_url)

   btn_register = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'kc-register'))
   )

   btn_register.click()

def test_fail_first_name_short(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.NAME, 'firstName')
   assert check_field(driver, field, 'ф') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_fail_first_name_latin(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.NAME, 'firstName')
   assert check_field(driver, field, 'Boris') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_fail_last_name_short(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.NAME, 'lastName')
   assert check_field(driver, field, 'а') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_fail_adress_text(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.ID, 'address')
   assert check_field(driver, field, 'fddfjfdjdjffdj') == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

def test_fail_adress_phone_long(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.ID, 'address')
   assert check_field(driver, field, '+790652931091') == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

def test_fail_adress_phone_short(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.ID, 'address')
   assert check_field(driver, field, '+79065293') == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

def test_fail_password_short(web_browser):
   driver = web_browser

   enter_register(driver)

   field = driver.find_element(By.ID, 'password')
   assert check_field(driver, field, 'pas') == 'Длина пароля должна быть не менее 8 символов'
