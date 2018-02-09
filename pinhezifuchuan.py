#!/usr/bin python
#coding:utf-8

"""
拼接颜色坐标差字符串
"""

import re

def x():
    s=""
    #抓取颜色的正则
    pat='\"(.*)\"'
    p=re.compile(pat)
    a=[i for i in raw_input("请输入首次颜色编码和坐标,以空格隔开!\n").split(" ") if i]#去空
   #首次颜色坐标1
    print a
    v1=int(a[1])
    #首次颜色坐标2
    v2=int(a[2])
    v0=re.sub("#","0x",p.search(a[0]).group(1))
    s=s+v0
    while True:
        b=[j for j in raw_input("请输入其他颜色编码和坐标,以空格隔开!\n").split(" ") if j]#去空
        if len(b):#需要判断里面的值是否为空
            print len(b)
            s+=","+str(int(int(b[1])-v1))+","+str(int(int(b[2])-v2))+","+re.sub("#","0x",p.search(b[0]).group(1))
        else:
            break
    print s

if __name__ == "__main__":
    x()
