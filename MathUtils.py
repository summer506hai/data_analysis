# -*- coding:utf-8 -*-

def fibonacci_listsum(n): #list后一个为前面几个的和
    i = 0
    for i in range(len(n)-1):
        yield n[i]
        n[i],n[i+1] = n[i+1],n[i]+n[i+1]
    yield n[i+1]

def fibonacci_listsum_from_zero(n):#list后一个为前面几个的和,从0开始
    a = 0
    for _ in n:
        yield a
        _, a = _, a + _

if __name__ == '__main__':
    w_list = [1, 2, 3, 4]
    w_list_2 = [1, 2, 3, 4]

    for j in fibonacci_listsum(w_list):
        print(j) #1、3、6、10

    for j in fibonacci_listsum_from_zero(w_list_2):
        print(j) #0、1、3、6
