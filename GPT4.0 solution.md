首先导入所需库：
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
```

1. 使用`scipy.stats.norm`库中的`ppf`函数计算标准正态分布的分位数。

```python
a = [0.01, 0.025, 0.5, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 0.975, 0.995]
c = [round(stats.norm.ppf(i), 6) for i in a]
print("分位数：", c)
```

2. 生成随机数并绘制直方图和密度函数。
(a) 生成标准正态分布的随机数，并绘制直方图和密度函数。

```python
N = 10**6
np.random.seed(42)
x = np.random.randn(N)

plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, alpha=0.6, label="Histogram of $x_i$")
x_range = np.linspace(-5, 5, 1000)
plt.plot(x_range, stats.norm.pdf(x_range), 'r', label="Standard Normal PDF")
plt.legend()
plt.xlabel("$x$")
plt.ylabel("Density")
plt.title("Histogram and PDF of $x_i$")
plt.show()
```

直方图和标准正态分布密度函数非常接近，说明生成的随机数服从标准正态分布。

(b) 计算$y_i = x_i^2$，绘制直方图和χ²分布密度函数。

```python
y = x**2

plt.figure(figsize=(10, 6))
plt.hist(y, bins=100, density=True, alpha=0.6, label="Histogram of $y_i$")
y_range = np.linspace(0, 20, 1000)
plt.plot(y_range, stats.chi2.pdf(y_range, df=1), 'r', label="Chi-squared PDF (df=1)")
plt.legend()
plt.xlabel("$y$")
plt.ylabel("Density")
plt.title("Histogram and PDF of $y_i$")
plt.show()
```

直方图和卡方分布密度函数（自由度为1）非常接近，说明$y_i = x_i^2$服从卡方分布。