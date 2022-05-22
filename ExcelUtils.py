# -*- coding:utf-8 -*-
'''
excel相关操作
'''
import os
import pandas as pd

from FileUtils import searchFile


def merge_muti_excel_to_one(out_file):
    '''
    将多个excel放到excel不同的sheet中
    :return:
    '''
    file_name_list = searchFile('dataset/excel',"xlsx")
    print(file_name_list)
    writer = pd.ExcelWriter(out_file)
    for file_name in file_name_list:
        data_each = pd.read_excel(file_name,engine='openpyxl')
        data_each.to_excel(writer,os.path.splitext(os.path.basename(file_name))[0],index=False)
    writer.save()

if __name__ == "__main__":
    merge_muti_excel_to_one('dataset/out.xlsx')