import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()

#login
enter_Email_address = driver.find_element(By.ID, "email-id")
enter_Email_address.send_keys("chike@yahoo.com")
enter_Password = driver.find_element(By.CSS_SELECTOR, "#password")
enter_Password.send_keys("1234")
click_submit_button = driver.find_element(By.ID, "submit-id")
click_submit_button.click()
time.sleep(5)

#Click on New Customer Button
click_NewCustomer_button = driver.find_element(By.ID, 'new-customer')
click_NewCustomer_button.click()

#Add Customer Details
enter_email_address = driver.find_element(By.CSS_SELECTOR, '#EmailAddress')
enter_email_address.send_keys('chike@yahoo.com')

enter_firstname = driver.find_element(By.CSS_SELECTOR, '#FirstName')
enter_firstname.send_keys('Chy')

enter_Lastname = driver.find_element(By.ID,"LastName")
enter_Lastname.send_keys("Oma")

enter_city = driver.find_element(By.XPATH, '//*[@id="City"]')
enter_city.send_keys('Houston')

click_state_button = driver.find_element(By.CSS_SELECTOR, '#StateOrRegion')
click_state_button.click()

select_state = driver.find_element(By.XPATH, '//*[@id="StateOrRegion"]/option[46]')
select_state.click()

click_gender_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[2]')
click_gender_button.click()

click_promotional_list_button = driver.find_element(By.CSS_SELECTOR, '#loginform > div > div > div > div > form > div:nth-child(7) > input[type=checkbox]')
click_promotional_list_button.click()

click_submit_button = driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/button')
click_submit_button.click()

time.sleep(3)

#SignOut
click_sign_out_button = driver.find_element(By.CSS_SELECTOR,"body > nav > ul > li > a")
click_sign_out_button.click()

time.sleep(3)