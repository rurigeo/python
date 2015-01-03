#!/usr/bin/env python
# coding = utf-8

#class switch(object):
#class switch():
class switch:
    __slots__ = ('master1','vender','__product') 
    def __init__(self,vender):
        self.vender = vender
        self.__product = "product"

    def get_product(self):
        return self.__product
    
    def set_product(self,product):
        self.__product = product
        
    def pro(self):
        print 'RF'
    def con(self):
        print 'ask who?'

class pin(switch):
    def pro1(self):   
        print 'fast switch and settling time'

    def con(self):
        print 'insertion loss'

class fet(switch):
    def con(self):
        print 'low isolation at high frequency'

    def pro(self):
        print 'esd protection'
        
pin.name = 'mini-circuits'
fet.name = 'peregrine'

print pin.name
print fet.name

isi = switch('insight')
print isi.vender
isi.vender = 'tuyue'
print isi.vender
#print isi.__product
isi.set_product('set a ball')
print isi.get_product()
isi.master1 = 'i am master'
print isi.master1

print isi.pro()
print pin('child').pro1()
"print switch.spec >>><unbound method switch.spec>"

#a = pin()
#b = switch()
#pin().pro()
#a.con()
#print isinstance(a,switch)
"isinstance() arg 2 must be a class, type, or tuple of classes and"
#print isinstance(b,pin)
