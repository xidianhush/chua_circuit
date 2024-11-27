import numpy as np

def chua_system(state, t, params):
    """
    Chua电路的核心方程实现
    
    参数:
        state: array, 状态变量 [v1, v2, i3]
        t: float, 时间点
        params: dict, 系统参数
        
    返回:
        dXdt: array, 状态变量的导数
    """
    # 解包当前状态
    v1, v2, i3 = state    # 两个电压和一个电流
    
    # 获取参数
    alpha = params['alpha']
    beta = params['beta']
    gamma = params['gamma']
    m0 = params['m0']
    m1 = params['m1']
    
    # 计算非线性函数h(x)
    h = m1*v1 + 0.5*(m0-m1)*(abs(v1+1) - abs(v1-1))
    
    # Chua系统方程
    dv1_dt = alpha*(v2 - v1 - h)    # 某个步长时刻电容C1电压的变化率
    dv2_dt = v1 - v2 + i3           # 某个步长时刻电容C2电压的变化率
    di3_dt = -beta*v2 - gamma*i3    # 某个步长时刻电感L电流的变化率
    
    return [dv1_dt, dv2_dt, di3_dt] 