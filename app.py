from selenium import webdriver #simulate brawser use
from selenium.webdriver.common.by import By #find informations 
import openpyxl #create workboot

driver = webdriver.Chrome() #variable for enable acess of chrome
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers') #command for open the site 

titles = driver.find_elements(By.XPATH, "//a[@class='nome-produto']") #variable for find the titles between the xpath
prices = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

workboot = openpyxl.Workbook() #create workboot
workboot.create_sheet('products') #create page

sheet_products = workboot['products']
sheet_products['A1'].value = 'product'
sheet_products['B1'].value = 'price'

for title, price in zip(titles, prices):
    sheet_products.append([title.text, price.text])

workboot.save('products.xlsx')