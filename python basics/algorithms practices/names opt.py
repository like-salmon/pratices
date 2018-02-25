#!/usr/bin/env python
#coding:utf-8

def namelist(names):
    """last two names concat with ‘&’，another with comma"""
    s=''
    a=[]
    if len(names)==0:
	return s
    for i in names[:len(names)-2]:
	s=s+i.values()[0]+","
    for i in names[-2:]:
	a.append(i["name"])
    s=s+"&".join(a)
    return s #'simon,alter,lily,wallen&george'
