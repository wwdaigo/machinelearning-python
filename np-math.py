import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

v = np.array([9,10])
w = np.array([11,12])

xy_sum = x + y # = np.add(x,y)
'''
[[  6.   8.]
 [ 10.  12.]]
 '''

xy_diff = x-y # = np.subtract(x,y)
'''
[[-4. -4.]
 [-4. -4.]]
 '''

xy_multiply_elementwise = x*y # = np.multiply(x, y)
'''
[[  5.  12.]
 [ 21.  32.]]
'''

xy_divide_elementwise = x/y # = np.divide(x,y)
'''
[[ 0.2         0.33333333]
 [ 0.42857143  0.5       ]]
 '''

x_square_root = np.sqrt(x)
'''
[[ 1.          1.41421356]
 [ 1.73205081  2.        ]]
 '''

vw_matrix_multiplication = v.dot(w) # = np.dot(v,w)
#219

xv_matrix_multiplication = x.dot(v)
#[ 29.  67.]


x_all_elements_summation = np.sum(x)
#10.0

x_all_elements_summation_each_col = np.sum(x, axis=0)
#[ 4.  6.]

x_all_elements_summation_each_row = np.sum(x, axis=1)
#[ 3.  7.]

x_transposed = x.T
'''
[[ 1.  3.]
 [ 2.  4.]]
 ''
print x_transposed