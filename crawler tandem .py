import urllib.request as req #import urllib.request用來串連線網址
import json #import json 用來解碼json格式的資料
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
     #台北市內湖科技園區廠商名錄資料(API網址)為json資料格式

with req.urlopen(src) as response: # 利用with req.urlopen串接資料
    data=json.load(response)#利用json模組處理json

clist=data["result"]["results"]#分析出資料所在字典的鍵值
with open("data.txt", "w",encoding="utf-8" ) as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
#最後利用with open寫法 和for迴圈將資料打包成.txt文字檔