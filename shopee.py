import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from pyquery import PyQuery as pq
from time import sleep
import pandas as pds
import matplotlib.pyplot as plt
redata = [] #記錄資料
position = {} # 地點
average = {}
driver = webdriver.Chrome("chromedriver")
product=input("What do you want? ")
#while True:
#    try: 
driver.get("https://shopee.tw/search?keyword="+product)# FIRST
hight = 0
while True:
    hight +=1000
    try:
        driver.execute_script("window.scrollTo({},{})".format(0,hight)) 
        sleep(0.5)
        if hight == 6000:
            break
    except:
        break
doc = driver.find_elements_by_css_selector(".col-xs-2-4")
GG=0
checkopen = 0
for i in doc:
    checkopen = 0
    try:
        webpo = i.find_element_by_css_selector(".col-xs-2-4>div>a").get_attribute("href") #取網頁
        posit = i.find_element_by_css_selector("._3amru2") #地點
        try:
            star = len(i.find_elements_by_css_selector(".shopee-rating-stars__star-wrapper")) #看多小星星
        except:
            star = 0
        if star != 0:
            subcp = 0
            cp = 0
            dataaa = webdriver.Chrome("chromedriver")
            dataaa.get(webpo)
            checkopen = 1
            pd = dataaa.find_element_by_css_selector(".flex-auto")
            hight = 0
            while True:
                hight +=1000
                try:
                    dataaa.execute_script("window.scrollTo({},{})".format(0,hight))
                    sleep(0.5)
                    if hight == 6000:
                        break
                except:
                    break
            pd = dataaa.find_element_by_css_selector(".flex-auto")
            try:
                name = dataaa.find_element_by_css_selector(".qaNIZv") 
            except:
                print("nameerror1")
            try:
                starnum = dataaa.find_element_by_css_selector("._3Oj5_n")
            except:
                starnum = 0
            try:
                money =dataaa.find_element_by_css_selector("._3n5NQx")
            except:
                print("moneyhead")
            try:
                sale = dataaa.find_element_by_css_selector("._22sp0A")
            except:    
                print("saleerror")
            ima = dataaa.find_element_by_css_selector("#main > div > div.shopee-page-wrapper > div.page-product > div.container > div:nth-child(3) > div.page-product__content > div.page-product__content--left > div:nth-child(2) > div > div.product-rating-overview > div.product-rating-overview__filters > div.product-rating-overview__filter.product-rating-overview__filter--active.product-rating-overview__filter--all")
            ima.click()
            star3 = dataaa.find_element_by_css_selector(".product-rating-overview__filters > div:nth-child(4)") #check 有沒有三星評價
            star = star3.text.split()
            star3 = star[2].replace("(","").replace(")","")
            star3 =int(star3)
            if star3 < 10:
                subcp += 1
            elif star3 >= 10:
                subcp += 2
            star2 = dataaa.find_element_by_css_selector(".product-rating-overview__filters > div:nth-child(5)")
            star = star2.text.split()
            star2 = star[2].replace("(","").replace(")","")
            star2 =int(star2)
            if star2 < 10:
                subcp += 2
            elif star2 >= 10:
                subcp += 3
            star1 = dataaa.find_element_by_css_selector(".product-rating-overview__filters > div:nth-child(6)")
            star = star1.text.split()
            star1 = star[2].replace("(","").replace(")","")
            star1 =int(star1)
            if star1 < 10:
                subcp += 2
            elif star1 >= 10:
                subcp += 3
            try:
                freight = dataaa.find_element_by_css_selector(".shopee-drawer > .flex") #取運費
                freight = freight.text.replace("$","")
               # print("freight =",freight,sep="")
                if " " in freight:
                    freight = freight.replace(" ","")
                  #  print("freight2 =",freight,sep="")
                if "-" in freight:
                    freight= freight.split("-")
                  #  print("freight3 =",freight,sep="")
                try:
                    if type(freight) != list:
                        freight = int(freight)
                        if 0 == freight:
                            cp += 1
                except:
                    print("freight1error")
                try:
                    if type(freight) == list:
                        for j in range(len(freight)):
                            freight[j] = int(freight[j])
                        if 0 in freight:
                            cp += 1
                except:
                    print("freight2error")
            except:
                try:
                    freight = dataaa.find_element_by_css_selector("._3djNyJ > .flex > .flex ")
                    if freight == "含運費":
                        freight = 0
                        cp += 1
                except:
                    print("freighterror")
                    print(webpo)
            if starnum != 0:
                try:
                    rd = {}
                    rd["title"] = name.text
                    starchange = starnum.text
         #           print("starchange = ",starchange)
         #           print(type(starchange))
                    rd["star"] = float(starchange)
                except:
                    print("cperror")
                try:  
                    cp = float(starchange)
          #          print("checkcp = ",cp)
                except:
                    print("cperror2")
                money = money.text.replace("$","").replace(",","")
                try:
                    if ' ' in money:
                        money = money.replace(" ","")
           #             print("money3 =",money,sep="")
                    if "-" in money:
                        money = money.split("-")
           #             print("money4 = ",money)
                        try:
                            for ii in range(len(money)):
                                money[ii] = int(money[ii])
                        except:
                            print("moneyerror")
                    else:
                        if ' ' in money:
                            money.replace(" ","")
                    if type(money) != list:
                        money = int(money)
                except:
                    print("moneyerror2")
          #      print("money5 =", type(money))
          #      print("money6 = ",money)
                try:
                    rd["money"] = money
                    rd["website"] = webpo
                    sold = sale.text
                    if "," in sold:
                        sold = sold.replace(",","")
                    if "." in sold:
                        sold = sold.replace(".","")
                    if "萬" in sold:
                        sold = sold.replace("萬","0000")
                    if "千" in sold:
                        sold = sold.replace("千","000")
                    if "仟" in sold:
                        sold = sold.replace("仟","000")
                    if "百" in sold:
                        sold = sold.replace("百","00")
                    if "佰" in sold:
                        sold = sold.replace("佰","00")
                    sold = int(sold)
                  #  print("money = ",money)
                  #  print("sold = ",sold)
                except:
                    print("error1")
                  #  print("money =",money)
                  #  print("webpo =",webpo)
                try:
                    if type(money) == list:
                        if sold >= max(money):
                            cp += 3
                            print("cp+3")
                        elif sold/max(money)*100 >= 50:
                            cp += 2
                            print("cp+2")
                        else:
                            cp += 1
                            print("cp+1")
                    else:
                        if sold >= money:
                            cp += 3
                            print("cp+3")
                        elif sold/money*100 >= 50:
                            cp += 2
                            print("cp+2")
                        else:
                            cp += 1
                            print("cp+1")
                    print("cp = ",cp)
                    print("subcp = ",subcp)
                    cp = cp-subcp
                except:
                    print("error2")
                    print(webpo)
                try:
                    rd["sold"] = sold
                    rd["position"] = posit.text
                    rd["CP"] = cp 
                    rd["freight"] = freight
                except:
                    print("error3")
                print("cp = ",cp)
                if cp >= 1:
             #       print("cp >= 8")
                    dataaa.save_screenshot(str(GG)+'.png')
                    imagename = str(GG)+'.png'
                    rd["image"] = imagename
                    GG += 1
                    redata.append(rd)
                    print("OK")
                    if rd["position"] not in position and rd["position"] != "":
                        position[rd["position"]] = 1
                    elif rd["position"] in position:
                        value = position[rd["position"]]
                        value += 1
                        position[rd["position"]] = value
                else:
            #        print("cp down")
                    pass
                #print(redata)
            dataaa.quit()
            if GG >= 10:
                break
            print("GG =",GG)
    except:
        if checkopen:
             dataaa.quit()
        pass
