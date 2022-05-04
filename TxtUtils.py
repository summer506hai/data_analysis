# -*- coding:utf-8 -*-
'''
txt相关操作
'''

def write2txt(txt_file,content_str): #覆盖之前的内容
    try:
        with open(txt_file,'w+',encoding='utf-8') as f:
            f.write(content_str)
        return True
    except Exception as e:
        print(e)
        return False

def write2txt_add(txt_file,content_str): #在后面追加
    try:
        with open(txt_file,'a+',encoding='utf-8') as f:
            f.write(content_str)
        return True
    except Exception as e:
        print(e)
        return False

def read_txt(txt_file):
    try:
        data=[]
        for line in open(txt_file,'r',encoding='utf-8'): #读取每一行，放到list中
            data.append(line.replace("\n",""))
        return data
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    print(write2txt_add('dataset/txt/write01.txt','hello'))
    data = read_txt('dataset/txt/write01.txt')
    print(data)

