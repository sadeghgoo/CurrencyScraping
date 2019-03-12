from bs4 import BeautifulSoup
import requests
import json
import time
import schedule
print('hello worls')
class Get_price :

    #MARK - Initialize 
    def __init__(self,url:list,name_currency):
        self.url = url
        self.name_currency = name_currency
        self.arry_price = list()
        self.price = list()

    #MARK - SAVE FILE WITH JSON FORMAT 
    def save_file(self,file_name):

        json_current_convert = json.dumps(self.price)
        file = open('dolor.json','w')
        file.write(json_current_convert)
        file.close()

        with open('dolor.json', 'w') as file:
            file.write(json_current_convert)
            print('json file saved ')

    #MARK - GET ARRAY OF PRICE AND SEPRATING THE STRING WITH ':'
    def seperate_dict(self):
        for price in self.arry_price:
            seperator = tuple(price.split(':'))
            self.price.append(seperator[1])

        print(f'{self.name_currency}:{self.price} \n --------------------------------------------')   
         

    #MARK - SEND REQUEST AND FIND DIV THAT HAVE PRICE 
    def fetch_price(self):
        #TODO:create array of url 
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content,'html.parser')
        main_panel = soup.find('ul',class_='data-line float-right float-half')
        all_currency_dolor = main_panel.find_all('li')
        
        for currency in all_currency_dolor:

            self.arry_price.append(currency.text)

        self.seperate_dict()
        
# CREATE OBJECT FOR TEST     
boj_test = Get_price('http://www.tgju.org/chart/price_dollar_rl','dolor')
boj_test.fetch_price()
boj_test_2 = Get_price('http://www.tgju.org/chart/geram24','Gold')
boj_test_2.fetch_price()

