import csv

# читаем информацию о квартирах в список flats_list
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

# убираем заголовок
header = flats_list.pop(0)

# создаем словарь с информацией о квартирах
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	subway_dict.setdefault(subway, [])

# TODO 1: добавьте код, который генерирует новую структуру данных с информацией о квартире - словарь вместо списка
    # ваш код...
    # не забудьте сделать проверку типа и преобразовать то, что можно, в числа
	for value in flat:
	    if isinstance(value, int):
		    value = int(value)
	    elif isinstance(value, float):
		    value = float(value)

	flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
	subway_dict[subway].append(flat_info)



print(subway_dict)

# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте вариант прохода по словарю, который вам больше нравится
for k,v in subway_dict.items():
    flats_number = len(v)
    print("На станции метро " + k + " - " + str(flats_number) + " квартир.")
