---
layout: default
title:  散图案例
parent: Matplotlib
nav_order: 12
---
# Matplotlib 50 例


Matplotlib学习我们其实不需要在上面花费太多精力, 以理解为主, 理解绘图原理和过程.

一旦需要实际画图, 则按下面的图例找到对应的Demo复制后填充弄数据即可, 下面是分类的示例集合.

可能用到的函数/图形有如下:
-  plot
- scatter
- pie
- errorbar
- bar
- barh: 水平方向柱状图
- hist: 直方图
- axhline: 水平参考线
- axvsapn/axhspan: 水平/垂直参考区域
- text: 显示文字
- plt.annotate: 注释箭头
- ax.legend(): 示例
- plt.Line2D: 线
- ax.add_artist(leg): 把一个Artist实例添加到Axes上
- imshow: 显示色图
- plt.colorbar: 显示色卡条
- ax1 = plt.axes: 生成一个Axes实例
- ax1 = fig.add_axes: 生成一个Axes实例
- plt.subplot: 生成一个子图
- plt.figure: 生成一个Figure
- plt.subplots: 生成N多个子图
- plt.GridSpec: 生成子图用的网格
- ax.plot3D: 生成3D线
- ax.scatter3D
- ax.stackplot(x, y1, y2, y3)


## 导入
### 导入matplotlib库简写为plt


```python
import matplotlib.pyplot as plt
import numpy as np
```

## 基本图表
### 用plot方法画出x=(0,10)间sin的图像


```python
x = np.linspace(0, 10, 30)
plt.plot(x, np.sin(x));
```


![png](./output_5_0.png)


### 用点加线的方式画出x=(0,10)间sin的图像


```python
plt.plot(x, np.sin(x), '-o');
```


![png](output_7_0.png)


### 用scatter方法画出x=(0,10)间sin的点图像


```python
plt.scatter(x, np.sin(x));
```


![png](output_9_0.png)


### 用饼图的面积及颜色展示一组4维数据


```python
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar(); # 展示色阶
```


![png](output_11_0.png)


### 绘制一组误差为±0.8的数据的误差条图


```python
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k')
```




    <Container object of 3 artists>




![png](output_13_1.png)


### 绘制一个柱状图


```python
x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]
label=['A','B','C','D','E','F','G','H']

plt.bar(x,y,tick_label = label);
```


![png](output_15_0.png)


### 绘制一个水平方向柱状图


```python
plt.barh(x,y,tick_label = label);
```


![png](output_17_0.png)


### 绘制1000个随机值的直方图


```python
data = np.random.randn(1000)
plt.hist(data);
```


![png](output_19_0.png)


### 设置直方图分30个bins，并设置为频率分布


```python
plt.hist(data, bins=30,histtype='stepfilled', density=True)
plt.show();
```


![png](output_21_0.png)


### 在一张图中绘制3组不同的直方图，并设置透明度


```python
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(alpha=0.3, bins=40, density = True)

plt.hist(x1, **kwargs);
plt.hist(x2, **kwargs);
plt.hist(x3, **kwargs);
```


![png](output_23_0.png)


### 绘制一张二维直方图


```python
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T
plt.hist2d(x, y, bins=30);
```


![png](output_25_0.png)


### 绘制一张设置网格大小为30的六角形直方图


```python
plt.hexbin(x, y, gridsize=30);
```


![png](output_27_0.png)


## 自定义图表元素
### 绘制x=(0,10)间sin的图像，设置线性为虚线


```python
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x),'--');
```


![png](output_29_0.png)


### 设置y轴显示范围为(-1.5,1.5)


```python
x = np.linspace(0,10,100)
plt.plot(x, np.sin(x))
plt.ylim(-1.5, 1.5);
```


![png](output_31_0.png)


### 设置x,y轴标签variable x，value y


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('variable x');
plt.ylabel('value y');
```


![png](output_33_0.png)


### 设置图表标题“三角函数”


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.title('三角函数');
```


![png](output_35_0.png)


### 显示网格


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.grid()
```


![png](output_37_0.png)


### 绘制平行于x轴y=0.8的水平参考线


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.axhline(y=0.8, ls='--', c='r')
```




    <matplotlib.lines.Line2D at 0x21e8e614eb8>




![png](output_39_1.png)


