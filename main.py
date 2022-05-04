# -*- coding:utf-8 -*-
import FileUtils

def main():
    #print(FileUtils.serachDiffFile('dataset/pic', 'dataset/xml'))
    #print(FileUtils.moveFile('dataset/pic','dataset/txt','09.jpg'))
    #FileUtils.changeSuffix('dataset/pic','dataset/pic/',"jpg","png")
    #print(FileUtils.searchFileReturnName('dataset/pic','jpg','png'))
    print(FileUtils.serachDiffFile('dataset/pic','dataset/txt','txt','jpg','png'))

if __name__ == '__main__':
    main()