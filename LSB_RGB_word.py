# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:45:27 2020

@author: wasdu
"""

import cv2
import numpy as np

class LSB():
    def __init__(self,s,h,k):
        self.h = cv2.imread(h)
        self.s = s
        self.s_size = len(s)
        self.h_size = self.h.shape
        self.k = k
        self.h_copy = []
        self.s_copy = []
        self.d = [0]*(self.h_size[0]*self.h_size[1])
        (B,G,R) = cv2.split(self.h)
        self.g = G
        self.r = R
        self.b = B
        self.error = 0
        self.o = ''
        print(self.g)
        
    def decoder(self):
        for m in range(self.s_size):
            x = bin(ord(self.s[m]))
            if len(x) == 9:
                x = x.replace('0b','000000000')
            elif len(x) == 10:
                x = x.replace('0b','00000000')
            elif len(x) == 8:
                x = x.replace('0b','0000000000')
            elif len(x) == 7:
                x = x.replace('0b','00000000000')
            elif len(x) == 6:
                x = x.replace('0b','000000000000')
            elif len(x) == 5:
                x = x.replace('0b','0000000000000')
            elif len(x) == 4:
                x = x.replace('0b','00000000000000')
            elif len(x) == 3:
                x = x.replace('0b','000000000000000')
            elif len(x) == 2:
                x = x.replace('0b','0000000000000000')
            elif len(x) == 11:
                x = x.replace('0b','0000000')
            elif len(x) == 12:
                x = x.replace('0b','000000')
            elif len(x) == 13:
                x = x.replace('0b','00000')
            elif len(x) == 14:
                x = x.replace('0b','0000')
            elif len(x) == 15:
                x = x.replace('0b','000')
            elif len(x) == 16:
                x = x.replace('0b','00')
            elif len(x) == 17:
                x = x.replace('0b','0')
            elif len(x) == 18:
                x = x.replace('0b','')
                
            self.s_copy.append(int(x[0:2],2))
            self.s_copy.append(int(x[2:4],2))
            self.s_copy.append(int(x[4:6],2))
            self.s_copy.append(int(x[6:8],2))
            self.s_copy.append(int(x[8:10],2))
            self.s_copy.append(int(x[10:12],2))
            self.s_copy.append(int(x[12:14],2))
            self.s_copy.append(int(x[14:16],2))
            
        for k in range(self.h_size[0]):
            for l in range(self.h_size[1]):
                x = bin(self.g[k,l])
                if len(x) == 9:
                    x = x.replace('0b','0')
                elif len(x) == 10:
                    x = x.replace('0b','')
                elif len(x) == 8:
                    x = x.replace('0b','00')
                elif len(x) == 7:
                    x = x.replace('0b','000')
                elif len(x) == 6:
                    x = x.replace('0b','0000')
                elif len(x) == 5:
                    x = x.replace('0b','00000')
                elif len(x) == 4:
                    x = x.replace('0b','000000')
                elif len(x) == 3:
                    x = x.replace('0b','0000000')
                elif len(x) == 2:
                    x = x.replace('0b','00000000')
                
                x = x[0:6] + '00'
                self.h_copy.append(int(x,2))
                
        if len(self.h_copy) >= len(self.s_copy):
            x = len(self.h_copy) - len(self.s_copy)
            for i in range(x):
                self.s_copy.append(0)
        else:
            print('error')
                
    def encoder(self):
        for i in range(len(self.s_copy)):
            self.d[i] = self.s_copy[i] + self.h_copy[i]
            
        self.d = np.array(self.d)
        self.d = self.d.reshape((self.h_size[0],self.h_size[1]))
        
        merged = np.ones(self.h_size, dtype=np.uint8)
        merged[:, :, 0] = self.b
        merged[:, :, 1] = self.d
        merged[:, :, 2] = self.r
        
        cv2.imwrite('lsb_linebot_get.png',merged)
        
    def get_o(self):
        orginImage = cv2.imread('buwXKVQ.png')
        o_shape = orginImage.shape
        (B,G,R) = cv2.split(orginImage)
        
        print('G',G)
        
        print(G == self.g)
        
        o_copy = np.array(G)
        o_copy = o_copy.reshape(o_shape[0]*o_shape[1])
        
        o = ''
        
        for i in range(int(o_shape[0]*o_shape[1]/8)):
            x = ''
            for j in range(8):
                x += (bin(o_copy[8*i+j]))[-2:]
                
            if x == '0000000000000000':
                break
            
            o += chr(int(x,2))

        print(o)
        
    def run(self):
        self.decoder()
        self.encoder()


b = 'aaa巨錘瑞斯'
a = LSB(b,'lsb_linebot_get.png',2)
#a.run()
a.get_o()