### 绘制垂直于x轴x<4 and x>6的参考区域，以及y轴y<0.2 and y>-0.2的参考区域


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.axvspan(xmin=4, xmax=6, facecolor='r', alpha=0.3) # 垂直x轴
plt.axhspan(ymin=-0.2, ymax=0.2, facecolor='y', alpha=0.3);  # 垂直y轴
```


![png](output_41_0.png)


### 添加注释文字sin(x)


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.text(3.2, 0, 'sin(x)', weight='bold', color='r');
```


![png](output_43_0.png)


### 用箭头标出第一个峰值


```python
x = np.linspace(0.05, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.annotate('maximum',xy=(np.pi/2, 1),xytext=(np.pi/2+1, 1),
             weight='bold',
             color='r',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'));
```


![png](output_45_0.png)


## 自定义图例
### 在一张图里绘制sin,cos的图形，并展示图例


```python
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin')
ax.plot(x, np.cos(x), '--', label='cos')
ax.legend();
```


![png](output_47_0.png)


### 调整图例在左上角展示，且不显示边框


```python
ax.legend(loc='upper left', frameon=False);
fig
```




![png](output_49_0.png)



### 调整图例在画面下方居中展示，且分成2列


```python
ax.legend(frameon=False, loc='lower center', ncol=2)
fig
```




![png](output_51_0.png)



### 绘制的图像，并只显示前2者的图例


```python
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

# lines 是 plt.Line2D 类型的实例的列表

plt.legend(lines[:2], ['first', 'second']);

# 第二个方法
#plt.plot(x, y[:, 0], label='first')
#plt.plot(x, y[:, 1], label='second')
#plt.plot(x, y[:, 2:])
#plt.legend(framealpha=1, frameon=True);
```


![png](output_53_0.png)


### 将图例分不同的区域展示


```python
fig, ax = plt.subplots()

lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),styles[i], color='black')
ax.axis('equal')
```




    (-0.5, 10.5, -1.1, 1.1)




![png](output_55_1.png)



```python
# 设置第一组标签
ax.legend(lines[:2], ['line A', 'line B'],
          loc='upper right', frameon=False)

# 创建第二组标签
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg);
```

## 自定义色阶
### 展示色阶


```python
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

plt.imshow(I)
plt.colorbar();
```


![png](output_58_0.png)


### 改变配色为'gray'


```python
plt.imshow(I, cmap='gray');
```


![png](output_60_0.png)


### 将色阶分成6个离散值显示


```python
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1);
```


![png](output_62_0.png)


## 多子图
### 在一个1010的画布中，(0.65,0.65)的位置创建一个0.20.2的子图


```python
ax1 = plt.axes()
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])
```


![png](output_64_0.png)


### 在2个子图中，显示sin(x)和cos(x)的图像


```python
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x));
ax2.plot(np.cos(x));
```


![png](output_66_0.png)


### 用for创建6个子图，并且在图中标识出对应的子图坐标


```python
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),fontsize=18, ha='center')
    
# 方法二
# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     ax.text(0.5, 0.5, str((2, 3, i)),fontsize=18, ha='center')
```


![png](output_68_0.png)


### 设置相同行和列共享x,y轴


```python
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
```


![png](output_70_0.png)


### 用[]的方式取出每个子图，并添加子图座标文字


```python
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')
fig
```




![png](output_72_0.png)



### 组合绘制大小不同的子图，样式如下
```python
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2]);
```


![png](output_74_0.png)


### 显示一组二维数据的频度分布，并分别在x,y轴上，显示该维度的数据的频度分布


```python
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.scatter(x, y,s=3,alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal')
y_hist.invert_xaxis()
```


![png](output_76_0.png)


## 三维图像
### 创建一个三维画布


```python
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')
```


![png](output_78_0.png)


### 绘制一个三维螺旋线


```python
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline);
```


![png](output_80_0.png)


### 绘制一组三维点


```python
ax = plt.axes(projection='3d')
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
```


![png](output_82_0.png)


## 宝可梦数据集可视化
### 展示前5个宝可梦的Defense,Attack,HP的堆积条形图


```python
import pandas as pd
df = pd.read_csv('Pokemon.csv')
```


