#!/usr/bin/env python3

class Tesst:
  Z=99
  def __getattr__(self, name):
    self.name1 = name
    print('getattr= ')
 
  #def __getattribute__(self, name):
    #self.name2 = name
    #print('__getattribute__= ')
