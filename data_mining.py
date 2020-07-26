# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:32:22 2020

@author: a2aniket
"""
import pandas as pd
import camelot
from get_course_code import code
import os

codee=[]
pdf=camelot.read_pdf("DSE Data/cap2 Allotment Final/2126_4.pdf",pages='all')
length = pdf.__len__()
college_code=1002
columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type"]
new_columns=["Sr.No.","Merit No","Marks","Application ID","Name of Candidate","Gender","Category","PWD/DEF","Sub Group","Seat Type","cource_code","college_code"]
for i in range(0,length):
    shape=pdf[i].shape
    if shape[1] <= 2:
        pdf[i].to_csv("mined data/Cap-1 Cource/cource{}-{}.csv".format(college_code,i))
        course_code=(code("mined data/Cap-1 Cource/cource{}-{}.csv".format(college_code,i)))
    else:
        if os.path.exists("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code)):
            dataFrame=pd.read_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))
            pdf[i].to_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))
            new_dataFrame=pd.read_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code),names=columns,header=0)
            new_dataFrame["cource_code"]=course_code
            new_dataFrame["college_code"]=college_code
            dataFrame=pd.concat([dataFrame[new_columns],new_dataFrame[new_columns]],ignore_index=True)
            #dataFrame.append(new_dataFrame)
            dataFrame.to_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))
        else:
            pdf[i].to_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))
            dataFrame=pd.read_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))
            dataFrame["cource_code"]=course_code
            dataFrame["college_code"]=college_code
            dataFrame.to_csv("mined data/Cap-1 Student info/student{}-{}.csv".format(course_code,college_code))