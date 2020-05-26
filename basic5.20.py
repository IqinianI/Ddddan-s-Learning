'''
def sale_car(price,length,hight,colour='red',brand='carny'):
    print('price:',price,
          'colour:',colour,
          'brand:',brand,
          'length:',length,
          'hight:',hight)
sale_car(1000,1000,2000)

class Calculator:
    name='Good calculator'
    price=18
    def __init__(self,name,price,hight,width,weight):
        self.name=name
        self.price=price
        self.h=hight
        self.w=width
        self.we=weight
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)

    def minus(self,x,y):
        result=x-y
        print(result)
'''

'''
a_input=input('Please give a number:')
if a_input=='1':
    print('this is a good one')
elif a_input=='2':
    print('this is second')
else:
    print('Good luck')
'''

'''
a_tuple=(12,3,4,5,6)
another_tuple=2,3,4,5,6
a_list=[12,3,4,5]

for index in range(len(a_list)):
    print('index:=',index,'number in list=',a_list[index])
'''

'''
a=[1,2,3,4,5,6]
#a.append(0)
#a.insert(1,0)index
#a.remove(2)value
print(a)
print(a[-1])
print(a[:3])
print(a.index(2))
print(a.count(-1))
a.sort()
a.sort(reverse=True)

a=[1,2,3,4,5]
multi_dim_a=[[1,2,3],
             [4,5,6],
             [7,8,9]]
'''

'''
#dictionary
d={key:value,...}
'''

'''
try:
    file=open('eeee','r+')
except Exception as e:
    print('there is no file named as eeee')
    response=input('Do you want to create a new file?')
    if response=='y':
        file=open('eeee','w')
    else:
        pass
else:
    file.write('ssss')
file.close()
   ''' 
'''
#zip迭代器的输出
a=[1,2,3]
b=[4,5,6]
list(zip(a,b))
for i,j in zip(a,b):
    print(i/2,j*2)

def fun(x,y):
    return x+y
fun1=lambda x,y:x+y
list(map(fun,[1,3,4],[2,6,8]))
    '''
'''
#set
char_list=['a','b','c','d','d','d']
sentence='welcome to Tiis tutorial'

#print(set(char_list))
#print(set(sentence))
unique_set=set(char_list)
#unique_set.add('x')
#unique_set.remove('x')
#print(unique_set)
set1=unique_set
set2={'a','e','x'}
print(set1.difference(set2))
print(set1.intersection(set2))
'''
'''
#正则表达式
import re
patten1='cat'
patten2='run'
string='dog runs to cat'
print(re.search(patten1,string))
print(re.search(patten2,string))

print(re.search(r"r[A-Z]n","dog runs to cat"))
print(re.search(r"r[a-z]n","dog runs to cat"))
print(re.search(r"r[0-9a-z]n","dog runs to cat"))
'''
'''
#多线程
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)

def mutilthreading():
    q=Queue()
    threads=[]
    data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result=[]
    for _ in range(4):
        result.append(q.get())
    print(result)
'''        
    
'''
def add_threading():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
    #print('this is a new threading,the number is %s'% threading.current_thread())

def thread2():
    print('T2 start\n')
    print('T2 finish\n')
    
def main():
    added_thread=threading.Thread(target=add_threading,name='T1')
    added_thread2=threading.Thread(target=thread2,name='T2')
    added_thread.start()
    added_thread2.start()
    added_thread.join()
    added_thread2.join()
    print('All done\n')
    #print(threading.active_count())
    #print(threading.enumerate())
    #print(threading.current_thread())
'''
'''
#多进程
import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)
    

if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p2=mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
   
    p2.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)
    #mutilthreading()

'''
#进程池
#多进程
import multiprocessing as mp
def job(x):
    return x*x

def multicore():
    pool=mp.Pool()
    res=pool.map(job,range(100000))
    print(res)

if __name__=='__main__':
    multicore()
    

    
    
    

