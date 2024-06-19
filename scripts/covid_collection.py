import requests
import pandas as pd

url_covid = 'https://storage.covid19datahub.io/latest.db.gz'

response = requests.get(url_covid)

if response.status_code == 200:
    data = response.json()
    df_covid = pd.DataFrame([data])
    print('COVID-19 data collected successfully')
    print(df_covid)
else:
    print('Failed to obtain COVID-19 data:', response.status_code)
