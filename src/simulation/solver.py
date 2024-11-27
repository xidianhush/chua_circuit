import numpy as np
from scipy.integrate import ode
from .chua_system import chua_system
from .parameters import get_parameters

def solve_chua_system():
    """
    求解Chua电路系统
    
    返回:
        t: array, 时间序列
        X: array, 状态变量的时间序列
    """
    # 获取参数
    params = get_parameters()
    
    # 创建时间序列
    t = np.arange(params['t_start'], params['t_end'], params['dt'])
    
    # 配置求解器
    solver = ode(chua_system)
    solver.set_integrator('dopri5')  # 使用Runge-Kutta (4,5)方法
    solver.set_f_params(params)
    solver.set_initial_value(params['init_conditions'], params['t_start'])
    
    # 数值求解
    solution = []
    while solver.successful() and solver.t < params['t_end']:
        solver.integrate(solver.t + params['dt'])
        solution.append([solver.t] + list(solver.y))
    
    # 转换为numpy数组
    solution = np.array(solution)
    t = solution[:,0]
    X = solution[:,1:]
    
    return t, X 