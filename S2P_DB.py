import re
import os  
import math  
import pylab  
freq = []
s11 = []
s21 = []
s12 = []
s22 = []
s2p = open('11.S2P','r')
s2p.seek(195) #read from 5th line
for line in s2p:
    #print line
    temp = re.split('\t',line.rstrip())
    freq.append(float(temp[0]))
    s11.append(float(temp[1]))
    s21.append(float(temp[3]))
    s12.append(float(temp[5]))
    s22.append(float(temp[7]))
s2p.close()
raw_input("END")
#print freq
#print s11
pylab.plot(freq,s11,'y')
pylab.plot(freq,s21,'c') 
pylab.plot(freq,s12,'m') 
pylab.plot(freq,s22,'g') 
pylab.show() 
