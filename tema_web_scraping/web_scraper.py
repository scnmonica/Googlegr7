from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

nr_crt = []
judet = []
intai = []
doi = []
trei = []
patru = []
cinci = []

url_1 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/'
driver.get(url_1)
rows = driver.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    nr_crt.append(row.find_element(by=By.XPATH, value='./td[1]').text)
    judet.append(row.find_element(by=By.XPATH, value='./td[2]').text)
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    intai.append(float(value))

url_2 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/'
driver.get(url_2)
rows = driver.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    doi.append(float(value))

url_3 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/'
driver.get(url_3)
rows = driver.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    trei.append(float(value))

url_4 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/'
driver.get(url_4)
rows = driver.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    patru.append(int(value))

url_5 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/'
driver.get(url_5)
rows = driver.find_elements(by=By.TAG_NAME, value='tr')[1:45]
for row in rows:
    value = row.find_element(by=By.XPATH, value='./td[3]').text
    value = re.sub(r'[^\d.]', '', value)
    cinci.append(float(value))

total_intai = sum(intai)
total_doi = sum(doi)
total_trei = sum(trei)
total_patru = sum(patru)
total_cinci = sum(cinci)

nr_crt.append('Total')
judet.append('')
intai.append(total_intai)
doi.append(total_doi)
trei.append(total_trei)
patru.append(total_patru)
cinci.append(total_cinci)

df = pd.DataFrame({'Nr. Crt': nr_crt, 'Judet': judet, '01.03': intai, '02.03': doi, '03.03': trei, '04.03': patru, '05.03': cinci})
df.to_excel('date_covid.xlsx', index=False)