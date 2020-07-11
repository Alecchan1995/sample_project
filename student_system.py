import os
class student():
        num,name,sex,phone,birth,alldata=[],[],[],[],[],[]
        def openfile(self):
            print("Open file")

        def safefile(self):
            print("Safe file")
            self.filename =input("Filename : ")
            if not os.path.exists("C:\\student_file\\"+self.filename):
                with open(self.filename,'w') as of:
                    of.write("\n".join(self.alldata))
        
        def checkdir(self):#開目錄            
            self.dir = "C:student_file"
            if not os.path.exists(self.dir):
                os.mkdir(self.dir)
            else:
                print(self.dir + "已經建立!")
                    
        def settable(self,num,name,sex,phone,birth):
            self.num.append(num)
            self.name.append(name)
            self.sex.append(sex)
            self.phone.append(phone)
            self.birth.append(birth)
            self.alldata.append([name,num,sex,birth,phone])

        def add(self):
            name = input("Name : ")
            sex = input("Sex : ")
            num = input("Your classnumber :")
            phone = input("phone :")
            birth = input("birthday : ")
            self.aa = self.addsafe(num)
            if self.aa == 0:
                self.data = self.settable(num,name,sex,phone,birth)
            else:
               print("ERROR")
        
        def addsafe(self,num):
            self.ckn = num
            if self.ckn == '' or self.ckn == ' ':
                print('Classnumber is empty')
                return 1
            for q in range(len(self.alldata)):
                if self.ckn == self.alldata[q][0] :
                    print('These have been your number')
                    return 1
            return 0
        
        def listmunes(self):
            print("1. 增加資料 :")
            print("2. 查詢資料 :")
            print("3. 列出資料 :")
            print("4. 刪除資料 :")
            print("5. 修改資料 :")
            print("6. 離開 :")

        def showall(self):
           # print(len(self.alldata))
            self.menu=['Name :','Classnumber :','Sex :','Birthday :','Phonenumber :']
            for i in range(len(self.alldata)): #name,num,sex,birth,phone
                for menu in self.menu:
                    print(menu.center(15),end="")
                print("")
                for j in range(len(self.menu)):
                    print(self.alldata[i][j].center(15),end="")
                    if(j == len(self.menu)-1):
                        print("")
        
        def show(self,i):
                print("Aame :\tClassnumber :\tSex :\tBirthday :\tPhonenumber :")
                print("%6s\t%10s\t%2s\t%10s\t%10s"%(self.alldata[i][0],self.alldata[i][1],self.alldata[i][2],self.alldata[i][3],self.alldata[i][4]),sep="")    
        
        def check(self): 
            while True:
                print("Choose your style\n(1) Name\t(2) Name and Classnumber\t(3)Exit")
                self.cho = input()
                if self.cho == '1':
                    self.cname = input('Check your Name: ')
                    self.checkdata(self.cname)
                elif self.cho == '2':
                    self.cname = input('Check your Name: ')
                    self.cnum = input('Check your Classnumber: ')
                    self.checkdata(self.cname,self.cnum)
                elif self.cho == '3':
                    break
                else:
                    print("輸入正確號碼")
                            
        def delete(self):
            print("輸入你的Delete的Name和Classnumber")
            self.act = True
            self.cname = input()
            self.cnum = input()
            print(self.alldata)
            for i in range(len(self.alldata)):
                    print(i)
                    if self.cname in self.alldata[i]:
                        self.act=False
                        self.show(i)
                        self.alldata.remove(self.alldata[i])
                        break
                    else:
                        print("These is not your data")
            
        def checkdata(self,cname2 = 'none',cnum2 = 'none' ):
            self.cname2 = cname2
            self.cnum2 = cnum2
            self.ctf=True
            i=0
            print(self.cname2,self.cnum2)
            if self.cname2 == 'none' and self.cnum2 == 'none':
                self.ctf=True
            elif self.cname2 != 'none' and self.cnum2 != 'none':
                for i in range(len(self.alldata)):
                    if self.cname2 in self.alldata[i] and self.cnum2 in self.alldata[i]:
                        self.ctf=False
                        self.show(i)
            else:
                for i in range(len(self.alldata)):
                    if self.cname2 in self.alldata[i]:
                        self.ctf=False
                        self.show(i)
                        return i
            if self.ctf:
                    print("These is not your data")
                    return -1
                    
        def change(self):
            while True:  #name,num,sex,birth,phone
                print('Want do you change')
                print("1. Name :")
                print("2. Classnumber :")
                print("3. Sex :")
                print("4. Birthday :")
                print("5. Phonenumber :")
                print("6. Exit :")
                self.cho=input()
                if self.cho == '1':
                     self.chn =  input("Check Name :")
                     self.po=self.changeact(self.chn,0)
                     if self.po != -1:
                         print("成功")
                elif self.cho == '2':
                     self.chc = input("Check Classnumber : ")
                     self.po=self.changeact(self.chc,1)
                     if self.po != -1:
                         print("成功")
                elif self.cho == '3':
                     self.chs = input("Check Sex :")
                     self.po=self.changeact(self.chs,2)
                     if self.po != -1:
                         print("成功")
                elif self.cho == '4':
                    self.chb = input("Check Birthday :")
                    self.po=self.changeact(self.chb,3)
                    if self.po != -1:
                         print("成功")
                elif self.cho == '5':
                    self.chp = input("Check Phonenumber :")
                    self.po=self.changeact(self.chp,4)
                    if self.po != -1:
                        print("成功")
                elif self.cho == '6':
                    break 
                
        def changeact(self,data,po):
            self.check=True
            for i in range(len(self.alldata)): 
                if data == self.alldata[i][po]:
                    self.chdata = input("Change :")
                    if po == 1 or po == 4:
                        for j in range(len(self.alldata)): 
                             if self.chdata == self.alldata[j][po]:
                                 print("These is your Classnumber")
                                 return -1
                        self.alldata[i][po] = self.chdata 
                        return i
                    else:          
                        self.alldata[i][po] = self.chdata
                        return i
            if self.check:
                print("These is not your data")
                return -1
                
        def process(self):
            self.checkdir()
            while True:
                self.listmunes()
                cho = input()
                if cho == '1': #add
                    self.add()
                elif cho == '2': #check
                    if len(self.alldata) == 0 :
                        print("These is not data")
                    else:
                        self.check()
                elif cho == '3': #list
                    if len(self.alldata) == 0 :
                        print("These is not data")
                    else:
                        self.showall()
                elif cho == '4': #delete
                    if len(self.alldata) == 0 :
                        print("These is not data")
                    else:
                        self.delete()
                elif cho == '5': #change
                    if len(self.alldata) == 0 :
                        print("These is not data")
                    else:
                        self.change()
                elif cho == '6': #exit()
                    break
                else:
                    print("輸入正確號碼") 


def main():
    a = student()
    a.process()
    
if __name__ == '__main__':
    main()