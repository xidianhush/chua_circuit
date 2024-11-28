def get_parameters():
    """返回Chua电路系统参数"""
    params = {
        # 系统参数
        'alpha': 15.6,    # alpha = C2/C1
        'beta': 28.58,    # beta = C2/(L*G^2)
        'gamma': 0,       # gamma = r0/(L*G)
        
        # Chua二极管参数
        'm0': -1.143,
        'm1': -0.714,

        # 仿真设置
        't_start': 0,     # 起始时间（秒）
        't_end': 50,      # 结束时间（50秒）
        'dt': 0.05,       # 时间步长（0.05秒）
        'init_conditions': [0.1, 0, 0]
    }
    
    return params 