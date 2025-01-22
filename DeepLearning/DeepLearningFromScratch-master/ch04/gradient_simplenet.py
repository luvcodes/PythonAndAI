# coding: utf-8
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

# 1. 定义simpleNet，里面只有两个方法，预测和损失函数计算
class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

# 2. x是输入数据，t是标签数据
x = np.array([0.6, 0.9])

net = simpleNet()
print("W矩阵: ", net.W, "\n")

# 3. x是一个1x2的矩阵，W是一个2x3的矩阵，所以预测的结果是一个1x3的矩阵
p = net.predict(x)
print("预测结果: ", p, "\n")

# 4. 计算预测结果的最大值的索引
print("最大值的索引: ", np.argmax(p), "\n")

# 5. 自己设置正确解标签t，基于这个标签计算损失函数
t = np.array([0, 0, 1])

# 6. 设置损失函数计算方法
def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print("梯度下降得到的2x3的矩阵: \n", dW)

# 求出神经网络的梯度后，接下来只需根据梯度法，更新权重参数即可。
