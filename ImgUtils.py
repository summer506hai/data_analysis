# -*- coding:utf-8 -*-
'''
图片相关操作
'''
from PIL import Image,ImageFile

from FileUtils import searchFile
from MathUtils import fibonacci_listsum, fibonacci_listsum_from_zero

ImageFile.LOAD_TRUNCATED_IMAGES = True

def resize_img(pic,width):
    PicFile = Image.open(pic)
    width1,height1 = PicFile.size
    newheight1 = int(height1 * (width / width1))
    PicFile = PicFile.resize((width,newheight1),Image.ANTIALIAS) #高质量改变图片尺寸

    left = 0
    up = 0
    right = width
    blow = (newheight1 + width) / 2
    newPicFile = PicFile.crop((left,up,right,blow))
    newW,newH = newPicFile.size
    return newW,newH,newPicFile


def DrawPic_with3pic(img_path,outpath,pic):
    """
    将3张图片横向拼接在一起
    :param pic1: 第一张图片
    :param pic2: 第一张图片
    :param pic3: 第一张图片
    :param outpath: 输出路径
    :param pic: 输出文件名
    :return:
    """
    newW_list, newH_list, newPicFile_list,w_list,w_list_2 = [],[],[],[],[]
    img_list = searchFile(img_path,"png","jpg")
    if len(img_list) <= 1:
        return False,"少于2张图片，无需拼接"

    PicFile = Image.open(img_list[0])
    width, height = PicFile.size

    for i in range(1,len(img_list)):
        newW, newH, newPicFile = resize_img(img_list[i],width)
        newW_list.append(newW)
        newH_list.append(newH)
        newPicFile_list.append(newPicFile)

    newH = max(height,max(newH_list))
    newImage = Image.new('RGB',(width+sum(newW_list),newH))
    newImage.paste(PicFile,(0,0,width,height))

    for i in fibonacci_listsum_from_zero(newW_list):
        #print(i)
        w_list.append(i)

    for i in fibonacci_listsum(newW_list):
        #print(i)
        w_list_2.append(i)

    for i in range(len(newW_list)):
        newImage.paste(newPicFile_list[i], (width + w_list[i], 0, width+w_list_2[i] , newH_list[i]))

    newImage.save(outpath+''+pic)


if __name__ == "__main__":
    DrawPic_with3pic("dataset/images","dataset/","out1.png")




