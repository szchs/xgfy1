## -*-  coding: utf-8  -*-
##爬取百度文库的VIP免费文档内容
import requests
import re
import json
import time
import fitz
import os
#获取json，先找到数据网址
url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=d0f68b6ef021dd36a32d7375a417866fb94ac0f2&pn=1&rn=99999&type=ppt&callback=&_=1587552604162'
#包含参数 doc_id  pn=1&rn=99999  type=ppt  callback 时间戳&_=1587532896439
def wenku_js(url):
    res = requests.get(url)
    res_js = res.text
    #print(res.text)  看看是否为json类型
    zzx2 = json.loads(res_js)
    return zzx2
zzx1 = wenku_js(url)
#print(zzx1,type(zzx1))  测试zzx1的数据类型

doc = fitz.open()  #创建一个空的pdf文件

for i in range(len(zzx1)):
    img1 = zzx1[i]['zoom']
    #print(img1)#打印出来的是每个ppt的图片，还需进一步转化成pdf图片
    img_res = requests.get(img1)
    print(img1[:77],img_res.status_code)
    with open(str(i)+'.jpg','wb') as f:
        f.write(img_res.content)
    #图片写入pdf文件
    img_doc = fitz.open(str(i)+'.jpg')
    pdfbytes = img_doc.convertToPDF()#图片转化为pdf流
    imgpdf = fitz.open('pdf',pdfbytes)
    doc.insertPDF(imgpdf)
    os.remove(str(i)+'.jpg')#删除图片，只保留pdf文件
doc.save('E://英雄时刻/121/百度文库.pdf')
doc.close()
print('pdf文件爬取完毕')