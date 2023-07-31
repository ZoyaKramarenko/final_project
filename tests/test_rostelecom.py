from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import email, password, url, home_url, phone, account

base_url = url

def login(driver, login_type, login, pas):
   # Открыть домашнюю страницу входа
   driver.get(base_url)

   btn_enter = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'kc-login'))
   )

   login_type_button = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, login_type))
   )

   login_type_button.click()

   # Ищем поле ввода электронной почты, очищаем его, а затем вводим свой email,
   # подставить вместо "<your_email>" свой email.
   field_email = driver.find_element(By.ID, "username")
   field_email.clear()
   field_email.send_keys(login)

   # То же самое для поля с паролем
   field_pass = driver.find_element(By.ID, "password")
   field_pass.clear()
   field_pass.send_keys(pas)

   btn_enter.click()

def email_login(driver, mail, pas):
   login(driver, 't-btn-tab-mail', mail, pas)

def test_success_email_login(web_browser):
   driver = web_browser

   email_login(driver, email, password)

   url_after_login = driver.current_url.split('?')[0]

   assert url_after_login == home_url

def test_failed_email_login(web_browser):
   driver = web_browser

   email_login(driver, email, 'failed_password')

   form_error = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'form-error-message'))
   )

   assert form_error.get_attribute("data-error") == 'Неверный логин или пароль'

def phone_login(driver, phone_number, pas):
   login(driver, 't-btn-tab-phone', phone_number, pas)

def test_success_phone_login(web_browser):
   driver = web_browser

   phone_login(driver, phone, password)

   url_after_login = driver.current_url.split('?')[0]

   assert url_after_login == home_url

def test_failed_phone_login(web_browser):
   driver = web_browser

   phone_login(driver, phone, 'failed_password')

   form_error = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'form-error-message'))
   )

   assert form_error.get_attribute("data-error") == 'Неверный логин или пароль'

def account_login(driver, user, pas):
   login(driver, 't-btn-tab-login', user, pas)

def test_success_account_login(web_browser):
   driver = web_browser

   account_login(driver, account, password)

   url_after_login = driver.current_url.split('?')[0]

   assert url_after_login == home_url

def test_failed_account_login(web_browser):
   driver = web_browser

   account_login(driver, account, 'failed_password')

   form_error = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'form-error-message'))
   )

   assert form_error.get_attribute("data-error") == 'Неверный логин или пароль'
