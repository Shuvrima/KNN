#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:51:34 2019

@author: shuvrimaalam
"""

import pandas
import operator


train_data = pandas.DataFrame()          # declare empty dataframe
test_data = pandas.DataFrame()

def read_file():
    train_data = pandas.read_csv("train_1.txt",delimiter=r"\s+") #read from file
    test_data = pandas.read_csv("test_1.txt",delimiter=r"\s+")
    test_list=[] #store data in list
    train_list=[]
    l1=[]

    for y in train_data.itertuples():
        #train_list.append(y)
        l1=[i for i in y[1:]]
        train_list.append(l1)
    for z in test_data.itertuples():
        test_list=[j for j in z[1:]]
        #print(test_list)
    return train_list, test_list



def hamming_dist(dt1,dt2):
    ham_dist=[]
    all_points=[]
    print(dt1)
    for x in range(len(dt1)):
        print("----")
        n = 0
        for i,j in zip(dt1[x],dt2):
            print('i,j',i,j)
            if i != j:
               n += 1
        ham_dist.append(n)
        all_points.append((dt1[x],n))
        #print(all_points)

    print(ham_dist)
    #print(all_points[0][0])
    #print(all_points)
    ham_dist.sort()
    #print(n)
    return all_points


def knn(all_points,k):
    #neighbours = ham_dist[:k]
    #print(neighbours)
    label = {}
    get_dist = operator.itemgetter(1)
    map(get_dist,all_points)
    final_list = sorted(all_points,key=get_dist)
    #print(final_list[0][0][-1])
    print(final_list)

    s = final_list[:k]

    for item in s:
        print('item : ',item[0][-1])
        if(item[0][-1] in label):
            label[item[0][-1]] += 1
        else:
            label[item[0][-1]] = 1

    print(label)
    final_class=list(label)[0]
    print(final_class)
    return final_class


if __name__ == "__main__":
    dt1,dt2 = read_file()
    a=hamming_dist(dt1,dt2)
    k = int(input('enter for k:'))
    knn(a,k)