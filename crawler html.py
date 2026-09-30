import urllib.request as req  #import urllib.request用來串連線網址
url="https://www.ptt.cc/bbs/movie/index9498.html" #ptt電影版含文章標題的html原始碼

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
})
#利用urllib.request中的req.Request方法代入網址(url)和標頭(headers User-Agent)
#目的在於模仿正常的使用者請求

with req.urlopen(request) as response: #對網址發出連線請求
    data=response.read().decode("utf-8")
#解析原始碼,取得每篇文章的標题
import bs4
root=bs4.BeautifulSoup(data, "html.parser")#讓BeautifulSoup協助
titles=root.find_all("div", class_="title")#找所有class-"title"
for title in titles:
    if title.a!= None:#如果题包含 a 標(沒有被剛除),印出来
        print(title.a.string)





    

