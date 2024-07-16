#################################
# 전국 신호위반 단속 카메라 개수 그래프
#################################

import pandas as pd
import matplotlib.pyplot as plt
import os
plt.rcParams["font.family"] = "Malgun Gothic"
cu_dir = os.getcwd()  # current working directory

path = f'{cu_dir}\\data\\cctv.csv'
cctv = pd.read_csv(path, encoding='CP949')

restricted_cctv = cctv[['시도명', '설치연도', '단속구분']]
restricted_cctv = restricted_cctv.dropna(axis=0)
restricted_cctv = restricted_cctv[(restricted_cctv['단속구분'] == "01+02") | (restricted_cctv['단속구분'] == "2") |
                                  (restricted_cctv['단속구분'] == 2) | (restricted_cctv['단속구분'] == "02")]
restricted_cctv = restricted_cctv[['시도명', '설치연도']]


def group_cctv(year):
    cctv_year = restricted_cctv[restricted_cctv['설치연도'] <= year]
    grouped_cctv = cctv_year.groupby('시도명').size()
    grouped_cctv = grouped_cctv.rename('CCTV 개수').reset_index()
    grouped_cctv['연도'] = year
    grouped_cctv.loc[len(grouped_cctv)] = ['도시합계',  grouped_cctv['CCTV 개수'].sum(), year]

    return grouped_cctv


def city_final(city):
    city_cctv = total_cctv[total_cctv['시도명'] == city]
    city_cctv = city_cctv[['CCTV 개수']]
    return city_cctv


total_cctv = pd.concat(
    [group_cctv(2013), group_cctv(2014), group_cctv(2015), group_cctv(2016), group_cctv(2017),
     group_cctv(2018), group_cctv(2019), group_cctv(2020), group_cctv(2021), group_cctv(2022)])
total_cctv = total_cctv.set_index('연도')


##################################################################
# 도시목록 #
##################################################################
# 강원도, 강원특별자치도, 경기도, 경상남도, 경상북도, 광주광역시
# 대구광역시, 대전광역시, 부산광역시, 서울특별시, 세종특별자치시, 울산광역시
# 인천광역시, 전라남도, 전라북도, 제주특별자치도, 충청남도, 충청북도
###################################################################

Seoul_final = city_final('서울특별시')
Busan_final = city_final('부산광역시')
Daegeon_final = city_final('대전광역시')
Incheon_final = city_final('인천광역시')
Ulsan_final = city_final('울산광역시')
Gwangju_final = city_final('광주광역시')
Daegu_final = city_final('대구광역시')
Gyeonggi_final = city_final('경기도')
# Gangwon_final = city_final('강원도')
# GangwonSpecial_final = city_final('강원특별자치도')
# GeungNam_final = city_final('경상남도')
# GeungBuk_final = city_final('경상북도')
# Sejong_final = city_final('세종특별자치시')
# JunNam_final = city_final('전라남도')
# JunBuk_final = city_final('전라북도')
# ChungBuk_final = city_final('충청북도')
# ChungNam_final = city_final('충청남도')
# Jeju_final = city_final('제주특별자치도')

City_sum = city_final('도시합계')

cctv_df = pd.DataFrame({
    '서울': Seoul_final['CCTV 개수'],
    '부산': Busan_final['CCTV 개수'],
    '대전': Daegeon_final['CCTV 개수'],
    '인천': Incheon_final['CCTV 개수'],
    '울산': Ulsan_final['CCTV 개수'],
    '광주': Gwangju_final['CCTV 개수'],
    '대구': Daegu_final['CCTV 개수'],
    '경기도': Gyeonggi_final['CCTV 개수'],
}, index=City_sum.index)

# cctv_df2 = pd.DataFrame({
#     '강원도': Gangwon_final['CCTV 개수'],
#     '강원특별': GangwonSpecial_final['CCTV 개수'],
#     '경상남도': GeungNam_final['CCTV 개수'],
#     '경상북도': GeungBuk_final['CCTV 개수'],
#     '세종': Sejong_final['CCTV 개수'],
#     '전라남도': JunNam_final['CCTV 개수'],
#     '전라북도': JunBuk_final['CCTV 개수'],
#     '충청북도': ChungBuk_final['CCTV 개수'],
#     '충청남도': ChungNam_final['CCTV 개수'],
#     '제주': Jeju_final['CCTV 개수']
# }, index=City_sum.index)

korea_df = pd.DataFrame({
    '도시합계': City_sum['CCTV 개수']
}, index=City_sum.index)

cctv_df.plot.line(rot=45)
korea_df.plot.line(rot=45)
# cctv_df2.plot.line(rot=45)

plt.show()


