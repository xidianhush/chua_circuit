import numpy as np
from scipy.integrate import ode
from .chua_system import chua_system
from .parameters import get_parameters

def solve_chua_system(params=None):
    """
    求解Chua电路系统
    
    参数:
        params: dict, 可选，系统参数字典。如果为None，使用默认参数
        
    返回:
        t: array, 时间序列
        X: array, 状态变量的时间序列
    """
    # 如果没有提供参数，使用默认参数
    if params is None:
        params = get_parameters()
    
    # 创建时间序列
    t = np.arange(params['t_start'], params['t_end'], params['dt'])
    
    # 配置求解器
    solver = ode(chua_system)
    solver.set_integrator('vode',           # 使用vode求解器
                         method='bdf',      # 使用后向差分公式（适合刚性问题）
                         order=5,           # 使用5阶方法
                         nsteps=5000,       # 步数
                         rtol=1e-2,         # 相对误差容限
                         atol=1e-4)         # 绝对误差容限
    solver.set_f_params(params)
    solver.set_initial_value(params['init_conditions'], params['t_start'])
    
    # 数值求解
    solution = []
    while solver.successful() and solver.t < params['t_end']:
        try:
            solver.integrate(solver.t + params['dt'])
            if not np.all(np.isfinite(solver.y)):
                print(f"警告: 在t={solver.t}时检测到无效值")
                break
            solution.append([solver.t] + list(solver.y))
        except Exception as e:
            print(f"求解器错误: {e}")
            break
    
    # 转换为numpy数组
    solution = np.array(solution)
    t = solution[:,0]
    X = solution[:,1:]
    
    return t, X 