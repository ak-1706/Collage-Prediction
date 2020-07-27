# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 05:41:33 2020

@author: a2aniket
"""


from os import listdir
from os.path import isfile, join
from data_mining import mine_data


get_college = [f for f in listdir("DSE Data/cap1 AllotmentFinal") if isfile(join("DSE Data/cap1 AllotmentFinal/", f))]



for college in get_college:
    path="DSE Data/cap1 AllotmentFinal/{}".format(college)
    mine_data(path, college)