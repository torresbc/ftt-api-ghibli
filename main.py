import requests
import json
import pandas


req = None
try:
    req = requests.get('https://ghibliapi.herokuapp.com/films')
except:
    print('Erro na conexão http!')
    exit()

list = json.loads(req.text)

title_list = []
description_list = []
director_list = []
releasedate_list = []
rtscore_list = []

for dict in list:
    title_list.append((dict['title']))
    description_list.append((dict['description']))
    director_list.append((dict['director']))
    releasedate_list.append((dict['release_date']))
    rtscore_list.append((dict['rt_score']))

df = pandas.DataFrame(
    {'Title': title_list,
     'Description': description_list,
     'Director': director_list,
     'Release Date': releasedate_list,
     'Rt Score': rtscore_list
     })

df.to_csv('ghibli-api.csv', index=False)
