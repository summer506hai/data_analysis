# -*- coding:utf-8 -*-
import os
import shutil

'''
创建文件夹
'''
def mkdir(path):
    try:
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            print("There is this folder")
        return True
    except Exception as e:
        print('mkdir error: ',e)
        return False

'''
移动文件：将srcPath/fileName 移动到 dstPath/fileName
moveFile('dataset/pic','dataset/txt','09.jpg') 
'''
def moveFile(srcPath,dstPath,fileName):
    print('from: ',srcPath,' to: ', dstPath)
    try:
        f_src = os.path.join(srcPath,fileName)
        mkdir(dstPath)
        f_dst = os.path.join(dstPath,fileName)
        shutil.move(f_src,f_dst)
        return True
    except Exception as e:
        print('move file error: ',e)
        return False

'''
拷贝文件：将srcPath/fileName 拷贝到 dstPath/fileName
moveFile('dataset/pic','dataset/txt','09.jpg') 
'''
def copyFile(srcPath,dstPath,fileName):
    print('from: ',srcPath,' to: ', dstPath)
    try:
        f_src = os.path.join(srcPath,fileName)
        mkdir(dstPath)
        f_dst = os.path.join(dstPath,fileName)
        shutil.copyfile(f_src,f_dst)
        return True
    except Exception as e:
        print('copy file error: ',e)
        return False

'''
修改文件后缀名
修改dirPath路径下，fileType类型的后缀名为 newFileType
changeSuffix('dataset/pic','dataset/pic/',"jpg","png")
'''
def changeSuffix(dirPath,newPath,fileType,newFileType):
    try:
        g = os.walk(dirPath)
        for maindir,subdir,filename_list in g:
            for filename in filename_list:
                if filename.endswith(fileType):
                    newFileName = os.path.splitext(filename)[0] + "." + newFileType
                    newFileDir = newPath + newFileName
                    os.rename(os.path.join(maindir,filename),newFileDir)
        return True
    except Exception as e:
        print('change suffix error: ',e)
        return False

'''
查找文件,返回文件（加路径）
dirPath路径下，fileType格式的文件
searchFile('dataset/pic','jpg','png')
'''
def searchFile(dirPath,*fileType):
    try:
        g = os.walk(dirPath)
        file_path_name = [os.path.join(maindir,filename) for maindir,subdir,filename_list in g for filename in filename_list
                   if filename.endswith(fileType)]
        return file_path_name
    except Exception as e:
        print('search file error: ',e)
        return False

'''
查找文件,返回文件名(不带路径)
'''
def searchFileReturnName(dirPath,*fileType):
    try:
        g = os.walk(dirPath)
        file_name = [filename for maindir,subdir,filename_list in g for filename in filename_list
                   if filename.endswith(fileType)]
        return file_name
    except Exception as e:
        print('search file error: ',e)
        return False

'''
查找两个文件夹中不同名的文件
serachDiffFile('dataset/pic','dataset/txt','txt','jpg','png')
'''
def serachDiffFile(dirPathA,dirPathB,fileTypeA,*fileTypeB):
    try:
        fileNameA = searchFileReturnName(dirPathA,*fileTypeB)
        fileNameB = searchFileReturnName(dirPathB,fileTypeA)
        file_list_A = [os.path.splitext(x)[0] for x in fileNameA]
        file_list_B = [os.path.splitext(y)[0] for y in fileNameB]
        diff = list(set(file_list_A).difference(set(file_list_B))) #a 有 b没有
        diff2 = list(set(file_list_B).difference(set(file_list_A))) #b 有 a没有
        return diff,diff2
    except Exception as e:
        print('search file error: ',e)
        return False

if __name__ == '__main__':
    #print(serachDiffFile('dataset/pic', 'dataset/xml'))
    #print(moveFile('dataset/pic','dataset/txt','09.jpg'))
    #changeSuffix('dataset/pic','dataset/pic/',"jpg","png")
    #print(searchFileReturnName('dataset/pic','jpg','png'))
    #print(serachDiffFile('dataset/pic','dataset/txt','txt','jpg','png'))
    #copyFile('dataset/pic', 'dataset/txt', '09.png')

    #拷贝文件夹中制定类型的文件
    result = searchFileReturnName('dataset/pic','png')
    if not result:
        print('error')
    else:
        for i in result:
            copyFile('dataset/pic','dataset/txt',i)
