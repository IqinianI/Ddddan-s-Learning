import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#导入数据
'''
#define and output
#直接导入数据定义pandas
s=pd.Series([1,3,6,np.nan,44,1])
print(s)

#用numpy导入数据
#自定义index和columns
dates=pd.date_range('20160101',periods=6)
df1=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df2=pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
print(df2)

#用字典导入数据
df3=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20200524'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test","train","test","train"]),
                  'F':'foo'})
print(df3)

#查看数据
df3.index
df3.columns
df3.values
df3.describe()
df3.sort_index(axis=1,ascending=False)
df3.sort_values(by='E')

'''
#选择数据
'''
dates=pd.date_range('20200524',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])

#简单输出方法
#print(df['A'])
#print(df.A)
#print(df[0:3],df['20200524':'20200526'])

#复杂输出方法

#select by label:loc
#print(df.loc['20200524'])
#print(df.loc[:,['A','B']])
#print(df.loc['20200524',['A','B']])

#select by position:iloc
#print(df.iloc[:,1:3])

#select by mixed:ix
#print(df.ix[:3,['A','C']])

#Boolean indexing
print(df[df.A<8])

'''
#pandas设置值
'''
dates=pd.date_range('20200524',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
df.iloc[2,2]=1111
df.loc['20200524','B']=2222
df.B[df.A>4]=0
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20200524',periods=6))
print(df)
'''

#处理丢失数据
'''
dates=pd.date_range('20200524',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
df.iloc[1,2]=np.nan
df.iloc[0,1]=np.nan
#print(df.dropna(axis=0,how='any'))
#print(df.fillna(value=0))
print(np.any(df.isnull())==True)
'''
#pandas导入：pd.read_格式(文件)
#pandas导出：pd.to_格式(文件)


#pandas合并——concat
#concatenating
'''
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
'''
#join {'inner','outer'}
'''
#默认outer，在不同的地方补NaN
#inner，把不同的地方删除
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)
#join_axes
#默认补NaN
#也可按照某行列索引，忽略多余的
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)
'''
#append尾加
#res=df1.append(df2)

#合并merge
'''
#merge by key/keys
#how={'right','left',outer'.,'inner'}
#indicator={true,false},合并形式输出
res=pd.merge(data1,data2,on=按什么关键字合并,how=，indicator=)

#left_index and right_index={true,false}:不是按key合并而是索引
res=pd.merge(data1,data2,left_index=,right_index=,how=)

#handle overlapping:区分名字同，内涵不同的数据
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how=)
'''

#plot画图
#series
'''
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.comsum()
data.plot()
plt.show()
'''
#DataFrame
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD")
                  )
data=data.cumsum()
#data.plot()
#plt.show()
#plot methods:
#bar,hist,box,kde,area,scatter,pie
ax=data.plot.scatter(x='A',y='B',color='Blue',label='Class 1')
data.plot.scatter(x='A',y='C',color='Green',label='Class 2',ax=ax)
plt.show()










