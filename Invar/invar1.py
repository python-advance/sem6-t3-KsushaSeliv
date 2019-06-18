#1.Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием
#сервиса, который они предоставляют.Применить шаблон проектирования «Одиночка» для предотвращения отправки
#избыточных запросов к серверу ЦБ РФ.

from xml.etree import ElementTree as ET
from urllib.request import urlopen
import time

def dengi(lis=['R01235', 'R01239', 'R01820']):
  
    cursbank = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
    spis = {}
    xml = ET.parse(cursbank)
    root = xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        denid = el.get('ID')
        if str(denid) in lis:
            curden = el.find('Value').text
            spis[denid] = curden
    time.clock()
    return spis

class CurrencyBoard(): #Класс синглтон
    
    def __init__(self): 
        self.currencies = ['R01235','R01239','R01820']
        self.rates = dengi(self.currencies)

    def cache(self, code): #Получаем информацию о валютах из кэша без запроса к сайту
        return self.currencies[code]

    def info(self, code): #Получаем новую информацию о валютах
        self.currencies.append(code)
        self.rates.update(dengi([code]))
        return self.rates[code]

    def update(self): #Обновляем 

        new_val = dengi(self.currencies)
        self.rates.update(dict(zip(sorted(self.currencies),new_val.values())))
        return self.rates

    def timit(self): #Если проходит меньше 5 минут, данный о валютах берутся из кэша
        if (time.clock() > 5*60):
            return dengi(self.currencies)
        else:
            print('Не прошло и 5 минут с последнего обноаления')

cursnes = dengi()

print("\ndollar = USD = R01235 \neuro = EUR = R01239 \niena = GBP = R01820  \n", cursnes)
