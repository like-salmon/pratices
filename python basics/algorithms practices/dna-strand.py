#!/usr/bin/env python
#coding:utf-8

def DNA_strand(s):
	dna=list(s)
	l=len(dna)
	n=0
	while n<l:
	    if "A"==dna[n]:
	        dna[n]="T"
	    elif "T"==dna[n]:
		dna[n]="A"
	    elif "G"==dna[n]:
		dna[n]="C"
	    else:
		dna[n]="G"
	    n+=1
	return "".join(dna)

