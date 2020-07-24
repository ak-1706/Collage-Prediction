# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:32:22 2020

@author: a2aniket
"""
import pandas as pd
import ghostscript
import camelot
from get_course_code import code

codee=[]
pdf=camelot.read_pdf("DSE Data/cap2 Allotment Final/1002_4.pdf",pages='all')
length = pdf.__len__()
for i in range(0,length):
    j=i
    if i % 2==0:
        pdf[i].to_csv("mined data/Cource/cource{}.csv".format(i))
    else:
        pdf[i].to_csv('mined data/Student info/student{}.csv'.format(j-1))
        dataframe=pd.read_csv('mined data/Student info/student{}.csv'.format(j-1))
        dataframe["Course"]=code("mined data/Cource/cource{}.csv".format(j-1))
        codee.append(code("mined data/Cource/cource{}.csv".format(j-1)))
        dataframe.to_csv('mined data/Student info/student{}.csv'.format(j-1))
