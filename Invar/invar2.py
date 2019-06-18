#Применить шаблон проектирования «Декоратор» для реализации функционала, позволяющего преобразовывать данные о курсах валют в формат JSON.

import urllib.request #для URL
from xml.etree import ElementTree as ET #для XML файлов

def nerv(func):
  import functools #сборник функций высокого уровня: взаимодействующих с другими функциями или возвращающие другие функции
  import datetime #модуль datetime предоставляет классы для обработки времени и даты разными способами
  @functools.wraps(func) #оборачиваем функцию func
  def wrapper(calc):
      t = datetime.datetime.now()
      result = func(calc)
      t = datetime.datetime.now() - t

      with open('Record.json', 'a') as f:
            f.write("\n")
            f.write("_" * 20)
            f.write("\n")
            f.write("Переводим " + str(calc) + " " + str(in_type) + " в " + str(convert_to) + "\n")
            f.write("Результат: " + str(result) + " " + str(convert_to) +"\n")
            f.write("Время выполнения функции " +  str(t))
            f.write("\n")
      return result
  return wrapper  

print ("Конвертер")
calc = float(input("Сумма для перевода: "))
in_type = input("Из какой валюты выполняется конвертирование введённой суммы (rubl, dollar, euro, iena): ")
convert_to = input("В какую валюту перевести введённую сумму(rubl, dollar, euro, iena): ")

id_dollar = "R01235" #USD
id_euro = "R01239" #EUR
id_iena = "R01820" #GBP

valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")) #данные с сайта

#применяем декоратор
def convert(calc):
  for line in valuta.findall('Valute'):
    id_v = line.get('ID')
    if id_v == id_dollar:
        rub1 = line.find('Value').text
        print (rub1)
    elif id_v == id_euro:
        rub2 = line.find('Value').text
        print (rub2)
    elif id_v == id_iena:
        rub3 = line.find('Value').text
        print (rub3)
       
  rub1 = float(rub1.replace(',', '.'))
  rub2 = float(rub2.replace(',', '.'))
  rub3 = float(rub3.replace(',', '.'))

  if in_type == "rubl":
    if convert_to == "rubl":
      result = float (calc)
    elif convert_to == "dollar":
      result = float (calc) / rub1
    elif convert_to == "euro":
      result = float (calc) / rub2
    elif convert_to == "iena":
      result = float (calc) / rub3
   
  elif in_type == "dollar":  
    if convert_to == "rubl":
      result = float (calc) * rub1
    elif convert_to == "dollar":
      result = float (calc)
    elif convert_to == "euro":
      result = (float (calc) * rub1) / rub2
    elif convert_to == "iena":
      result = (float (calc) * rub1) / rub3

  elif in_type == "euro":  
    if convert_to == "rubl":
      result = float (calc) * rub2
    elif convert_to == "dollar":
      result = (float (calc) * rub2) / rub1
    elif convert_to == "euro":
      result = float (calc)
    elif convert_to == "iena":
      result = (float (calc) * rub2) / rub3

  elif in_type == "iena":  
    if convert_to == "rubl":
      result = float (calc) * rub3
    elif convert_to == "dollar":
      result = (float (calc) * rub3) / rub1
    elif convert_to == "euro":
      result = (float (calc) * rub3) / rub2
    elif convert_to == "iena":
      result = float (calc)     
  return result

result = convert(calc)

print (calc, in_type, " = ", result, convert_to)
