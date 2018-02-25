#!/usr/bin/env python
#coding:utf-8
import numpy as np
def done_or_not(board):
    b=len([i for i in board if len(set(filter(lambda x:0<=x<=9,i)))==9 and sum(set(filter(lambda x:0<=x<=9,i)))==sum(range(10))])==9 or False
    blist = np.swapaxes(np.array(board),0,1)#np.array(board).T
    c=len([i for i in blist if len(set(filter(lambda x:0<=x<=9,i)))==9 and sum(set(filter(lambda x:0<=x<=9,i)))==sum(range(10))])==9 or False
    clist=np.array(board).reshape(3,3,3,3).transpose(2,0,1,3).reshape(9,9)
    d=len([i for i in clist if len(set(filter(lambda x:0<=x<=9,i)))==9 and sum(set(filter(lambda x:0<=x<=9,i)))==sum(range(10))])==9 or False
    if b and c and d:
        return "Finished!"
    return 'Try again!'

#details on transpose(*axis)#left section
"""
usually a n-d array ,its axis is like(0,1,2,...),if you transpose it,
then you need to transpose its axis,like ,transpose(2,0,1),this array's original position is
(0,1,2)
transpose matrix according to its shape(2,8),2-d array
"""

[[0,3],[0,3]],[[3,6],[0,3]],[[6,9],[0,3]]
#[[0:3,0:3]],[[3:6,0:3]],[[6:9,0:3]]
#middle section
[[0,3],[3,6]],[[3,6],[3,6]],[[6,9],[3,6]]
#[[0:3,3:6]],[[3:6,3:6]],[[6:9,3:6]]
#right section
[[0,3],[6,9]],[[3,6],[6,9]],[[6,9],[6,9]]
#[[0:3,6:9]],[[3:6,6:9]],[[6:9,6:9]]

#list comprehension:
f=lambda x:[y for sub_li in x for y in sub_li]
#retrieve first section:
f([a[row][0:3] for row in range(3)]) # retrieves the first section
#>>> [1, 3, 2, 4, 9, 8, 7, 5, 6]

#retrieve left section:
[f([a[row][0:3] for row in range(y*3, y*3+3)]) for y in range(3)]
#>>> [[1, 3, 2, 4, 9, 8, 7, 5, 6], [6, 4, 3, 5, 2, 1, 9, 8, 7], [2, 1, 4, 3, 6, 5, 8, 7, 9]]

#retrieve all sections:
[[f([a[row][x*3:x*3+3] for row in range(y*3, y*3+3)]) for y in range(3)] for x in range(3)]

0,3
0,6
0,9

3,3
3,6
3,9

6,3
6,6
6,9
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

