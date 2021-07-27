# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:27:41 2021

@author: dkjua
"""
mylist=[]
stu=int(input('學生人數?'))
i=0
while i<stu:
    x=int(input('成績?'))
    mylist.append(x)
    i=i+1
high=max(mylist)
low=min(mylist)
s=sum(mylist)
print(str(high))
print(str(low))
print(str(s//stu))




