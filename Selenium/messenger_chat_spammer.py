from selenium import webdriver
import time

driver = webdriver.Firefox(
    executable_path='D:/2021/Python/Selenium/geckodriver.exe')

driver.get('https://www.facebook.com/messages/t')

# Login Credentials
id = 9811111111
password = "password"

# Facebook Name of the target
target_name = 'Subarna Poudel'

# Login
driver.find_element_by_xpath('//*[@id="email"]').send_keys(id)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

time.sleep(25)

# Searching the person
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input').send_keys(target_name)
time.sleep(10)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a').click()

# Writing and sending the message
time.sleep(5)
for i in range(1, 101):
    # Writing
    driver.find_element_by_css_selector(
        '.notranslate').send_keys(f"{i}. I did it.")

    # Sending
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div').click()

# driver.quit()
