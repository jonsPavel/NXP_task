from datetime import datetime
from random import randint
from random import triangular

import matplotlib.pyplot as plt
import  numpy as np

def arr_for_month(min,avg,max)-> np.ndarray:
    size = 43200
    return np.random.triangular(min, avg, max, size)

class Temerature_for_year:
    # В силу того, что на складе отсутствуют обогреватели и они имеют большой объём,
    # допустим, что температура внутри здания ~ t снаружи
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


print(f'date - сейчас \t{datetime.now()}')
print(f'smpt - сейчас \t{get_stmp(datetime.now())}')
print(f'год  - сейчас \t{get_stmp(datetime.now())/31536000+1970}')




