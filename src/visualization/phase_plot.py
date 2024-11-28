import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_phase_portrait(X, title='Phase Portrait', ax=None):
    """
    静态相图绘制
    
    参数:
        X: array, 形状为(n, 3)的数组，包含状态变量的时间序列
        title: str, 图的标题
        ax: matplotlib轴对象，如果为None则创建新的图形
    """
    if ax is None:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
    else:
        fig = ax.figure
        
    ax.plot(X[:,0], X[:,1], X[:,2], 'b-', linewidth=0.5)
    ax.set_xlabel('v1')
    ax.set_ylabel('v2')
    ax.set_zlabel('i3')
    ax.set_title(title)
    ax.view_init(elev=30, azim=45)
    ax.grid(True)
    
    return fig, ax

def plot_time_series(t, X, title='Time Series', ax=None, component=0, color='b'):
    """
    时间序列图绘制
    
    参数:
        t: array, 时间序列
        X: array, 状态变量的时间序列
        title: str, 图的标题
        ax: matplotlib轴对象，如果为None则创建新的图形
        component: int, 要绘制的分量（0=v1, 1=v2, 2=i3）
        color: str, 线条颜色
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    else:
        fig = ax.figure
        
    variables = ['v1', 'v2', 'i3']
    ax.plot(t, X[:,component], color=color, linewidth=0.8)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel(variables[component])
    ax.set_title(title)
    ax.grid(True)
    
    return fig, ax