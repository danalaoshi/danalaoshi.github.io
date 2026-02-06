---
layout: default
title: Matplotlib简介
parent: Matplotlib
nav_order: 1
---

# Matplotlib绘图简介

- 建立在Numpy数组基础上的多平台数据可视化库
- 最初设计用来完善SciPy生态
- 良好的操作系统兼容性和图形显示底层接口兼容性
- 功能强大，设置灵活


## 图形样式

利用Matplotlib绘图的图形风格可以设定，所有图形，可以通过`plt.style.use('classic')`
设置图形样式，在1.5版本以前只能使用经典风格，新版本会有不同的风格设置。

## 不同环境的使用

不同环境中使用Matplotlib可能稍有不同，需要注意:

### 脚本中使用

在脚本中使用，并不能自动显示图形，需要使用`plt.show()`明确让Matplotlib把图形显示出来，否则不会看到图形。

### IPython shell

在IPython shell中使用画图，需要使用魔法命令`%matplotlib`, 在以后的画图命令中，会自动显示出需要画的图形。

### Jupyter Notebook

在Jupyter Notebook中一般也需要使用魔法函数，但是相应魔法函数有两个：
- `%matplotlib inline`: 在Notebook中启动静态图形
- `%matplotlib notebook`：在Notebook中启动交互式图形

使用以上两个魔法函数，理论上不需要在使用show函数强制显示图形，但在实践过程中，可能出现不显示的情况，此时建议使用
show显示图像。



## 图像的保存

经常需要保存产生的图像以备使用，
如果使用的是交互式显示图形，可以直接点击保存按钮来保存图形，在所有代码中，都可以使用savefig函数来保存函数。


## 两种不同的画图接口

Matplotlib支持两类画图接口：
- MATLAB风格接口：此类接口的特点是有状态的(Stateful），使用方便，对MATLAB用户友好，此类接口在pyplot中
- 面向对象接口：面向对象方式，处理复杂图形比较方便，能力相对比较强

此两种风格接口比较相似，容易混淆，我们在使用中，经常会混用。

