# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:41:57 2020

@author: K0718
"""





x = 1 

def foo():
    x = 2 
    def innerfoo():
        x = 3 
        print ('locals ', x)
    innerfoo()
    print ('enclosing function locals ', x)

foo()
print ('global ', x)


#def innerfoo():：Local， 函數本身命名空間
#def foo():：Enclosing function locals；外部函數命名空間
#module(文件本身)：Global(module)；函数所在文件名字空間
#Python内置模組的名字空間





