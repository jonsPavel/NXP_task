from datetime import datetime
from random import randint
from random import triangular
from random import choices

import matplotlib.pyplot as plt
import  numpy as np

def arr_for_month(min,avg,max)-> np.ndarray:
    SS_size = 43800
    return np.random.triangular(min, avg, max, SS_size).tolist()


class Temerature_for_year:
    jan = arr_for_month(-28, -6.7, 0)
    feb = arr_for_month(-12, -6.2, 2)
    march = arr_for_month(-6, 2.5, 10)
    apr = arr_for_month(-1, 5.4, 19)
    may = arr_for_month(2, 11.2, 19)
    june = arr_for_month(6, 14.44, 20)
    jule = arr_for_month(11, 18, 25)
    aug = arr_for_month(11, 18.5, 24)
    sent = arr_for_month(7, 12.8, 19)
    oct = arr_for_month(-1.5, 4.75, 12)
    nov = arr_for_month(-6, -1, 3)
    dec = arr_for_month(-6, -1.22, 3)

    year = jan + feb + march + apr + may + june + jule + aug + sent + oct + nov + dec


class Pressure_for_year:
    jan = arr_for_month(746.5, 764.2, 777.1)
    feb = arr_for_month(738.2, 763, 784.2)
    march = arr_for_month(742, 761, 773)
    apr = arr_for_month(743, 760, 772.6)
    may = arr_for_month(748, 761, 773)
    june = arr_for_month(744, 756, 765)
    jule = arr_for_month(749, 757.3, 763)
    aug = arr_for_month(752, 763.1, 773)
    sent = arr_for_month(749, 765.4, 783.2)
    oct = arr_for_month(732.4, 759, 776.5)
    nov = arr_for_month(739.9, 763.3, 775.3)
    dec = arr_for_month(735, 759.3, 774.3)

    year = jan + feb + march + apr + may + june + jule + aug + sent + oct + nov + dec


class Wet_for_year:
    jan = arr_for_month(67, 85, 98)
    feb = arr_for_month(63, 81, 92)
    march = arr_for_month(55, 74, 93)
    apr = arr_for_month(30, 66, 97.5)
    may = arr_for_month(30, 66, 89)
    june = arr_for_month(48, 69, 87)
    jule = arr_for_month(54, 72, 89)
    aug = arr_for_month(51, 75, 91)
    sent = arr_for_month(66, 80, 93)
    oct = arr_for_month(67, 82, 94)
    nov = arr_for_month(74, 86, 93)
    dec = arr_for_month(84, 86, 95)

    year = jan + feb + march + apr + may + june + jule + aug + sent + oct + nov + dec

def get_timestamp(year, month, day, hour, min, s):
    return datetime.timestamp(datetime(year, month, day, hour, min, s))

def get_stmp(date:datetime.date):
    return datetime.timestamp(date)

def get_date(tmstmp):
    return datetime.fromtimestamp(tmstmp).date()

stmp_start_2017=int(get_timestamp(2017, 0o1, 0o1, 0o0, 0o0, 0o0))
stmp_end_2017=int(get_timestamp(2018, 0o1, 0o1, 0o0, 0o0, 0o0))
print(stmp_start_2017)
print(stmp_end_2017)
print(stmp_end_2017-stmp_start_2017)


# i=stmp_start_2017
# count=0
# insert_snapshots=[]
#
# while i<stmp_end_2017:
#     insert_snapshots.append((i,1,Temerature_for_year.year[count],Pressure_for_year.year[count],Wet_for_year.year[count]))
#     count+=1
#     i+=60

def create_inserts():
    i = stmp_start_2017
    count = 0
    insert_snapshots = []

    while i < stmp_end_2017:
        insert_snapshots.append(
            (i, 1, Temerature_for_year.year[count], Pressure_for_year.year[count], Wet_for_year.year[count]))
        count += 1
        i += 60
    return insert_snapshots