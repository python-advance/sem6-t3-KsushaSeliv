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

... в процессе
