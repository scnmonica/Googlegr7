import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# URL-urile paginilor pe care dorim să le vizităm
urls = [
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/",
    "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/"
]

# Lista de liste pentru stocarea datelor
data = [["Judet", "01.03", "02.03", "03.03", "04.03", "05.03"]]

# Parcurgem fiecare URL și extragem datele
for url in urls:
    driver.get(url)

    # Așteptăm ca tabelul să fie încărcat în pagină
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Identificăm tabelul cu datele
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Parcurgem fiecare rând din tabel, ignorând antetele
    for row in rows[1:]:
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 6:
            row_data = [columns[0].text, columns[1].text, columns[2].text, columns[3].text, columns[4].text, columns[5].text]
            data.append(row_data)

    time.sleep(1)  # Pauză de 1 secundă între fiecare URL

# Închidem driverul
driver.quit()

# Creăm un nou fișier Excel
wb = Workbook()
ws = wb.active

# Adăugăm valorile din data în fișierul Excel
for row in data:
    ws.append(row)

# Salvăm fișierul Excel
wb.save("date_covid.xlsx")