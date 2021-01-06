import numpy as np
import os
def setz(reimx=[],reimy=[],wx=[],uy=[],z=[]): #算Z的值\n",
    global remin
    zres = (reimx - wx)**2
    for i in range(len(z)):#hid is hidden verous
        z[i] += zres[i].sum() #imagexx[i] - wx[j][i]
        #if i == 0:
         #       print('z[0]',z[0],'=','zres',zres[0][0],'wx[0][0]',wx[0][0])

    yres = (reimy - uy)**2
    for yy in range(len(z)):
        z[yy] += yres[yy].sum()
        #if yy == 0:
        #        print('z[0]',z[0],'=','yres',yres[0][0],'uy[0][0]',uy[0][0])
    #print(z[0])
    
    remin = z.argmin()
    for i in range(len(z)):
        z[i] = 1 if i == remin else 0
        
   # print("z = ",z)
   # rounddate(z)
def setout(z=[],vx=[],ty=[],outx=[],outy=[]):
    resoutx = z*vx
    for i in range(len(outx)): #輸出的量  targer verous\n",
        outx[i] +=  resoutx[i].sum()  # x的輸出 XV的權重*Z的值  \n",
        #    print("outx[",i,"] = ",outx[i],"z[",j,"]=",z[j],'*',"vx[",j,"][",i,"] = ",vx[j][i])
    
    
    resouty = z*ty
    for i in range(len(outy)):   #輸出的量    output y imagey\n",
        outy[i] +=  resouty[i].sum()  # x的輸出 XV的權重*Z的值\n",
           # print("outy[",i,"] = ",outy[i],"z[",j,"]=",z[j],'*',"ty[",j,"][",i,"] = ",ty[j][i])
            


def setznum(hid):  #初始化Z\n",
    return np.zeros(hid)

def setoutx(xn): #初始化Ximage output\n",
    return np.zeros(xn)

def setouty(yn): #初始化Ximage output\n",
    return np.zeros(yn)

def recodeE(imagexx,outx):
    recodex = imagexx - outx
    #print(type(recodex))
    return recodex

def updatevx(n,z,outx,vx,imagexx):
    global remin
    for jj in range(len(outx)):
        #for ii in range(len(z)):
         #   print("vx[",ii,"][",jj,"] + n*(reimxx[",jj,"]-outx[",jj,"])*z[",ii,"] = ",vx[ii][jj],"+",n,"*",(reimx[jj]-outx[jj]),"*",z[ii])
        vx[jj][remin] = vx[jj][remin] + n*(imagexx[jj]-outx[jj])*z[remin]
         #   print("vx[",ii,"][",jj,"] = ",vx[ii][jj])
          #          print("new vx = ",vx[ii][jj])
                #print("vx[",ii,"][",jj,"] = ",vx[ii][jj] ,"(1-n) = ",1-n,"*uy[i][j] + n*imageyy[i] = ",n*z[ii])
                
def updatety(n,imageyy,z,outy,ty):
    for jj in range(len(outy)):
        #for ii in range(len(z)):
      #      print("ty[",ii,"][",jj,"] + n*(reimy[",jj,"]-outy[",jj,"])*z[",ii,"] = ",ty[ii][jj],"+",n,"*",(reimy[jj]-outy[jj]),"*",z[ii] )
       ty[jj][remin] = ty[jj][remin] + n*(imageyy[jj]-outy[jj])*z[remin]
       #     print("ty[",ii,"][",jj,"] = ",ty[ii][jj])
       #         print("ty[",ii,"][",jj,"] = ",ty[ii][jj],"+","n = ",n,"imy=",imageyy[jj]," - ty =",imageyy[jj] - ty[ii][jj],"*sqrt(z)[",jj,"] =",math.sqrt(z[jj]))
def updatewx(imagexx,wx,n,reimx):
    #for j in range(len(z)): #wx,uy
    for i in range(len(imagexx)):
       #     print("wx[",i,"][",j,"] = (1-n)*wx[",i,"][",j,"]+n*reimx[",i,"] = ",(1-n),"*",wx[i][j],"+",n,"*",reimx[i])
        wx[remin][i] = (1-n)*wx[remin][i]+n*reimx[i] #n=(0.785*183)=143.655+40.205=(0.215*187)
          #  print("wx[",i,"][",j,"] = ",wx[i][j])

def updateuy(imageyy,n,reimy,uy):
    #for j in range(len(z   )):
    for i in range(len(imageyy)):
          #  print("uy[",i,"][",j,"] = (1-n)*uy[",i,"][",j,"]+n*reimy[",i,"] = ",(1-n),"*",uy[i][j],"+",n,"*",reimy[i])
        uy[remin][i] = (1-n)*uy[remin][i] + n*reimy[i]
          #  print("uy[",i,"][",j,"] = ",uy[i][j])

def updateall(imagexx,wx,n,reimx,imageyy,reimy,uy,z,outx,vx,outy,ty):
    updatewx(imagexx,wx,n,reimx)
    updateuy(imageyy,n,reimy,uy)
    updatevx(n,z,outx,vx,imagexx)
    updatety(n,imageyy,z,outy,ty)
 #   print("new wx00 = ",wx[0][0],"new y = ",uy[0][0],"new vx = ",vx[0][0],"new ty = ",ty[0][0])
 #   print("mean w=",np.mean(wx),"mean u=",np.mean(uy),"mean v=",np.mean(vx),"mean t=",np.mean(ty))
def updatehid():
    updatewx()
    updateuy()
def updateout():
    updatevx()
    updatety()
    
def rounddate(date = []):
    for i in range(len(date)):
        date[i] = round(date[i],0)
    
def outfiledoc(c):
 #   print(filename)
    newfile = []    #save name
    lenfilename = c[-1] # len of filename
    for i in c[-c[-1]-1:-1]:
        newfile.append(chr(i))  # change int to str of filename 
  #  print(newfile)
    newfilename = ''.join(newfile) # save int to str of filename 
    print(newfilename)
    c = np.delete(c,np.s_[-c[-1]-1::]) # del file data
   # print(c)
    filelen = c[-1] # get file size
   # print(filelen)
    c = np.delete(c,-1)
   # print(len(c))
    outfile = bytearray()
    for j in c[-filelen::]:
        outfile.append(j)
    #print(outfile)
    name = 'add'+"".join(newfile)
    with open(name,'wb') as f:
        f.write(outfile)


def outwaterz(rex,wx,z):
    zres3 = (rex - wx) ** 2
    for i in range(len(z)):  # hid is hidden verous
        z[i] += zres3[i].sum()  # imagexx[i] - wx[j][i]

    remin = z.argmin()
    for i in range(len(z)):
        z[i] = 1 if i == remin else 0


def outwatery(z,ty,outyy):
    reoutyy = z * ty
    for i in range(len(reoutyy)):  # 輸出的量    output y imagey\n",
        #  for j in range(len(z)): #Z的量\n",
        #print(i)
        outyy[i] = reoutyy[i].sum()  # x的輸出 XV的權重*Z的值\n",
        # print("outy[",i,"] = ",outy[i],"z[",j,"]=",z[j],'*',"ty[",j,"][",i,"] = ",ty[j][i])

def opendocx(filename):
    res = []
    with open(filename,'rb') as f:
        res.append(f.read())
    res =  bytearray(res[0])
    filelen = len(res)
    for i in filename:
        res.append(ord(i))
    #print(res)
    change = []
    for i in res:
        change.append(i) 
    change.insert(-len(filename),filelen)  
    change.append(len(filename))
    #print(change)
    return change 
