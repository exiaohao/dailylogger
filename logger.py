#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime

CURRENT_PATH = os.path.abspath(__file__).rsplit('/', 1)[0]
LogDATEFORMAT = '%Y%m%d'

class logger(object):
    def __init__(self):
        pass
    def today(self):
        print(datetime.date.today())
        pass
    def write(word):
        #文件路径
        file_path = CURRENT_PATH + '/logs/' + str(datetime.date.today())
        #读追加/不存在则新建
        try:
            f = open(file_path, 'a')
            #写入
            f.write(word)
            f.write("\n")
            return 1
        except Exception as err:
            print(err)
            return 0

    def read(day = 'NULL'):
        if day == 'NULL':
            day = str(datetime.date.today())
        #产生文件路径
        file_path = CURRENT_PATH + '/logs/' + str(day)
        #读文件
        f = open(file_path, 'r')
        read_result = f.read()
        print(read_result)