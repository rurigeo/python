import re
import os  
import math  
import pylab  
freq = []
s11 = []
s2p = open('22.S2P','r')
s2p.seek(195) #read from 5th line
for line in s2p:
    #print line
    temp = re.split('\t',line.rstrip())
    freq.append(float(temp[0]))
    a = float(temp[3])
    b = float(temp[4])
    c = complex(a,b)
    s11.append(20*math.log10(abs(c)))
s2p.close()
raw_input("END")
print freq
print s11
pylab.plot(freq,s11,'c')  
pylab.show() 
