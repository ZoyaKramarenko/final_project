# Итоговый проект 28 модуль.  

Для выполнения задания использовался selenium, тк он позволяет гибко тестировать, повторяя действия пользователя.  

Для запуска всех тестов нужно выполнить команду pytest -v  
Для запуска конкретного файла с тестами pytest -v tests/test_registration.py  
Для запуска конкретного теста pytest -v tests/test_registration.py::test_fail_first_name_latin  

В корневой директории лежит файл settings.py - содержит информацию о валидном логине и пароле, также ссылки  
В директории /tests располагаеются файлы с тестами  
1. tests/test_login.py - проверки логина
- test_success_email_login - проверка успешного входа по email
- test_failed_email_login - проверка на ошибку при входе по email если пароль неверен
- test_success_phone_login - проверка успешного входа по телефонному номеру
- test_failed_phone_login - проверка на ошибку при входе по телефонному номеру если пароль неверен
- test_success_account_login - проверка успешного входа по аккаунту
- test_failed_account_login - проверка на ошибку при входе по аккаунту если пароль неверен
2. tests/test_login_links.py - проверка кнопок перехода на странице логина
- test_success_vk_link_redirect - проверка успешного редиректа на вход через vk
- test_success_ok_link_redirect - проверка успешного редиректа на вход через одноклассники
- test_success_mail_link_redirect - проверка успешного редиректа на вход через mail
- test_success_forgot_password_redirect - проверка успешного редиректа на восстановление пароля
3. tests/test_registration.py - проверка формы регистрации
- test_fail_first_name_short - проверка ошибки, если имя короткое
- test_fail_first_name_latin - проверка ошибки, если имя латиницей
- test_fail_last_name_short - проверка ошибки, если фамилия короткая
- test_fail_adress_text - проверка ошибки, если "Email или мобильный телефон" просто текст
- test_fail_adress_phone_long - проверка ошибки, если "Email или мобильный телефон" длинный номер
- test_fail_adress_phone_short - проверка ошибки, если "Email или мобильный телефон" короткий номер
- test_fail_password_short - проверка ошибки, если короткий пароль
4. tests/test_lk.py - проверка личного кабинета
- test_success_redirect_from_auth_profile_to_site - проверка в авторизованном профиле редиректа на Сайт Ростелекома
- test_success_redirect_from_auth_profile_to_lk - проверка в авторизованном профиле редиректа в личный кабинет
- test_success_logout - проверка логаута
- test_success_elements_menu - проверка в личном кабинете переходов по каждому элементу главного меню