driver.quit()
totalcp = 0
totalmoney = 0
totalstar = 0
totalsold = 0
for i in range(len(redata)):
    money = redata[i].get("money")
    if type(redata[i].get("money")) == list:
        totalmoney += max(money)
    else:
        totalmoney += money
    totalcp += redata[i].get("CP")
    totalsold += redata[i].get("sold")
    totalstar += redata[i].get("star")
print("money = %.2f" % (totalmoney/len(redata)))
print("cp =",totalcp/len(redata))
print("sold = %.2f" %(totalsold/len(redata)))
print("stars = %.2f" % (totalstar/len(redata)))
print(position)
print(len(position))
print(redata)
data = pds.DataFrame(redata)
data['Average_price'] =  totalmoney/len(redata)
data['Average_cp'] =  totalcp/len(redata)
data['Average_star'] =  totalstar/len(redata)
data['Average_sold'] =  totalsold/len(redata)
print(data)
data.to_excel("hobedata.xlsx")
x = [i  for i in range(len(position))]
print(x)
y = [position[i] for i in position]
soldline = []
pos = [i for i in position]
print(y)
plt.subplot(1,2,1)
plt.plot(x, y,color='red', linewidth=5.0, linestyle='--')
plt.xlabel('Position')
plt.subplot(1,2,2)
yy = [yy['sold'] for yy in redata] #sold
mon =[]
for i in redata:
    if type(i["money"]) ==list:
        mon.append(max(i['money']))
    else:
        mon.append(i['money'])
print(mon)
xx = [i for i in range(len(data))]
plt.plot(xx,yy,color='red', linewidth=5.0, linestyle='--')  #sold
plt.plot(xx,mon,color='blue', linewidth=5.0, linestyle='-')  #money
plt.xlabel("Date")