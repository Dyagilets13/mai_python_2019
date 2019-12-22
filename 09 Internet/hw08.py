# ДЗ по теме "Работа с интернет-источниками"
# ваша задача - получить данные о воздушном флоте перечисленных ниже авиакомпаний (2 компании),
# аналогично тому, как это было на лекции
# 1) NordWind https://nordwindairlines.ru/ru/fleet
# 2) ЮТэйр https://www.utair.ru/about/aircrafts/

# TODO1: разработайте структуру данных, в которой вы сможете сохранить данные по воздушному флоту каждой из авиакомпаний
# например, это может быть словарь с ключами - названиями авиакомпаний и значениями - данными по воздушному флоту
# в любом случае, у вас получится сложная структура

# TODO2: напишите код парсеров данных о воздушном флоте для каждой из перечисленных авиакомпаний

# TODO3: сохраните полученные данные в структуру данных об авиакомпаниях Не забудьте добавить туда S7 и АК "Россия"
# если вас будет банить S7 так же, как на лекции, тогда добавьте только АК "Россия", без S7
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

url_nordwind = r'https://nordwindairlines.ru/ru/fleet'
url_utair = r'https://www.utair.ru/about/aircrafts/'
url_ros = r'https://www.rossiya-airlines.com/about/about_us/fleet/aircraft/'
url_s7 = r'https://www.s7.ru/ru/about/ourfleet.dot'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

keys = ['NordWind', 'UTAir', 'Rossiya', 'S7']
aircrafts = dict.fromkeys(keys, None)

try:
    print("Ищем самолеты компании NordWind\n")
    nw_aircrafts = []
    nw_request = requests.get(url_nordwind, headers=headers)
    nw_bs = BeautifulSoup(nw_request.text, "lxml")
    nw_a_bs = nw_bs.find_all("a", attrs={"class":"fleet__item-name-link"})

    for item in nw_a_bs:
        nw_aircrafts.append(item.text)

    print("Самолеты компании NordWind: ", ', '.join(nw_aircrafts))

    aircrafts["NordWind"] = nw_aircrafts
    print("\nЗакончили поиск самолетов компании NordWind\n")
except Exception as e:
    print(e)
    print("Не удалось найти информацию :(")

try:
    print("Ищем самолеты компании UTAir\n")
    ut_aircrafts = []
    ut_request = requests.get(url_utair, headers=headers)
    ut_bs = BeautifulSoup(ut_request.text, "lxml")
    ut_div_bs = ut_bs.find_all("div", attrs={"class":"airship-block"})

    for item in ut_div_bs:
        aircraft = item.find("a")
        ut_aircrafts.append(aircraft.text)

    print("Самолеты компании UTAir: ", ', '.join(ut_aircrafts))
    aircrafts["UTAir"] = ut_aircrafts
    print("\nЗакончили поиск самолетов компании UTAir\n")
except Exception as e:
    print(e)
    print("Не удалось получить информацию:(")

try:
    print("\nИщем самолеты компании Rossiya\n")
    ros_aircrafts = []
    ros_request = requests.get(url_ros, headers=headers)
    ros_bs = BeautifulSoup(ros_request.text, "lxml")
    ros_h2_bs = ros_bs.find_all("h2")

    for item in ros_h2_bs:
        aircraft = item.find("span")
        if aircraft != None:
            ros_aircrafts.append(aircraft.text)

    print("Самолеты компании Rossiya: ", ', '.join(ros_aircrafts))
    aircrafts["Rossiya"] = ros_aircrafts
    print("\nЗакончили поиск самолетов компании Rossiya\n")

except Exception as e:
    print(e)
    print("Не удалось получить информацию:(")

try:
    print("\nИщем самолеты компании S7\n")
    s7_aircrafts = []
    s7_request = requests.get(url_s7, headers=headers)
    s7_bs = BeautifulSoup(s7_request.text, "lxml")
    s7_h3_bs = s7_bs.find_all("h3")

    for item in s7_h3_bs:
        if "Схема" not in str(item):
            s7_aircrafts.append(item.text)

    print("Самолеты компании S7: ", ', '.join(s7_aircrafts))
    aircrafts["S7"] = s7_aircrafts
    print("\nЗакончили поиск самолетов компании S7\n")
except Exception as e:
    print(e)
    print("Не удалось получить информацию:(")

print("Итог:")
for k,v in aircrafts.items():
    print("{0} : {1}".format(k, ', '.join(v)))
