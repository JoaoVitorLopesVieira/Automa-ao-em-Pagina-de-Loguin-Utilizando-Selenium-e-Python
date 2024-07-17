from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(r'C:\Users\User\Documents\TesteComSelenium\index.html')
sleep(2)
navegador.find_element('xpath','//*[@id="email"]').send_keys('joao@gmail.com')
sleep(2)
navegador.find_element('xpath','//*[@id="senha"]').send_keys('joao123')
sleep(2)
navegador.find_element('xpath', '//*[@id="loginForm"]/input[3]').click()
sleep(2)


sleep(5)