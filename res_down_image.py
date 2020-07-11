import requests
from pyquery import PyQuery as pq
from selenium.webdriver.common.action_chains import ActionChains
from os_file import newfile,changepath
name = "picture"
newfile(name)
changepath(name)


def downimg(name, url,header,cookie):
    img = requests.get(url, headers=header, cookies= cookie)
    with open(name, "wb") as f:
        f.write(img.content)

def one_web():
    for i in range(1,5):
        print("this is ",i,"time")
        url="http://www.tooopen.com/img/87_0_1_"+str(i)+".aspx"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                  "Referer":"https://www.tooopen.com/view/2187454.html"}
        cookie = {"ASP.NET_SessionId":"819f1a1b-7ba7-49f5-b010-0436a2a7ec6f","Hm_lvt_d3ac2f8840ead98242d6":"1593785370","Hm_lpvt_d3ac2f8840ead98242d6205eeff29cb4":"1593785370"}
        rep = requests.get(url,headers = header,cookies = cookie)
        print(rep.status_code)
        rep.encoding="utf-8"
        if rep.status_code == 200:
            doc = pq(rep.text)
            for i in doc("div > a.pic").items():
                imageweb = i.attr("href")
                imagpng = i("img").attr("src")
                name = i("p").html()
                print("name = ",str(name))
                print("small image = ",imagpng)
                print("path = ",imageweb)
                smallname = str(imagpng)
                smallname = smallname.split("/")[-1]
                smallname = smallname.split(".")
                print("small name = ",smallname[0])
                downimg(smallname[0]+".jpg",imagpng,header,cookie)
                downimg(smallname[0]+".png", imagpng,header,cookie)
                imgweb = requests.get(imageweb,headers = header,cookies = cookie)
                doc2 = pq(imgweb.text)
                image = doc2("th.pic-box > img").attr("src")
                downimg(name+".jpg",image,header,cookie)
                downimg(name + ".png", image,header,cookie)
            else:
                print("web error")
    print("finish one web")

def two_web():
    for i in range(1,10+1):
       url = "https://www.crazybackground.com/tag/%e8%83%8c%e6%99%af%e5%9c%96%e5%ba%ab/page/"+str(i)
       header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
       cookies = {"__cfduid":"d1ca7eea9283b1d5d59fbadf8d441be"}
       rep = requests.get(url,headers = header)
       rep.encoding="UTF-8"
       if rep.status_code == 200:
           doc = pq(rep.text)
           for i in doc("div.excerpts > article.excerpt").items():
               img = i("a>img").attr("data-src")
               name = str(img).split("/")[-1]
               print(img,"name = ",name)
               downimg(name, img,header,cookies)
       else:
           print("web error")
    print("finish two web")

if __name__ == '__main__':
    one_web()
    two_web()
