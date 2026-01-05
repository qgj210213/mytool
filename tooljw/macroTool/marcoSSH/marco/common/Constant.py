# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:34:47 2021

@author: ts-guangjie.qi
"""

class Constants(object):
  def __init__(self):
    self.__PI = 3.1415926
    self.__const_suffix_bat=".bat"
 
  @property
  def PI(self):
    return self.__PI
  @property
  def const_suffix_bat(self):
    return self.__const_suffix_bat
 
constant = Constants()
print(constant.PI)
print(constant.const_suffix_bat)