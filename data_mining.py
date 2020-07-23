# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:32:22 2020

@author: a2aniket
"""

import ghostscript
import camelot

pdf=camelot.read_pdf("DSE Data/cap2 Allotment Final/1002_4.pdf",pages='all')
length = pdf.__len__()
for i in range(0,length):
    j=i
    if i % 2==0:
        pdf[i].to_csv("mined data/cource{}.csv".format(i))
    else:
        pdf[i].to_csv('mined data/foo{}.csv'.format(j-1))
