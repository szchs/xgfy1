##爬虫,爬取腾讯疫情肺炎数据
import requests
import pandas as pd
import json

url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
r = requests.get(url)
#print(r.text[0:1000])测试一下内容是否爬取正确
zzx1 = json.loads(r.text)
#print(zzx1'\nzzx1类型为',type(zzx1))  测试一下数据类型
df = pd.DataFrame(columns= ['国家或地区','新增病例','总确诊病例','死亡病例','治愈病例'])
for i in range(len(zzx1['data'])):
    df.loc[i+1]=[zzx1['data'][i]['name'],
                 zzx1['data'][i]['confirmAdd'],
                 zzx1['data'][i]['confirm'],
                 zzx1['data'][i]['dead'],
                 zzx1['data'][i]['heal']]
df.to_csv('E://英雄时刻/疫情数据.csv',index=0,encoding='utf_8_sig' )
print('爬取完毕')

