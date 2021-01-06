import cv2 as cv
import matplotlib.pyplot as plt
from wfunction import *
import numpy as np
import cv2 as cv
import os

class WV():
	def __init__(self,filenamec,filenamedc): #filenamec 加密  filenamedc 解密
		self.filenamec=filenamec
		self.filenamedc=filenamedc
		
	def wmvc(self): #加密動作
		filename = self.filenamec
		imageyy = opendocx(filename)
		print(type(imageyy))
		yn = len(imageyy)
		imagex = cv.imread(self.filenamedc,cv.IMREAD_GRAYSCALE)   #y的圖\n",
		regx = imagex.shape
		imagexx = imagex.flatten()
		xn=len(imagexx)
		hid = 10
		n = 0.55#round(random.uniform(0,1),3) #閥值 #learn rate
		b = 0.001 #閥值
		z = setznum(hid) #初始化Z\n" z of len
		wx = np.random.uniform(-1,1,(hid,xn)) #x->z of w
		uy = np.random.uniform(-1,1,(hid,yn)) # y->z of w
		vx = np.random.uniform(-1,1,(xn,hid)) #z->outx of w
		ty = np.random.uniform(-1,1,(yn,hid)) #z->outy of w
		print("wx.shape :",wx.shape)
		print("vx.shape :",vx.shape)
		print("uy.shape :",uy.shape)
		print("ty.shape :",ty.shape)
		print("z.shape :",z.shape)
		reimx = setoutx(xn)
		reimy = setouty(yn)
		print("b = ",b,"n = ",n)
		from datetime import datetime as dt
		num = 0
		for i in range(len(imagexx)):
			reimx[i] = ((imagexx[i]/255)*2) - 1   #正規化
		for j in range(len(imageyy)):
			reimy[j] = ((imageyy[j]/255)*2) - 1
		print(dt.now())
		start = dt.now()
		z = setznum(hid)
		zres = setznum(hid)
		reoutx =[]
		reouty =[]
		renum = []
		while True:
			risx = []
			risy = []
			outx = setoutx(xn)
			outy = setouty(yn)
			setz(reimx, reimy, wx, uy, z)
			setout(z, vx, ty, outx, outy)
			checkoutx = 0
			for i in range(len(outx)):  # check outx of error
				# check = 0
				check = outx[i] - imagexx[i]
				if check < 0:
					check = check * -1
				# if i < 11:
				#    print("x",i,"=",check,"outx - imagexx",outx[i]," - ",imagexx[i])
				risx.append(check)
				if check > b or check < 0:
					checkoutx = 1
			imx = np.array(check)  # outxage
			for j in range(len(outy)):
				check = outy[j] - imageyy[j]
				if check < 0:
					check = check * -1
				#  print("yerror = ",check )
				risy.append(check)
				if check > b or check < 0:
					checkoutx = 1
			imy = np.array(check)  # outy
			if checkoutx == 0:
				print("FINISH")
				finish = dt.now()
				break
			else:
				# print("imagex00 = ",imagexx[0])
				# print("outx = ",np.mean(imx),"outy = ",np.mean(imy),"ty00 = ",ty[0][0])
				reoutx.append(np.mean(imx))
				renum.append(num)
				reouty.append(np.mean(imy))
				# print("z = ",z[0])
				# print("outx =",outx[0])
				# print("outy =",outy[0])
				num += 1
				updateall(imagexx,wx,n,reimx,imageyy,reimy,uy,z,outx,vx,outy,ty)
		used = finish - start
		print('START :',start)
		print('FINISH :',finish)
		print('USED :',used)
		print("zmin = ", z.argmin())
		print(reimx[0],imagexx[0],z[0])
		rounddate(outx)
		rounddate(outy)
		outtext = outy.astype('int32')
		outfiledoc(outtext)
		regoutx = np.array(outx).reshape(regx[0],regx[1])
		cv.imwrite('outx.jpg', regoutx)
		strn = str(n)
		with open(self.filenamec+'w.txt' , 'w') as f: #權重
			f.write(strn+"\n")
			f.write(str(b)+'\n')
			f.write(str(hid)+'\n')
			f.write(str(len(wx))+'\n')
			f.write(str(len(wx[0])) + '\n')
			for i in range(len(wx)):
				for j in range(len(wx[i])):
					f.write(str(wx[i][j])+"\n")
			f.write(str(len(uy))+'\n')
			f.write(str(len(uy[0])) + '\n')
			for i in range(len(uy)):
				for j in range(len(uy[i])):
					f.write(str(uy[i][j])+"\n")
			f.write(str(len(vx)) + '\n')
			f.write(str(len(vx[0])) + '\n')
			for i in range(len(vx)):
				for j in range(len(vx[i])):
					f.write(str(vx[i][j]) + "\n")
			f.write(str(len(ty)) + '\n')
			f.write(str(len(ty[0])) + '\n')
			for i in range(len(ty)):
				for j in range(len(ty[i])):
					f.write(str(ty[i][j]) + "\n")
					
	def decset(self):    # 解碼
		name = self.filenamedc# filenamedc ==KEY
		n = 0.0
		with open(self.filenamec+'w.txt','r') as f:
		   n = float(f.readline().replace("\n",""))
		   b = float(f.readline().replace("\n",""))
		   hid = int(f.readline().replace("\n",""))
		   wxlen = int(f.readline().replace("\n",""))
		   wxlenlen =  int(f.readline().replace("\n",""))
		   wx = np.zeros((wxlen,wxlenlen))
		   for i in range(wxlen):
			   for j in range(wxlenlen):
				   wx[i][j] = float(f.readline().replace("\n",""))
		   uylen = int(f.readline().replace("\n", ""))
		   uylenlen = int(f.readline().replace("\n", ""))
		   uy = np.zeros((uylen, uylenlen))
		   for i in range(uylen):
			   for j in range(uylenlen):
				   uy[i][j] = float(f.readline().replace("\n", ""))
		   vxlen = int(f.readline().replace("\n", ""))
		   vxlenlen = int(f.readline().replace("\n", ""))
		   vx = np.zeros((vxlen, vxlenlen))
		   for i in range(vxlen):
			   for j in range(vxlenlen):
				   vx[i][j] = float(f.readline().replace("\n", ""))
		   tylen = int(f.readline().replace("\n", ""))
		   tylenlen = int(f.readline().replace("\n", ""))
		   ty = np.zeros((tylen, tylenlen))
		   for i in range(tylen):
			   for j in range(tylenlen):
				   ty[i][j] = float(f.readline().replace("\n", ""))
		self.decrypt(hid,wx,ty,name)
		
	def decrypt(self,hid,wx,ty,name): #   name = filename
		outxx = cv.imread(name,cv.IMREAD_GRAYSCALE)
		outxxx = outxx.flatten()
		rex = setoutx(len(outxxx))
		z = setznum(hid)
		rex = ((outxxx/255)*2) - 1
		outyy = setouty(len(ty))
		outwaterz(rex,wx,z)
		outwatery(z,ty,outyy)
		rounddate(outyy)  # doc
		print(outyy)
		outtext2 = outyy.astype('int32')
		outfiledoc(outtext2)

filenamec = 'aaa.jpg'
filenamedc = 'a30.jpg'
filena = WV(filenamec,filenamedc) #filenamec 加密  filenamedc 解密
filena.wmvc() 
filena. decset() 