import numpy as np

arr=np.arange(49).reshape(7,7)
print(arr)

arr[1:3,:2]=8
arr[4:6,4:6]=0
arr[4:6,1:4]=1
print(arr)
print(np.random.randn(5,4))