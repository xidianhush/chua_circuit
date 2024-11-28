import numpy as np

def chua_system(t, state, params):
    """
    Chua电路系统方程
    
    参数:
        t: float, 时间点（秒）
        state: array-like, 状态变量 [v1, v2, i3]
        params: dict, 系统参数
        
    返回:
        array, 状态变量的导数 [dv1/dt, dv2/dt, di3/dt]
    """
    # 确保state是numpy数组
    state = np.asarray(state)
    
    # 获取状态变量
    v1, v2, i3 = state[0], state[1], state[2]
    
    # 获取系统参数
    alpha = params['alpha']
    beta = params['beta']
    gamma = params['gamma']
    m0 = params['m0']
    m1 = params['m1']
    
    # 计算Chua二极管的非线性特性
    h = m1*v1 + 0.5*(m0-m1)*(abs(v1+1) - abs(v1-1))
    
    # Chua系统方程
    dv1_dt = alpha*(v2 - v1 - h)    # v1的变化率
    dv2_dt = v1 - v2 + i3           # v2的变化率
    di3_dt = -beta*v2 - gamma*i3    # i3的变化率
    
    return np.array([dv1_dt, dv2_dt, di3_dt]) 