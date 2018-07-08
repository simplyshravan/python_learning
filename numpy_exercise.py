import numpy as np
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)
print(np.arange(10,51))
#arr=np.arange(10,51)
#arr1=list(filter(lambda x:x%2==0,arr))
print(list(filter(lambda x:x%2==0,np.arange(10,51))))
print(np.arange(0,9).reshape(3,3))
print(np.identity(3))
print(np.random.rand(1))
print(np.random.randn(25))
print(np.random.rand(100).reshape(10,10))

print(np.arange(1,101).reshape(10,10) /100)
print(np.linspace(0,1,20))

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])

print(mat[3,4])

print(mat[0:3,1:2])

print(mat[3:])


print(sum(sum(mat)))
print(len(mat))

#print(mat.mean())
#print(mat.average())

print(np.sqrt(sum(sum((mat-(sum(sum(mat))/25))*(mat-(sum(sum(mat))/25))))/25))

print(sum(mat))
