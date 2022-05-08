# -*- coding:utf-8 -*-
'''
图片相关操作
'''
from PIL import Image,ImageFile

from FileUtils import searchFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def DrawPic_with3pic(pic1,pic2,pic3,outpath,pic):
    """
    将3张图片横向拼接在一起
    :param pic1: 第一张图片
    :param pic2: 第一张图片
    :param pic3: 第一张图片
    :param outpath: 输出路径
    :param pic: 输出文件名
    :return:
    """
    PicFile = Image.open(pic1)
    width,height = PicFile.size

    PicFile1 = Image.open(pic2)
    width1,height1 = PicFile1.size
    newheight1 = int(height1 * (width / width1))
    PicFile1 = PicFile1.resize((width,newheight1),Image.ANTIALIAS) #高质量改变图片尺寸

    left = 0
    up = 0
    right = width
    blow = (newheight1 + width) / 2
    newPicFile1 = PicFile1.crop((left,up,right,blow))
    newW1,newH1 = newPicFile1.size

    PicFile2 = Image.open(pic3)
    width2, height2 = PicFile2.size
    newheight2 = int(height2 * (width / width2))
    PicFile2 = PicFile2.resize((width, newheight2), Image.ANTIALIAS)  # 高质量改变图片尺寸

    left = 0
    up = 0
    right = width
    blow = (newheight2 + width) / 2
    newPicFile2 = PicFile2.crop((left, up, right, blow))
    newW2, newH2 = newPicFile2.size

    newH = max(height,newH1,newH2)
    newImage = Image.new('RGB',(width+newW1+newW2,newH))
    newImage.paste(PicFile,(0,0,width,height))
    newImage.paste(newPicFile1, (width, 0, width + newW1, newH1))
    newImage.paste(newPicFile2, (width + newW1, 0, width + newW1 + newW2, newH2))
    newImage.save(outpath+''+pic)



if __name__ == "__main__":
    DrawPic_with3pic("dataset/pic/09.png","dataset/pic/21.jpg","dataset/pic/025.png","dataset/pic/","out.png")




