from selenium import webdriver
import time

driver = webdriver.Firefox(
    executable_path='D:/2021/Python/Selenium/geckodriver.exe')

# Website URL
driver.get('https://iporesult.cdsc.com.np/')

# BOID
boid = 1234567891011121

# XPaths
company_xpath = driver.find_element_by_xpath(
    '/html/body/app-root/app-allotment-result/div/div/div/div/form/div[1]/select/option[10]')
boid_xpath = driver.find_element_by_xpath('//*[@id="boid"]')
submit_xpath = driver.find_element_by_xpath(
    '/html/body/app-root/app-allotment-result/div/div/div/div/form/button')
result_xpath = driver.find_element_by_xpath(
    '/html/body/app-root/app-allotment-result/div/div/div/div/form/p[2]')

# Operations
time.sleep(5)
company_xpath.click()
boid_xpath.send_keys(boid)
submit_xpath.click()

print("")
print(result_xpath.text)
print("")

driver.quit()
