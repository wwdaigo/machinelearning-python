import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''

b = a[:2, 1:3] # :2 = 0:2 > first two rows. 1:3 > starting from index 1 and ending at 3. (2 cols)
'''
[[2 3]
 [6 7]]
 '''

row_r1 = a[1, :] # whole second row
'''
[5 6 7 8]
'''
row_r2 = a[1:2, :] #whole second row (2nd rank)
'''
[[5 6 7 8]]
'''

new_a = np.array([[1,2],[3,4],[5,6]])
print new_a[[0,1,2], [0,1,0]]
print np.array([new_a[0,0], new_a[1,1], new_a[2,0]])
#[1 4 5]

print new_a[[0,0], [1,1]] #[2 2]
'''
new_a[0] = [1,2]
new_a[[0]] = [[1,2]]
new_a[[0,0]] = [[1 2]
 				[1 2]]
new_a[[0,0], [1,1]] = [2 2]
'''

c = np.array([0,2,1])
print a[np.arange(3), c] #select one element from each row of a, using indices in c
#[ 1  7 10]

a[np.arange(3), c] += 10 #mutates the elements in a using indices in c
print a
'''
[ 5  6 17  8]
 [ 9 20 11 12]]
 '''
print a[a>3] #[11  4  5  6 17  8  9 20 11 12]
