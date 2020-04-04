import os
import csv
import datetime 
from time import sleep

def writefile(file = "cmd_control_path.txt"):
    print("Set your path:")
    path = input()
    with open(file, "w") as of:
        of.write(path)
    print("have set your path")
    os.chdir(path)

if not os.path.exists("cmd_control_path.txt"): #如果不存在 ,寫你的路徑
    writefile()
else:
    f = open("cmd_control_path.txt","r") #如果存在 開你的路徑
    c = f.readline()
    os.chdir(c)
    f.close()

if os.path.exists(os.getcwd()):
    while True:
        os.system("cls")
        print("Your path :",os.getcwd())
        print("Choose yuor services")
        print("1.Add file\t2.Check your path\t3.Change your path\t4.EXIT")
        print("(11).file\t(22).txt\t(33).Word\t(44).PPT\t(55).ECXL [Fast key]")
        cho = input()
        check = 1
        chfast = 0
        chfastxlsx = 0
        ent = 0
        if cho == '1':
            print("(1).file\t(2)txt.(txt)\t(3).Word(docx)\t(4).PPT(pptx)\t(5).ECXL(xlsx)")
            cho2 = input()
            if cho2 == '1': # 增目錄
                print("Are you changing file name?   (1).YES (2)NO")
                cho3 =input()
                if cho3 == "1" or cho3 =="yes" or cho3 =='YES' or cho3 =="Yes":
                    name = input()
                    if not os.path.exists(name):
                        os.mkdir(name)
                    else:
                        print(name+"have set")
                elif cho3 == "2" or cho3 =="no" or cho3 =='NO' or cho3 =="No":
                    try:
                      name = str(datetime.datetime.now())
                      name = str(name).split(".")
                      name = name[0].split(":")
                      name = name[0]+name[1]
                      os.mkdir(name)
                    except:
                        print("These are this name")
            elif cho2 == '2':
                check = 0
                last = '.txt'
            elif cho2 == '3':
                check = 0
                last = '.docx'
            elif cho2 == '4':
                check = 0
                last = '.pptx'
            elif cho2 == '5':
                check = 1
                last = '.csv'
                print("Are you changing file name?   (1).YES (2)NO")
                cho3 = input()
                if cho3 == "1" or cho3 == "yes" or cho3 == 'YES' or cho3 == "Yes":
                    name = input()
                else:
                    name = datetime.datetime.now()
                    name = str(name).split(".")
                    name = name[0].split(":")
                    name = name[0]+name[1]
                name = str(name)+last
                if not os.path.exists(name):
                    ent = 1
                else:
                    print(name + "have set")
                    print("Are you sure ?   (1).YES (2)NO")
                    cho4 = input()
                    if cho4 == "1" or cho4 == "yes" or cho4 == 'YES' or cho4 == "Yes":
                        ent = 0
                    else:
                        ent = 1
                if ent:
                   with open(name, 'w', newline='') as csvfile:
                    fieldnames = []
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                    writer.writeheader()
                    writer.writerow({})
                    writer.writerow({})
                    writer.writerow({})
                    print("finish")
                    
        elif cho == '11':#  快鍵
            try:
                name = str(datetime.datetime.now())
                name = str(name).split(".")
                name = name[0].split(":")
                name = name[0]+name[1]
                os.mkdir(name)
            except:
                print("These is this name")
        elif cho == '22':
            last = '.txt'
            chfast = 1
        elif cho == '33':
            last = '.docx'
            chfast = 1
        elif cho == '44':
            last = '.pptx'
            chfast = 1
        elif cho == '55':
            last = '.csv'
            chfastxlsx = 1
        elif cho == '2':
            print("Your path is :", os.getcwd())
            sleep(1)
        elif cho == '3':
            print("Change your path :")
            writefile()
        elif cho == '4':
            break
        
        if chfast:
            name = datetime.datetime.now()
            name = str(name).split(".")
            name = name[0].split(":")
            name = name[0]+name[1]+last
            fd = os.open( name+last, os.O_RDWR|os.O_CREAT )
            os.close(fd)
        
        if chfastxlsx:
            name = datetime.datetime.now()
            name = str(name).split(".")
            name = name[0].split(":")
            name = name[0]+name[1]+last
            with open(name, 'w', newline='') as csvfile:
                fieldnames = []
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
                writer.writeheader()
                writer.writerow({})
                writer.writerow({})
                writer.writerow({})
            print("finish")
        
        if not check: #add  word ,ppt,文本
                print("Are you changing project name   (1).YES (2)NO")
                cho3 = input()
                if cho3 == "1" or cho3 == "yes" or cho3 == 'YES' or cho3 == "Yes":
                    name = input()
                else:
                    name = datetime.datetime.now()
                    name = str(name).split(".")
                    name = name[0].split(":")
                    name = name[0]+name[1]
                name = name+last
                if not os.path.exists(name):
                    ent = 1
                else:
                    print(name + "have set")
                    print("Are your sure ?   (1).YES (2)NO")
                    cho4 = input()
                    if cho4 == "1" or cho4 == "yes" or cho4 == 'YES' or cho4 == "Yes":
                        ent = 0
                    else:
                        ent = 1
                if ent:
                    print(name)
                    fd = os.open(name, os.O_RDWR|os.O_CREAT )
                    os.close(fd)
                    print("finish")
else:
    print("PATH ERROR")