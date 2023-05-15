from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

path_list = ['//*[@id="post-29587"]/div/div/table[1]',
             '//*[@id="post-29627"]/div/div/table[1]',
             '//*[@id="post-29664"]/div/div/table[1]',
             '//*[@id="post-25709"]/div/div/table[1]',
             '//*[@id="post-29726"]/div/div/table[1]']
url_5 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/'
urls_list = []

for i in range(1, 5):
    url_pattern = f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-martie-ora-13-00-2/'
    urls_list.append(url_pattern)
    urls_list.append(url_5)

data = []

for url in urls_list:
    driver.get(url)

    for path in path_list:
        table = driver.find_element(by=By.XPATH, value=path)

        for tr in table.find_elements(by=By.XPATH, value='.//tr')[1:45]:
            row = [item.text for item in tr.find_elements(by=By.XPATH, value='.//td')[1:3]]
            data.append(row)

for row in data:
    print(row)

df = pd.DataFrame(data)
df.to_excel('date.xlsx')

driver.quit()
