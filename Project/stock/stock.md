from prophet import Prophet
import pandas as pd
import requests
new_url = 'https://finance.naver.com/item/sise_day.naver?code=252670&page='
my_headers = {'user-agent' : 'Mozilla/5.0'}
all_tables_year = pd.DataFrame()
for page_number in range(1, 178):full_url = new_url + str(page_number)
print(f'{page_number} 번째 페이지 읽어오기({full_url})')
page = requests.get(full_url, headers=my_headers)
table = pd.read_html(page.text)[0]
print(f'전체 {len(all_tables_year.index)} 줄에{len(table.index)}줄 추가')
all_tables_year = pd.concat([all_tables_year, table])
