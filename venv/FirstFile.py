"""
1. Задаём даты пребывания в ЕС и другие исходные
2. Смотрим, в какую дату мы были больше 90 дней, сразу говорим, что так нельзя.
3. Смотрим, от даты выезда первой поездки на 180 дней назад.
4. Суммируем всё что есть в эти 180 дней
5. Смторим дату выезда второй поездки, смотрим на 180 дней назад.
6. Суммруем все поездки за эти 180 дней.
7. Если сумма поездок превышает 90 дней, сообщаем об этом и говорим на сколько дней превышено время прибывания.
"""

shengen_window = 180
residents = 90

visits = [[1,9], [20, 51], [50, 98], [200, 250], [310, 399]]

#Продолжительность каждого визита
list_time_visits = []
count_visit = 0
print('Даты поездок:', visits)
for time_one_visit in visits:
    count_visit += 1
    time_visit = 0
    time_visit = time_one_visit[1] - time_one_visit[0] + 1
    list_time_visits.append(time_visit) #Создали список с продолжительностью каждой поездки
    print('Визит №',count_visit, '=', time_visit, 'дней')


#Есть ли визиты длиннее 90 дней?
count_visit = 0
for check_time in list_time_visits:
    erorr_residents = False
    count_visit += 1
    if check_time > residents:
        print('Визит №',count_visit, 'длится', check_time, 'дней, и первышает лимит на', check_time - residents, 'дней')
        erorr_residents = True

if erorr_residents == False:
    print('Визитов с превышением в', residents, 'дней не обнаружено')

#Находим окно в 180 дней от даты выезда первой поездки
#Находим поездки в этом окне
#Складываем время поездок
#Если оно меньше 90, то ок
#Если больше 90, то показать на какое время сократить первую поездку
#Переходим к второй поездке
#Откладываем 180 дней, складываем всё что раньше, проверка на 90 дней

count_visit = 0
for done_window in visits:
    count_visit += 1
    start_window = done_window[1] - shengen_window #Нашли дату начала окна

    list_days_in_window = []
    all_time_in_window  = 0
    erorr_window = False
    for in_window in visits: #Находим поездки в окне и их длительность

        if start_window <= in_window[0] and in_window[1] <= done_window[1]:
            var_days_in_window = in_window[1] - in_window[0] + 1
            list_days_in_window.append(var_days_in_window)

    all_time_in_window = sum(list_days_in_window) #Складываем длительность поездок

    if all_time_in_window <= residents:
        #print('Время пребывания не нарушено, вы можете пробыть в этом окне ещё', residents - all_time_in_window, 'дней')
        print('Визит:', count_visit, '— Ок')
    else:
        print('Визит:', count_visit, '— Время пребывания в окне:', all_time_in_window, 'дней')
        corect_start = 0
        if start_window < 0:
            corect_start = 0
        else:
            corect_start = start_window
        print('Сократите время прибывания в интервале дат:', corect_start, '—', done_window[1])
        print('Минимальное время сокращения:', all_time_in_window - residents, 'дней.')
        erorr_window = True

if erorr_window == False:
    print('Все визиты укаладываются в', residents, 'дней, за последние',shengen_window, 'дней.')
