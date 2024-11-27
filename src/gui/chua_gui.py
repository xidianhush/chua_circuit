import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                           QVBoxLayout, QSlider, QLabel, QGridLayout)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.integrate import ode
import sys
import os

# 添加源代码路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from simulation.chua_system import chua_system
from simulation.parameters import get_parameters

class ChuaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chua Circuit Simulation')
        self.setGeometry(100, 100, 1200, 800)
        
        # 获取默认参数
        self.params = get_parameters()
        
        # 创建主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QGridLayout(main_widget)
        
        # 创建图形
        self.fig = Figure(figsize=(12, 6))
        self.canvas = FigureCanvasQTAgg(self.fig)
        layout.addWidget(self.canvas, 0, 0, 1, 2)
        
        # 创建参数控制面板
        control_widget = QWidget()
        control_layout = QVBoxLayout(control_widget)
        
        # 添加参数滑块
        self.sliders = {}
        for param in ['alpha', 'beta', 'gamma']:
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(500)
            slider.setValue(int(self.params[param] * 10))
            slider.valueChanged.connect(self.update_plot)
            
            label = QLabel(f'{param}: {self.params[param]}')
            control_layout.addWidget(label)
            control_layout.addWidget(slider)
            self.sliders[param] = (slider, label)
        
        layout.addWidget(control_widget, 1, 0, 1, 2)
        
        # 初始绘图
        self.update_plot()
    
    def update_plot(self):
        # 更新参数
        for param, (slider, label) in self.sliders.items():
            self.params[param] = slider.value() / 10
            label.setText(f'{param}: {self.params[param]}')
        
        # 运行仿真
        t, X = self.run_simulation()
        
        # 清除原图
        self.fig.clear()
        
        # 绘制相图
        ax1 = self.fig.add_subplot(121, projection='3d')
        ax1.plot(X[:,0], X[:,1], X[:,2])
        ax1.set_xlabel('v1')
        ax1.set_ylabel('v2')
        ax1.set_zlabel('i3')
        ax1.set_title('Phase Portrait')
        
        # 绘制时间序列
        ax2 = self.fig.add_subplot(122)
        ax2.plot(t, X[:,0])
        ax2.set_xlabel('Time')
        ax2.set_ylabel('v1')
        ax2.set_title('Time Series of v1')
        
        self.canvas.draw()
    
    def run_simulation(self):
        # 创建时间序列
        t = np.arange(self.params['t_start'], self.params['t_end'], self.params['dt'])
        
        # 配置求解器
        solver = ode(chua_system)
        solver.set_integrator('dopri5')
        solver.set_f_params(self.params)
        solver.set_initial_value(self.params['init_conditions'], self.params['t_start'])
        
        # 数值求解
        solution = []
        while solver.successful() and solver.t < self.params['t_end']:
            solver.integrate(solver.t + self.params['dt'])
            solution.append([solver.t] + list(solver.y))
        
        solution = np.array(solution)
        return solution[:,0], solution[:,1:]

def main():
    app = QApplication(sys.argv)
    gui = ChuaGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 