from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import url

base_url = url

def get_redirect_url(driver, button_id):
   driver.get(base_url)

   btn_register = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'kc-register'))
   )

   btn_vk = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, button_id))
   )

   btn_vk.click()

   WebDriverWait(driver, 10).until(
      EC.url_changes)

   return driver.current_url

def test_success_vk_link_redirect(web_browser):
   driver = web_browser

   current_url = get_redirect_url(driver, 'oidc_vk')

   assert (current_url.startswith("https://id.vk.com/auth"))

def test_success_ok_link_redirect(web_browser):
   driver = web_browser

   current_url = get_redirect_url(driver, 'oidc_ok')

   assert (current_url.startswith("https://connect.ok.ru/dk"))

def test_success_mail_link_redirect(web_browser):
   driver = web_browser

   current_url = get_redirect_url(driver, 'oidc_mail')

   assert (current_url.startswith("https://connect.mail.ru/oauth/authorize"))

def test_success_forgot_password_redirect(web_browser):
   driver = web_browser

   current_url = get_redirect_url(driver, 'forgot_password')

   assert (current_url.startswith("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"))
