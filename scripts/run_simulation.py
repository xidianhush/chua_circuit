import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 - 需要用于3D图形
import os
import sys

# 添加源代码路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.simulation.solver import solve_chua_system

def run_simulation():
    """
    运行Chua电路仿真的主函数
    """
    # 求解系统
    t, X = solve_chua_system()
    
    # 创建图形
    fig = plt.figure(figsize=(12, 8))
    
    # 绘制相图
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot(X[:,0], X[:,1], X[:,2])
    ax1.set_xlabel('v1')
    ax1.set_ylabel('v2')
    ax1.set_zlabel('i3')
    ax1.set_title('Phase Portrait')
    
    # 绘制时间序列
    ax2 = fig.add_subplot(122)
    ax2.plot(t, X[:,0])
    ax2.set_xlabel('Time')
    ax2.set_ylabel('v1')
    ax2.set_title('Time Series of v1')
    
    # 创建结果目录（如果不存在）
    results_dir = os.path.join(project_root, 'results', 'figures')
    os.makedirs(results_dir, exist_ok=True)
    
    # 保存结果
    plt.savefig(os.path.join(results_dir, 'simulation_results.png'))
    plt.show()

if __name__ == '__main__':
    run_simulation() 