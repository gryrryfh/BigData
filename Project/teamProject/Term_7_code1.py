######################
# 전국 사고율 그래프 코드
######################
import os
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

years = range(2013, 2022 + 1)
cu_dir = os.getcwd()


def city_accident_rate(city, year):

    split_accident1 = accident.iloc[1:19, 7]
    split_accident2 = accident.iloc[1:19, 0]
    filtered_accident = pd.concat([split_accident1, split_accident2], axis=1)
    filtered_accident.columns = ['사고수', '시도']
    filtered_accident['사고수'] = filtered_accident['사고수'].str.replace(',', '')
    filtered_accident['사고수'] = filtered_accident['사고수'].astype('float64')
    filtered_accident['년도'] = year
    filtered_accident.set_index('시도', inplace=True)
    filtered_accident = filtered_accident.dropna()

    split_car1 = car.iloc[4:22, 21]
    split_car2 = car.iloc[4:22, 0]
    concat_car = pd.concat([split_car1, split_car2],axis=1)
    filtered_car = pd.DataFrame({
        '시도': concat_car['Unnamed: 0'],
        '계': concat_car['Unnamed: 21']
    }, index=concat_car.index)

    filtered_car['계'] = filtered_car['계'].str.replace(',', '')
    filtered_car['계'] = filtered_car['계'].astype('float64')
    filtered_car.set_index('시도', inplace=True)
    filtered_car = filtered_car.dropna()

    accident_rate = pd.concat([filtered_accident, filtered_car], axis=1)
    accident_rate['사고율'] = filtered_accident['사고수'].div(filtered_car['계'])

    filtered_city = accident_rate.loc[[city], ['사고율', '년도']]

    city_index = filtered_city.set_index('년도', inplace=True)
    city_df = pd.DataFrame({
        city: filtered_city['사고율']
    }, index=city_index)

    return city_df

##################################################
# 도시목록
##################################################
# 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종
# 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주
##################################################

seoul_final = pd.DataFrame()
busan_final = pd.DataFrame()
Daegeon_final = pd.DataFrame()
Incheon_final = pd.DataFrame()
Ulsan_final = pd.DataFrame()
Gwangju_final = pd.DataFrame()
Daegu_final = pd.DataFrame()
Gyeonggi_final = pd.DataFrame()

# sejong_final = pd.DataFrame()
# gangwon_final = pd.DataFrame()
# chungbuk_final = pd.DataFrame()
# chungnam_final = pd.DataFrame()
# junbuk_final = pd.DataFrame()
# junnam_final = pd.DataFrame()
# geungbuk_final = pd.DataFrame()
# geungnam_final = pd.DataFrame()
# jeju_final = pd.DataFrame()

korea_final = pd.DataFrame()


for year in years:
    path_accident = f'{cu_dir}\\data\\{year}_accident.csv'
    path_car = f'{cu_dir}\\data\\{year}_car.csv'
    accident = pd.read_csv(path_accident, encoding='CP949')
    car = pd.read_csv(path_car, encoding='CP949')

    seoul_final = pd.concat([seoul_final, city_accident_rate('서울', year)])
    busan_final = pd.concat([busan_final, city_accident_rate('부산', year)])
    Daegeon_final = pd.concat([Daegeon_final, city_accident_rate('대전', year)])
    Incheon_final = pd.concat([Incheon_final, city_accident_rate('인천', year)])
    Ulsan_final = pd.concat([Ulsan_final, city_accident_rate('울산', year)])
    Gwangju_final = pd.concat([Gwangju_final, city_accident_rate('광주', year)])
    Daegu_final = pd.concat([Daegu_final, city_accident_rate('대구', year)])
    Gyeonggi_final = pd.concat([Gyeonggi_final, city_accident_rate('경기', year)])

    # sejong_final = pd.concat([sejong_final, city_accident_rate('세종', year)])
    # gangwon_final = pd.concat([gangwon_final, city_accident_rate('강원', year)])
    # chungbuk_final = pd.concat([chungbuk_final, city_accident_rate('충북', year)])
    # chungnam_final = pd.concat([chungnam_final, city_accident_rate('충남', year)])
    # junbuk_final = pd.concat([junbuk_final, city_accident_rate('전북', year)])
    # junnam_final = pd.concat([junnam_final, city_accident_rate('전남', year)])
    # geungbuk_final = pd.concat([geungbuk_final, city_accident_rate('경북', year)])
    # geungnam_final = pd.concat([geungnam_final, city_accident_rate('경남', year)])
    # jeju_final = pd.concat([jeju_final, city_accident_rate('제주', year)])

    korea_final = pd.concat([korea_final, city_accident_rate('합계', year)])

total_accident = pd.concat(
    [seoul_final, busan_final, Daegeon_final, Incheon_final, Ulsan_final, Gwangju_final, Daegu_final, Gyeonggi_final],
    axis=1)

# total_accident2 = pd.concat(
#     [sejong_final, gangwon_final, chungbuk_final, chungnam_final, junbuk_final, junnam_final, geungbuk_final, geungnam_final, jeju_final],
#     axis=1)

total_accident.plot.line()
# total_accident2.plot.line()
korea_final.plot.line()

plt.show()

