from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\zehan_lap\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')

try:
    driver.get('https://fitpeo.com/revenue-calculator')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    revenue_calculator_link = driver.find_element(By.LINK_TEXT, 'Revenue Calculator')
    revenue_calculator_link.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    slider_section = driver.find_element(By.ID, 'slider')
    driver.execute_script("arguments[0].scrollIntoView();", slider_section)

    slider = driver.find_element(By.XPATH, '//*[@id="slider"]')
    text_field = driver.find_element(By.XPATH, '//*[@id="text_field"]')
    text_field.clear()
    text_field.send_keys('560')

    assert slider.get_attribute('value') == '560'


    cpt_codes = ['CPT-99091', 'CPT-99453', 'CPT-99454', 'CPT-99474']
    for code in cpt_codes:
        checkbox = driver.find_element(By.XPATH, f'//input[@value="{code}"]')
        if not checkbox.is_selected():
            checkbox.click()

    total_reimbursement = driver.find_element(By.ID, 'total_reimbursement')
    assert total_reimbursement.text == '$110700'

finally:
    driver.quit()