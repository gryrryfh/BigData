``` python 

# 공통 부분
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
raw_df = pd.read_csv('C:\data\owid-covid-data.csv')
selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
revised_df = raw_df[selected_columns]
kor_df = revised_df[revised_df.location == 'South Korea']
kor_date_index_df = kor_df.set_index('date')
kor_total_cases = kor_date_index_df['total_cases']
kor_population = kor_date_index_df['population']['2020-01-23']

raw_hawaii_df = pd.read_csv('C:\data\hawaii-covid-data.csv')
filtered_hawaii_df = raw_hawaii_df[['date_updated','tot_cases']]
sorted_hawaii_df = filtered_hawaii_df.sort_values(by='date_updated')
sorted_hawaii_df['date'] = pd.to_datetime(filtered_hawaii_df['date_updated'])
sorted_hawaii_df.sort_values(by='date', inplace=True)
sorted_hawaii_df.set_index('date', inplace=True)
hawaii_total_cases = sorted_hawaii_df['tot_cases']
hawaii_population = 1500800
hawaii_rate = round((hawaii_population / kor_population), 2)
kor_total_cases.index = kor_total_cases.index.astype('string')
hawaii_total_cases.index = hawaii_total_cases.index.astype('string')
from pandas import Series
revised_kor_df = kor_date_index_df['2020-01-23':]
revised_kor_index = revised_kor_df.index
revised_kor_total_cases = revised_kor_df['total_cases']
revised_final_kor_total_cases = Series(revised_kor_total_cases.values, index=revised_kor_total_cases.index)

# 하와이 주와 대한민국의 총 확진자 수 데이터가 데이터의 수도 다르며, 데이터를 이루는 일자(date) 또한 다름을 알 수 있습니다.
# 하와이 주의 데이터에 맞춰서 대한민국의 데이터를 추출하는 것입니다.
# 결과적으로 하와이 주와 대한민국의 데이터의 수와 각 데이터의 순서가 일자를 기준으로 정렬되어 있는 형태가 되어야 합니다

final_df = pd.DataFrame({
'KOR': revised_final_kor_total_cases * hawaii_rate,
'HAWAII' : hawaii_total_cases}, index=hawaii_total_cases.index)

final_df.plot.line(rot=45)
plt.tight_layout()
plt.show()
final_df['2023-01-01':].plot.line(rot=45)
plt.tight_layout()
plt.show()
```
