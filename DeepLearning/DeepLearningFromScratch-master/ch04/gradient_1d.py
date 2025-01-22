# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

def tangent_line(f, x):
    d = numerical_diff(f, x)
    y0 = f(x) - d*x
    return lambda t: d*t + y0

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)

# 分别计算两个切线
tf_5 = tangent_line(function_1, 5)
y2 = tf_5(x)

tf_10 = tangent_line(function_1, 10)
y3 = tf_10(x)

# 使用 subplots 创建两个子图
fig, axes = plt.subplots(1, 2, figsize=(10,4))

# 在第一个子图上绘制原函数及 x=5 处的切线
axes[0].plot(x, y, label="f(x)")
axes[0].plot(x, y2, label="tangent x=5")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].legend()
axes[0].set_title("Differentiation x=5")

# 在第二个子图上绘制原函数及 x=10 处的切线
axes[1].plot(x, y, label="f(x)")
axes[1].plot(x, y3, label="tangent x=10")
axes[1].set_xlabel("x")
axes[1].set_ylabel("f(x)")
axes[1].legend()
axes[1].set_title("Differentiation x=10")

plt.tight_layout()
plt.show()
