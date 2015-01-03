import re
import os  
import math  
import pylab  
freq = []
s11 = []
s21 = []
s12 = []
s22 = []

def db_proc(snp):
    snp.seek(195) #read from 5th line
    for line in snp:
        #print line
        temp = re.split('\t',line.rstrip())
        freq.append(float(temp[0]))
        s11.append(float(temp[1]))
        s21.append(float(temp[3]))
        s12.append(float(temp[5]))
        s22.append(float(temp[7]))
   
def ri_proc(snp):
    snp.seek(195) #read from 5th line
    for line in snp:
        #print line
        temp = re.split('\t',line.rstrip())
        freq.append(float(temp[0]))
        #a = float(temp[1])
        #b = float(temp[2])
        #c = complex(a,b)
        #s11.append(20*math.log10(abs(c)))
        s21.append(20*math.log10(abs(complex(float(temp[1]),(temp[2])))))
        s21.append(20*math.log10(abs(complex(float(temp[3]),(temp[4])))))
        s12.append(20*math.log10(abs(complex(float(temp[5]),(temp[6])))))
        s22.append(20*math.log10(abs(complex(float(temp[7]),(temp[8])))))

s2p = open('11.S2P','r')
s2p.seek(186) #whether DB or RI
if s2p.readline(2) == 'dB':
    print 'db'
    db_proc(s2p)
elif s2p.readline(2) == 'RI':
    print 'ri'
    ri_proc()
s2p.close()
raw_input("END")
#print freq
#print s11
pylab.plot(freq,s11,'y')
pylab.plot(freq,s21,'c') 
pylab.plot(freq,s12,'m') 
pylab.plot(freq,s22,'g')
pylab.xlabel('Frequency')
pylab.ylabel('Log magtitude')
#pylab.ylim(-80,0)
pylab.axis([2E9, 2.2E9, -1, 0])
#pylab.legend()
pylab.show() 
