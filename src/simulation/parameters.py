def get_parameters():
    """返回默认参数配置"""
    params = {
        # 电路参数
        'alpha': 15.6,
        'beta': 28.58,
        'gamma': 0,
        'm0': -1.143,
        'm1': -0.714,
        
        # 仿真设置
        't_start': 0,
        't_end': 100,
        'dt': 0.01,
        'init_conditions': [0.7, 0, 0]
    }
    return params 