```python
pokemon = df['Name'][:5]
hp = df['HP'][:5]
attack = df['Attack'][:5]
defense = df['Defense'][:5]
ind = [x for x, _ in enumerate(pokemon)]

plt.figure(figsize=(10,10))
plt.bar(ind, defense, width=0.8, label='Defense', color='blue', bottom=attack+hp)
plt.bar(ind, attack, width=0.8, label='Attack', color='gold', bottom=hp)
plt.bar(ind, hp, width=0.8, label='Hp', color='red')

plt.xticks(ind, pokemon)
plt.ylabel("Value")
plt.xlabel("Pokemon")
plt.legend(loc="upper right")
plt.title("5 Pokemon Defense & Attack & Hp")
plt.show()
```


![png](output_85_0.png)


### 展示前5个宝可梦的Attack,HP的簇状条形图


```python
N = 5
pokemon_hp = df['HP'][:5]
pokemon_attack = df['Attack'][:5]

ind = np.arange(N)
width = 0.35       
plt.bar(ind, pokemon_hp, width, label='HP')
plt.bar(ind + width, pokemon_attack, width,label='Attack')

plt.ylabel('Values')
plt.title('Pokemon Hp & Attack')

plt.xticks(ind + width / 2, (df['Name'][:5]),rotation=45)
plt.legend(loc='best')
plt.show()
```


![png](output_87_0.png)


### 展示前5个宝可梦的Defense,Attack,HP的堆积图


```python
x = df['Name'][:4]
y1 = df['HP'][:4]
y2 = df['Attack'][:4]
y3 = df['Defense'][:4]

labels = ["HP ", "Attack", "Defense"]

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3)
ax.legend(loc='upper left', labels=labels)
plt.xticks(rotation=90)
plt.show()
```


![png](output_89_0.png)


### 公用x轴，展示前5个宝可梦的Defense,Attack,HP的折线图


```python
x = df['Name'][:5]
y1 = df['HP'][:5]
y2 = df['Attack'][:5]
y3 = df['Defense'][:5]

# Create two subplots sharing y axis
fig, (ax1, ax2,ax3) = plt.subplots(3, sharey=True)

ax1.plot(x, y1, 'ko-')
ax1.set(title='3 subplots', ylabel='HP')

ax2.plot(x, y2, 'r.-')
ax2.set(xlabel='Pokemon', ylabel='Attack')

ax3.plot(x, y3, ':')
ax3.set(xlabel='Pokemon', ylabel='Defense')

plt.show()
```


![png](output_91_0.png)


### 展示前15个宝可梦的Attack,HP的折线图


```python
plt.plot(df['HP'][:15], '-r',label='HP')
plt.plot(df['Attack'][:15], ':g',label='Attack')
plt.legend();
```


![png](output_93_0.png)


### 46.用scatter的x,y,c属性，展示所有宝可梦的Defense,Attack,HP数据


```python
x = df['Attack']
y = df['Defense']
colors = df['HP']

plt.scatter(x, y, c=colors, alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('HP')
plt.ylabel('Attack')
plt.colorbar();
```


![png](output_95_0.png)


### 展示所有宝可梦的攻击力的分布直方图，bins=10


```python
x = df['Attack']
num_bins = 10
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.title('Histogram')
plt.xlabel('Attack')
plt.ylabel('Value')
plt.show()
```


![png](output_97_0.png)


### 展示所有宝可梦Type 1的饼图


```python
plt.figure(1, figsize=(8,8))
df['Type 1'].value_counts().plot.pie(autopct="%1.1f%%")
plt.legend()
```




    <matplotlib.legend.Legend at 0x21e8f131c88>




![png](output_99_1.png)


### 展示所有宝可梦Type 1的柱状图


```python
ax = df['Type 1'].value_counts().plot.bar(figsize = (12,6),fontsize = 14)
ax.set_title("Pokemon Type 1 Count", fontsize = 20)
ax.set_xlabel("Pokemon Type 1", fontsize = 20)
ax.set_ylabel("Value", fontsize = 20)

plt.show()
```


![png](output_101_0.png)


### 展示综合评分最高的10只宝可梦的系数间的相关系数矩阵


```python
import seaborn as sns

top_10_pokemon=df.sort_values(by='Total',ascending=False).head(10)
corr=top_10_pokemon.corr()

fig, ax=plt.subplots(figsize=(10, 6))
sns.heatmap(corr,annot=True)
ax.set_ylim(9, 0)
plt.show()
```


![png](output_103_0.png)



```python

```
