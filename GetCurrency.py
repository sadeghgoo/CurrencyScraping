from bs4 import BeautifulSoup
import requests
import json
import time
import schedule
import validators

class Get_price :

    # MARK - Initialize 
    def __init__(self,url:list,name_currency = 'unknown'):
        self.url = url
        self.name_currency = name_currency
        self.arry_price = list()
        self.price = list()

    # MARK - SAVE FILE WITH JSON FORMAT 
    def save_file(self,file_name):
        json_current_convert = json.dumps(self.price)
        file = open('dolor.json','w')
        file.write(json_current_convert)
        file.close()

        with open('dolor.json', 'w') as file:
            file.write(json_current_convert)
            print('json file saved ')

    # MARK - GET ARRAY OF PRICE AND SEPRATING THE STRING WITH ':'
    def seperate_dict(self):
        #len_array = len(self.arry_price)
        for price in self.arry_price:
            seperator = tuple(price.split(':'))
            self.price.append(seperator[1])
        
        print(f'{self.name_currency}:{self.price} \n --------------------------------------------')   
        self.price.clear()
        self.arry_price.clear()

    # MARK - SEND REQUEST AND FIND DIV THAT HAVE PRICE 
    def fetch_price(self):
           
        for url in self.url:
            if validators.url(url):
                page = requests.get(url)
                soup = BeautifulSoup(page.content,'html.parser')
                main_panel = soup.find('ul',class_='data-line float-right float-half')
                all_currency_dolor = main_panel.find_all('li')
                for currency in all_currency_dolor:

                    self.arry_price.append(currency.text)
                self.seperate_dict()
            else:
                raise TypeError('you must enter valid URL')


# CREATE OBJECT FOR TEST     
boj_test = Get_price(['tgju.org/chart/price_dollar_rl','http://www.tgju.org/chart/geram24'])
boj_test.fetch_price()

