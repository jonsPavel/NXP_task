from datetime import datetime
from random import randint
from random import triangular
from random import choices

import matplotlib.pyplot as plt
import  numpy as np
#
#
#
#
#
#

class Day_times_for_month:
    size = int
    def __init__(self,values_for_month:np.ndarray):
        self.sort_values = values_for_month.sort()
        size = len(values_for_month)

        self.dx_hour = size / 12
    #     т.к. ожидается, что значения в 13:30 +6ч и -6ч (6:30 и 19:30) совпадают


    def get_time_values(self):
        time_values=[]
        time_values.append(choices(self.sort_values[], k=60))

    def get_val_from_arr(self,time:float):

        if (time>13.5):
            offset_time =abs(13.5-time)
        else:
            if (time<1.5):
                offset_time = 1.5-time
            else:
                offset_time = time - 1.5
        time_values = []
        time_values.append(choices(self.sort_values[offset_time:offset_time*dx], k=60))




def sort_for_days(ss_time_list,temp_list,press_list,wet_list):
#     key= SnapShot_time
#     val= Temp,press,wet
    dict={}
    for i in range(ss_time_list):

        dict[ss_time_list[i]]=[temp_list]


def sort_day(ss_time_list,temp_list,press_list,wet_list):
    for i in range()

# WORK
def arr_for_month(min,avg,max)-> np.ndarray:
    SS_size = 43800
    return np.random.triangular(min, avg, max, SS_size)

# WORK
class Temerature_for_year:
    # В силу того, что на складе отсутствуют обогреватели и они имеют большой объём,
    # допустим, что температура внутри здания ~ t снаружи
    #
    sec_in_month = 2628000
    SS_in_month = 31536000 / 12 / 60

    jan = list(arr_for_month(-12, -7.8, 5.4))
    feb = list(arr_for_month(-11, -4.6, -2.1))
    march = list(arr_for_month(-9, -0.7, 5.4))
    apr = list(arr_for_month(1.8, 5.3, 8.9))
    may = list(arr_for_month(6.3, 11, 15.7))
    june = list(arr_for_month(10.5, 14.4, 18.1))
    jule = list(arr_for_month(14.1, 17.9, 21.9))
    aug = list(arr_for_month(14.5, 18.8, 23.1))
    sent = list(arr_for_month(9.1, 13, 13.8))
    oct = list(arr_for_month(3.4, 5, 6.8))
    nov = list(arr_for_month(-1.3, 0, 1.4))
    dec = list(arr_for_month(-6.5, 0, 1.1))

    year = jan + feb + march + apr + may + june + jule + aug + sent + oct + nov + dec




class Pressure_for_year:
# Атм. д. в 760 мм.рт.ст. = 1013, 25 гПа = 1013, 25

    jan=arr_for_month(-12,-7.8,5.4)
    feb =arr_for_month(-11,-4.6,-2.1)
    march=arr_for_month(-9,-0.7,5.4)
    apr=arr_for_month(1.8,5.3,8.9)
    may=arr_for_month(6.3,11,15.7)
    june=arr_for_month(10.5,14.4,18.1)
    jule=arr_for_month(14.1,17.9,21.9)
    aug=arr_for_month(14.5,18.8,23.1)
    sent=arr_for_month(9.1,13,13.8)
    oct=arr_for_month(3.4,5,6.8)
    nov=arr_for_month(-1.3,0,1.4)
    dec=arr_for_month(-6.5,0,1.1)






def gen_T(timestamp:int):
        date = get_date(timestamp)
        # print(date.)


def get_timestamp(year, month, day, hour, min, s):
    return datetime.timestamp(datetime(year, month, day, hour, min, s))

def get_stmp(date:datetime.date):
    return datetime.timestamp(date)

def get_date(tmstmp):
    return datetime.fromtimestamp(tmstmp).date()

sec_2017=31536000
stmp_start_2017=get_timestamp(2017, 0o1, 0o1, 00, 00, 00)
stmp_end_2017=get_timestamp(2017, 12, 31, 23, 59, 59)

dx = Temerature_for_year.sec_in_month/Temerature_for_year.SS_in_month
print(f'Один снапшот описывает {dx} времени')

print(f'В 2017 - {sec_2017}c.')
print(f'Начало 2017 - {stmp_start_2017}c. stmp')
# print(f'Вычисленное значение sec_2017 = {}c. ')
print(f'Разница: {sec_2017/(stmp_end_2017-stmp_start_2017)}')

print(f'date - сейчас \t{datetime.now()}')
print(f'smpt - сейчас \t{get_stmp(datetime.now())}')
print(f'год  - сейчас \t{get_stmp(datetime.now())/31536000+1970}')

# На основе разных оценочных мнений, будем считать, что пик температуры дня наблюдается в 13:30
# На основе разных оценочных мнений некоторой выборочной статистике,
# будем считать, что минимум температуры наблюдается в 01:30




# WORK
def time_to_list_offset(time:float):
    if (time>13.5):
    	if (time<15):
    		offset_time =12-(time-13.5)
    	else:
    		offset_time =13.5-(time-13.5)
        # offset_time =-13.5+time
    else:
        if (time<1.5):
            offset_time = 1.5-time
        else:
            offset_time = time - 1.5
    return offset_time


def values_for_day(list_values:list):
    i=0
    SS_for_day=[]
    list_values=list_values.sort()
    while i<24:
        SS_for_day.append(choices(list_values[time_to_list_offset(i):time_to_list_offset(i+1)], k=60))
        i+=1
    return SS_for_day



print(time_to_list_offset(0))
print(time_to_list_offset(2))
print(time_to_list_offset(4))
print(time_to_list_offset(6))

print(time_to_list_offset(10))
print(time_to_list_offset(14))
print(time_to_list_offset(18))
print(time_to_list_offset(20))
print(time_to_list_offset(24))

