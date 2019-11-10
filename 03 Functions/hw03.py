# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!
import csv
# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('ages.csv', encoding="utf-8-sig") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)

# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
#for al in ages_list:
    #print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')



# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
def filter_students_1(age):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    for al in ages_list:
        if "-" in al["Возраст"]:
            al["Возраст"] = al["Возраст"].split("-")[0]

        if al["Возраст"] == '' or al["Возраст"] == None:
            unknownage_count += 1
        else:
            if int(al["Возраст"]) <= age:
                under_list.append([al["Номер в списке"], al["Возраст"]])
            else:
                upper_list.append([al["Номер в списке"], al["Возраст"]])

    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, и подсчитать их количество

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию:
und_list, upp_list, unknwncount = filter_students_1(30)
# TODO 2: выведите результат:
print(f"Старше 30:{upp_list}")
print(f"Младше 30:{und_list}")
print(f"Не указали возраст:{unknwncount}")


# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
def filter_students_2(**kwargs):
    under_list = list()
    upper_list = list()
    unknownage_count = 0
    age_param = kwargs.get("age")
    # TODO 3: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, и измените ее так, чтобы она работала с параметрами **kwargs
    for al in ages_list:
        if al["Возраст"] == '' or al["Возраст"] == None:
            unknownage_count += 1
        else:
            if "-" in al["Возраст"]:
                al["Возраст"] = al["Возраст"].split("-")[0]
            if int(al["Возраст"]) <= age_param:
                under_list.append([al["Номер в списке"], al["Возраст"]])
            else:
                upper_list.append([al["Номер в списке"], al["Возраст"]])

    # TODO 4: получите остальные два параметра по аналогии:
    warn_if_toomany = kwargs.get("warn")
    show_average_param = kwargs.get("show_average")
    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, выполните соответствующую обработку. Например:
    if warn_if_toomany == True:
        summary_len = len(under_list) + len(upper_list)
        if summary_len < unknownage_count:
            print("Большая часть студентов не указала возраст!")
    # напишите здесь код проверки и вывод предупреждающего сообщения пользователю
    if show_average_param == True:
        concatenated = upper_list + under_list
        ages = [int(element[1]) for element in concatenated]

        avg = sum(ages)/len(ages)
        print("Средний возраст: " + str(avg))
    # напишите здесь код подсчета и вывода среднего значения возраста студентов

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию filter_students_2
und_list, upp_list, unknwncount = filter_students_2(age=30, warn=True, show_average=True)
