from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site
driver = webdriver.Chrome()
driver.get('https://www.terabyteshop.com.br/monitores')

# extrair todos os titulos
titulos = driver.find_elements(By.XPATH, "//a[@class='prod-name']")
# extrair todos os preços
precos = driver.find_elements(By.XPATH, "//div[@class='prod-new-price']")

workbook = openpyxl.Workbook() #criando planilha
workbook.create_sheet('produtos') #criando pagina produtos
sheet_produtos = workbook['produtos'] #selecionando pagina
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B2'].value = 'Preço'




# inserir os titulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo,preco])

workbook.save('produtos.xlsx')

# como entregar para o cliente
