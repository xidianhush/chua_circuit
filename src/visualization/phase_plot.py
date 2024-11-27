import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

def plot_phase_portrait(X, title='Phase Portrait'):
    """静态相图绘制"""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(X[:,0], X[:,1], X[:,2])
    ax.set_xlabel('v1')
    ax.set_ylabel('v2')
    ax.set_zlabel('i3')
    ax.set_title(title)
    
    return fig, ax

def animate_phase_portrait(X, title='Animated Phase Portrait', interval=50):
    """
    创建动态相图
    
    参数:
        X: array, 形状为(n, 3)的数组，包含状态变量的时间序列
        title: str, 图的标题
        interval: int, 动画帧之间的间隔（毫秒）
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 设置图形范围
    ax.set_xlim([np.min(X[:,0]), np.max(X[:,0])])
    ax.set_ylim([np.min(X[:,1]), np.max(X[:,1])])
    ax.set_zlim([np.min(X[:,2]), np.max(X[:,2])])
    
    # 初始线条
    line, = ax.plot([], [], [], 'b-', lw=1)
    point, = ax.plot([], [], [], 'ro', markersize=8)
    
    # 设置标题和标签
    ax.set_xlabel('v1')
    ax.set_ylabel('v2')
    ax.set_zlabel('i3')
    ax.set_title(title)
    
    # 初始化函数
    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
        return line, point

    # 动画更新函数
    def update(frame):
        # 绘制轨迹
        line.set_data(X[:frame,0], X[:frame,1])
        line.set_3d_properties(X[:frame,2])
        
        # 绘制当前点
        point.set_data([X[frame,0]], [X[frame,1]])
        point.set_3d_properties([X[frame,2]])
        
        # 动态调整视角
        ax.view_init(30, frame/2)
        return line, point
    
    # 创建动画
    anim = FuncAnimation(fig, update, frames=len(X), 
                        init_func=init, interval=interval,
                        blit=True)
    
    return fig, anim

def plot_time_series(t, X, title='Time Series'):
    """时间序列图绘制"""
    fig, ax = plt.subplots(3, 1, figsize=(8, 10))
    
    variables = ['v1', 'v2', 'i3']
    for i in range(3):
        ax[i].plot(t, X[:,i])
        ax[i].set_xlabel('Time')
        ax[i].set_ylabel(variables[i])
        ax[i].grid(True)
    
    fig.suptitle(title)
    fig.tight_layout()
    
    return fig, ax

def animate_time_series(t, X, title='Animated Time Series', interval=50):
    """
    创建动态时间序列图
    
    参数:
        t: array, 时间序列
        X: array, 状态变量的时间序列
        title: str, 图的标题
        interval: int, 动画帧之间的间隔（毫秒）
    """
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle(title)
    
    lines = []
    points = []
    variables = ['v1', 'v2', 'i3']
    
    for i, ax in enumerate(axes):
        line, = ax.plot([], [], 'b-', lw=1)
        point, = ax.plot([], [], 'ro', markersize=8)
        ax.set_xlim(t[0], t[-1])
        ax.set_ylim(np.min(X[:,i])-0.1, np.max(X[:,i])+0.1)
        ax.set_xlabel('Time')
        ax.set_ylabel(variables[i])
        ax.grid(True)
        lines.append(line)
        points.append(point)
    
    def init():
        for line, point in zip(lines, points):
            line.set_data([], [])
            point.set_data([], [])
        return lines + points
    
    def update(frame):
        for i, (line, point) in enumerate(zip(lines, points)):
            line.set_data(t[:frame], X[:frame,i])
            point.set_data([t[frame]], [X[frame,i]])
        return lines + points
    
    anim = FuncAnimation(fig, update, frames=len(t),
                        init_func=init, interval=interval,
                        blit=True)
    
    fig.tight_layout()
    return fig, anim