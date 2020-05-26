import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
from matplotlib import animation
'''
x=np.linspace(-3,3,50)
y1=2*x+1
#y2=x**2


plt.figure()
plt.plot(x,y1)
#######################################
#figure参数：number,figsize
#两个线显示在同一个figure,figure开头，后面都和这个有关
#设置图例

plt.figure(num=3,figsize=(8,5)) 
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
l1,=plt.plot(x,y1,label='up')
l2,=plt.plot(x,y2,label='down')
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')

######################################
#坐标轴设置
#横纵坐标值修改

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
#横纵坐标轴区间
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           ['$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])

#####################################
#移动横纵坐标位置
ax=plt.gca()#获取当前坐标轴位置
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')#右边和上面轴线不显示
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

################################
#设置标注
x0=1
y0=2*x0+1
#标点
plt.scatter(x0,y0,s=50,color='b')
#标线
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
#method 1
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',textcoords='offset points',
             xytext=(+30,-30),fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
#method 2
plt.text(-3.9,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',fontdict={'size':16,'color':'r'})

plt.show()


####################################
#scatter图
n=1024
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)#for color value
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks(())
plt.yticks(())
plt.show()


######################################
#bar图
n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x + 0.4,y + 0.05,'%.2f'%y,ha='center',va='bottom')

for x,y in zip(X,Y2):
    plt.text(x + 0.4,- y - 0.05,'-%.2f'%y,ha='center',va='top')

plt.show()

###################################
#contours等高线图
def f(x,y):
    #the contours function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)#x,y对应至网格
#use plt.contourf to filling contours
#X,Y and value for f(X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#use plt.contour to add contour lines
C=plt.contour(X,Y,f(X,Y),8,alpha=0.75,colors='black',linewidth=.5)
#adding label
plt.clabel(C,inline=True,fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()

#####################################
#image
a=np.array([]).reshape(3,3)
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shink=)

####################################
#3D
fig=plt.figure()
ax=Axes3D(fig)
#X,Y value
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()

#####################################
#subplot多图合并
plt.figure()
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])
plt.subplot(2,3,5)
plt.plot([0,1],[0,3])
plt.subplot(2,3,6)
plt.plot([0,1],[0,4])

plt.show()

######################################
#subplot分格显示
#method 1 :subplot2grid
plt.figure()
ax1=plt.subplot2grid((3,3),(0,0),colspan=3)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax3=plt.subplot2grid((3,3),(1,2),rowspan=2,colspan=1)
ax4=plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
ax5=plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)
plt.show()

#method 2:gridspec
plt.figure()
gs=girdspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:2])
ax3=plt.subplot(gs[1:,2])
ax4=plt.subplot(gs[-1,0])
ax5=plt.subplot(gs[-1,-2])
plt.show()

#method 3 :easy to define structure
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[2,1])

plt.tight_layout()
plt.show()


#######################################
#plot in plot图中图
fig=plt.figure()
x=[1,2,3,4,5,6,7]
y=[1,3,4,2,5,8,6]

left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('ax1_title')

left,bottom,width,height=0.2,0.6,0.25,0.25
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')


plt.show()


#######################################
#主次坐标轴
x=np.arange(0,10,0.1)
y1=0.05*x**2
y2=-1*y1

fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b-')
ax1.set_xlabel('X data')
ax2.set_ylabel('Y2',color='b')
ax1.set_ylabel('Y1',color='g')
plt.show()
'''

################################################
fig,ax=plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata=(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata=(np.sin(x))
    return line,

ani=animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)
plt.show()
