#https://sites.google.com/chromium.org/driver/  chromdriver 程式下載處



from selenium import webdriver



PATH="C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://ani.gamer.com.tw/")


titles=driver.find_elements_by_class_name("anime-name")
clicker=driver.find_element_by_xpath('//*[@id="blockVideoInSeason"]/div[2]/div/div[31]/span')
clicker.click()
print("本季新番:↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓") 
for title1 in titles:
    if title1.text!=None:
        print(title1.text)

titles=driver.find_elements_by_class_name("theme-name")
clicker=driver.find_element_by_xpath('//*[@id="blockAnimeNewArrive"]/div[3]/span')
clicker.click()
print("新上架:↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓") 
for title2 in titles:
   
        print(title2.text)


driver.quit()
