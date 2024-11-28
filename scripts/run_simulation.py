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
    fig = plt.figure(figsize=(12, 6))
    
    # 创建子图
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)
    
    # 绘制相图
    ax1.plot(X[:,0], X[:,1], X[:,2], 'b-', linewidth=0.5)
    ax1.set_xlabel('v1')
    ax1.set_ylabel('v2')
    ax1.set_zlabel('i3')
    ax1.set_title('Phase Portrait')
    ax1.view_init(elev=30, azim=45)
    ax1.grid(True)
    
    # 绘制时间序列
    ax2.plot(t, X[:,0], 'b-', linewidth=0.8)  # 使用秒为单位
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('v1')
    ax2.set_title('Time Series of v1')
    ax2.grid(True)
    
    # 调整布局
    fig.tight_layout()
    
    # 创建结果目录（如果不存在）
    results_dir = os.path.join(project_root, 'results', 'figures')
    os.makedirs(results_dir, exist_ok=True)
    
    # 保存结果
    fig.savefig(os.path.join(results_dir, 'simulation_results.png'), dpi=300, bbox_inches='tight')
    
    # 显示图形
    plt.show()

if __name__ == '__main__':
    run_simulation() 