from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho do ChromeDriver
CAMINHO_CHROMEDRIVER = '/Users/gusta/Downloads/chromedriver'

# Configurar o WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=Service(CAMINHO_CHROMEDRIVER), options=options)
driver.get("https://statusinvest.com.br/fundos-imobiliarios/busca-avancada")

wait = WebDriverWait(driver, 20)

# Aceitar cookies se aparecer
try:
    aceitar_cookies = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    aceitar_cookies.click()
except:
    pass  # Ignora se não aparecer

# Clicar no botão "Buscar"
buscar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Buscar')]")))
buscar_btn.click()

# Espera os resultados carregarem (ajuste conforme necessário)
time.sleep(5)

# Clicar no botão "Download"
download_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Download')]")))
download_btn.click()

# Esperar um pouco para o download iniciar
time.sleep(5)

# Fechar o navegador
driver.quit()
