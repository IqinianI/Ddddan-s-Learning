import numpy as np

#array一维
'''
array=np.array[[1,2,3],[4,5,6]]

print(array)
print('dim:',array.ndim)
print('shape:',array.shape)
print('size:',array.size)
'''
#特殊矩阵的定义
'''
zreo=np.zeros((2,3))
one=np.ones((2,3))
empty=np.empty((2,3))
a=np.arange(12).reshape((3,4))
lines=np.linshape(1,10,20)
'''
#矩阵的运算
'''
a=np.array([[1,2],[1,0]])
b=np.range(4)
print(a+b)
#点乘
print(a*b)
#矩阵乘法
print(np.dot(a,b))
print(a.dot(b))
#随机生成矩阵
a=np.random.random((2,4))
#矩阵的计算
print(a)
print(sum(a),axis=1)
print(min(a),axis=0)
print(max(a),axis=1)

A=np.range(2,14).reshape((3,4))
#最大值和最小值的索引
print(A.argmin())
print(np.argmin(A))
print(A.argmax())
#平均值
print(A.mean())
print(np.mean(A))
#中位数
print(np.median(A))
#累加
print(np.cumsum(A))
#累差
print(np.diff(A))
#非0
print(np.nonzero(A))
#排序
print(np.sort(A),axis=1)
#转置
np.transport(A)
print((A.T)*dot(A))
#截取替换
np.clip(A,5,9)
'''
#numpy 索引
'''
A=np.range(3,15).reshape((3,4))
#某一具体值的索引
print(A[1,:])
print(A[1][:])
#输出行
for row in A:
    print(row)
#输出列
for column in A.T:
    print(column)
'''
#numpy合并
'''
A=np.array([1,1,1])
B=np.array([2,2,2])
#在列上加维度
A=np.array([1,1,1])[:,np.nexaxis]
B=np.array([2,2,2])[:,np.newaxis]
#合并1
C=np.vstack((A,B))
D=np.hstack((A,B))
print(C.shape,D.shape)
#合并2
C=np.concatenate((A,A,B,B),axis=1)
print(C)
'''
#numpy分割
'''
A=np.range(12).reshape((3,4))
#不能做不等的分割
print(np.split(A,2,axis=1))
#不等分割
print(np.array_split(A,3,axis=1))
'''

#numpy copy and deepcopy
b=a.copy() #deepcopy


