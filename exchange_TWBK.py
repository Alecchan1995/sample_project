import requests
from pyquery import PyQuery as pq
import copy
def twbk():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    req = requests.get(url)
    num = 0
    if req.status_code == 200:
        doc = pq(req.text)
        data = {}
        for i in doc("tbody>tr").items():
            data["country"] = i("div.visible-phone.print_hide").text()
            try:
                data["buy"] = float(i("tr>td:nth-child(2)").text())
            except:
                data["buy"] = str(i("tr>td:nth-child(2)").text())
            try:
                data["sale"] = float(i("tr>td:nth-child(3)").text())
            except:
                data["sale"] = str(i("tr>td:nth-child(3)").text())
            num += 1
            alldata[num]  = copy.deepcopy(data)
    # ie11andabove > div > table > tbody > tr:nth-child(1) > td:nth-child(2)
    # ie11andabove > div > table > tbody > tr:nth-child(1) > td:nth-child(3)

def ecme(comdata,yourmem):
    if comdata != "-":
        return comdata*yourmem
    else:
        print("these is not date")

def com_act():
    #while True:
    for i,j in alldata.items():
        print(i,j["country"])
    cho = int(input("input your cuntry number"))
    print(alldata[cho])
    inpmo = int(input("how much excange your memory(TW) :"))
    buy = ecme(alldata[cho]["sale"],inpmo)
    sale = ecme(alldata[cho]["buy"], inpmo)
    print("Your memory  = ",str(inpmo)+"TW","sale = ",sale,"but = ",buy)

if __name__ == '__main__':
    alldata = {}
    twbk()
    com_act()