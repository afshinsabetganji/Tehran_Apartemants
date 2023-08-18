import time
import requests



data= {"json_schema":{"category":{"value":"apartment-sell"},"districts":{"vacancies":["85"]},"sort":{"value":"sort_date"},"cities":["1"]},"last-post-date":1692181133088754}
#data = {"json_schema":{"category":{"value":"apartment-sell"},"districts":{"vacancies":["315"]},"sort":{"value":"sort_date"},"cities":["1"]},"last-post-date":1692170907648220}
# {"json_schema":{"category":{"value":"apartment-sell"},"districts":{"vacancies":["936"]},"cities":["1"]},"last-post-date":1664607700661411}

url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'

header = {
    "Contet-type": "application/json"
}



res = requests.post(url, json=data, headers=header)
time.sleep(1.0)
print(res.status_code)
data = res.json()
last_post_date = data['last_post_date']
count = 0
listoftokens = []
while data['last_post_date']!=-1:
    try:
        json = {"json_schema":{"category":{"value":"apartment-sell"},"districts":{"vacancies":["85"]},"sort":{"value":"sort_date"},"cities":["1"]},"last-post-date":last_post_date}
        res = requests.post(url, json=json, headers=header)
        data = res.json()
        last_post_date = data['last_post_date']
        
    except ConnectionError :
        print('connection is lost  i try to reconnecting...')
        continue

props=[]
for item in data['web_widgets']['post_list']:
    token = item['data']['token']
    listoftokens.append(token)
    count += 1
    print (count,token)

txtfile = open('txts/elahiyeh.txt', 'w', encoding='utf8')
txtfile.write(','.join(listoftokens))
txtfile.close()
print (count,listoftokens[count-1])
