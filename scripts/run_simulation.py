import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 - 需要用于3D图形
import os
import sys

# 添加源代码路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.simulation.solver import solve_chua_system
from src.visualization.phase_plot import plot_phase_portrait, plot_time_series

def run_simulation():
    """
    运行Chua电路仿真的主函数
    """
    # 求解系统
    t, X = solve_chua_system()
    
    # 创建并显示相图
    fig1, ax1 = plot_phase_portrait(X, title='Chua Circuit Phase Portrait')
    
    # 创建并显示时间序列图
    fig2, ax2 = plot_time_series(t, X, title='Chua Circuit Time Series')
    
    # 创建结果目录（如果不存在）
    results_dir = os.path.join(project_root, 'results', 'figures')
    os.makedirs(results_dir, exist_ok=True)
    
    # 保存结果
    fig1.savefig(os.path.join(results_dir, 'phase_portrait.png'), dpi=300, bbox_inches='tight')
    fig2.savefig(os.path.join(results_dir, 'time_series.png'), dpi=300, bbox_inches='tight')
    
    # 显示图形
    plt.show()

if __name__ == '__main__':
    run_simulation() 