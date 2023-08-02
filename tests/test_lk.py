from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import url, email, password
from tests.test_login import email_login

base_url = url

def test_success_redirect_from_auth_profile_to_site(web_browser):
   driver = web_browser

   email_login(driver, email, password)

   rt_btn = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'rt-btn'))
   )

   rt_btn.click()

   WebDriverWait(driver, 10).until(
      EC.url_to_be('https://msk.rt.ru/'))

   assert (driver.current_url.startswith('https://msk.rt.ru/'))

def lk_enter(driver):
   email_login(driver, email, password)

   rt_btn = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'lk-btn'))
   )

   rt_btn.click()

   WebDriverWait(driver, 10).until(
      EC.url_to_be('https://start.rt.ru/'))

def test_success_redirect_from_auth_profile_to_lk(web_browser):
   driver = web_browser
   lk_enter(driver)

   assert (driver.current_url.startswith('https://start.rt.ru/'))

def test_success_logout(web_browser):
   driver = web_browser

   email_login(driver, email, password)

   rt_btn = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'logout-btn'))
   )

   rt_btn.click()

   WebDriverWait(driver, 10).until(
      EC.url_changes)

   assert (driver.current_url.startswith('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth'))

def test_success_elements_menu(web_browser):
   driver = web_browser
   lk_enter(driver)

   menu_main = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/p'))
   )

   menu_payments = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[2]/p'))
   )

   menu_payments.click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   assert (driver.current_url.startswith('https://start.rt.ru/payments/cart'))

   menu_main.click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   menu_finance = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[3]/p'))
   )

   menu_finance.click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   assert (driver.current_url.startswith('https://start.rt.ru/payments'))

   menu_main.click()

   WebDriverWait(driver, 10).until(EC.url_changes)


   menu_bonuses = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[4]/p'))
   )

   menu_bonuses.click()

   h_bonuses = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[2]/h1'))
   )

   assert h_bonuses.text == 'Программа «Бонус»'

   driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[1]/a[1]').click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   menu_moving = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[5]/p'))
   )

   menu_moving.click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   assert (driver.current_url.startswith('https://start.rt.ru/pereezd'))

   driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/p').click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   menu_promocode = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[6]/p'))
   )

   menu_promocode.click()

   h_promocode = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div[1]/div/header'))
   )

   assert h_promocode.text == 'Активация промокода'

   driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[1]/a[1]').click()

   WebDriverWait(driver, 10).until(EC.url_changes)

   menu_games = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[3]/div/div[1]/div[7]/p'))
   )

   menu_games.click()

   h_games = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div/div/h1[1]'))
   )

   assert h_games.text == 'Игровые сервисы'
