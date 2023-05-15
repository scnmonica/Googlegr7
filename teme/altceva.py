from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url_pattern = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/'
dates = ['01-03', '02-03', '03-03', '04-03', '05-03']

header = {'NR. CRT': [], 'Judet': []}
data = {}

for date in dates:
    header[date] = []
    data[date] = []

for i, date in enumerate(dates):
    url = url_pattern.format(date=date)
    driver.get(url)
    table = driver.find_element(by=By.XPATH, value='//*[@id="post-29587"]/div/div/table[1]')
    rows = table.find_elements(by=By.XPATH, value='.//tr')

    if i == 0:
        header['01-03'] = [td.text for td in rows[0].find_elements(by=By.XPATH, value='.//td')[1:]]

    for row in rows[1:]:
        cells = row.find_elements(by=By.XPATH, value='.//td')
        judet = cells[1].text
        values = [cell.text for cell in cells[2:]]
        if judet in header['Judet']:
            idx = header['Judet'].index(judet)
        else:
            header['Judet'].append(judet)
            header['NR. CRT'].append(str(len(header['Judet'])))
            idx = len(header['Judet']) - 1

        for j in range(i):
            if len(data[dates[j]]) < len(header['Judet']):
                data[dates[j]].append([''] * len(header['01-03']))

        data[date].append([values[0]] + values[2:])

for i in range(1, len(dates)):
    missing_dates = set(dates[:i]) - set(data.keys())
    for date in missing_dates:
        data[date] = [[''] * len(header['01-03'])] * len(header['Judet'])

df = pd.DataFrame(data=data['01-03'], columns=header['01-03'])
for date in dates[1:]:
    df_date = pd.DataFrame(data=data[date], columns=header['01-03'])
    df = pd.concat([df, df_date], ignore_index=True)

total_row = df.sum(numeric_only=True).tolist()
total_row.insert(0, 'Total')
df = df.append(pd.Series(total_row, index=df.columns), ignore_index=True)

df.to_excel('date.xlsx', index=False)
driver.quit()