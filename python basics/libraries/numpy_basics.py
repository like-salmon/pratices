#!/usr/bin/env python
#coding:utf-8

import numpy as np

#crate an array
a=np.array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
#in numpy array 's axis ,axis' number refers to the number of axes needed to index it.not the geometrical space concept.
#exchange different axises.

"""
for example :
a=array([[1, 3, 2, 5, 7, 9, 4, 6, 8],
       [4, 9, 8, 2, 6, 1, 3, 7, 5],
       [7, 5, 6, 3, 8, 4, 2, 1, 9],
       [6, 4, 3, 1, 5, 8, 7, 9, 2],
       [5, 2, 1, 7, 9, 3, 8, 4, 6],
       [9, 8, 7, 4, 2, 6, 5, 3, 1],
       [2, 1, 4, 9, 3, 5, 6, 8, 7],
       [3, 6, 5, 8, 1, 7, 9, 2, 4],
       [8, 7, 9, 6, 4, 2, 1, 5, 3]])
after reshape:
b=a.reshape(3,3,3,3)

b's strides is:(216, 72, 24, 8),for number ,each take up 8 bits in memory,so,
b's strides in num is (27,9,3,1),in axises ,it is (0,1,2,3)

because in memory ,a is list like[1,2,3,4,5,6....7,8,9],81 numbers listed in series,continuously.

from a to b,b's strides is:
(216,72,24,8),that is (27,9,3,1)
for the outer axis 3,numpy moves 27 steps,
for axis 2,numpy moves 9 steps to next value in this axis,
for axis 1,numpy moves 3 steps to next value in this axis,
for axis 0,numpy moves 1 step to next value in this axis.

so,for b ,its axises list like 0,1,2,3
b.transpose(2,0,1,3).strides => (24,216,72,8) =>(3,27,9,1)
for axis 3,numpy moves 1 step to get to next value in this axis,
for axis 2,numpy moves 3 steps to get to next value in this axis,
for axis 1,numpy moves 9 steps to get to next value in this axis,
for axis 0,numpy moves 27 steps to get to next value in this axis.

sequence is:from within the n-d array,and outer.
b=array([[[[1, 3, 2],    
         [5, 7, 9],
         [4, 6, 8]],

        [[4, 9, 8],
         [2, 6, 1],
         [3, 7, 5]],

        [[7, 5, 6],
         [3, 8, 4],
         [2, 1, 9]]],


       [[[6, 4, 3],
         [1, 5, 8],
         [7, 9, 2]],

        [[5, 2, 1],
         [7, 9, 3],
         [8, 4, 6]],

        [[9, 8, 7],
         [4, 2, 6],
         [5, 3, 1]]],


       [[[2, 1, 4],
         [9, 3, 5],
         [6, 8, 7]],

        [[3, 6, 5],
         [8, 1, 7],
         [9, 2, 4]],

        [[8, 7, 9],
         [6, 4, 2],
         [1, 5, 3]]]])
"""
a.T
#same as  np.swapaxes(np.array(board),0,1)
"""
array([[ 2.,  4.,  8.],
       [ 8.,  5.,  9.],
       [ 0.,  1.,  3.],
       [ 6.,  1.,  6.]])
"""
#sum up each column
a.sum(axis=0)

#sum up each row
a.sum(axis=1)

#get the min value of each row:
a.min(axis=1)

#create two dimensions array:
a=np.arange(16).reshape((2,8))

