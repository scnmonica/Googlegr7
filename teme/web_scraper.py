from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url_5 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/'
urls_list = []
for i in range(1, 5):
    url_pattern = f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-martie-ora-13-00-2/'
    urls_list.append(url_pattern)
urls_list.append(url_5)

data = []
dates = ['01.03', '02.03', '03.03', '04.03', '05.03']

for url in urls_list:
    driver.get(url)

    for tr in driver.find_elements(by=By.XPATH, value='.//tr')[1:45]:
        row = [item.text for item in tr.find_elements(by=By.XPATH, value='.//td')[0:3]]
        data.append(row)

# for row in data:
#     print(row)
#
# df = pd.DataFrame({'Nr. Crt.': [], 'Judet': [], '01.03': [], '02.03': [], '03.03': [], '04.03': [], '05.03':[]})
# df.to_excel('date.xlsx')
#
# driver.quit()
data_dict = {'Nr. Crt.': [], 'Judet': []}

# Add columns for each date to the dictionary
for date in dates:
    data_dict[date] = []

for row in data:
    data_dict['Nr. Crt.'].append(row[0])
    data_dict['Judet'].append(row[1])
    for i, date in enumerate(dates):
        data_dict[date].append(row[i + 2] if i + 2 < len(row) else '')  # Handle incomplete rows

# Create the DataFrame using the dictionary
df = pd.DataFrame(data_dict)

# Save the DataFrame to an Excel file
df.to_excel('date.xlsx', index=False)

driver.quit()






