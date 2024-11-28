import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                           QVBoxLayout, QSlider, QLabel, QGridLayout)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import os
import sys

# 添加源代码路径
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from src.simulation.solver import solve_chua_system
from src.simulation.parameters import get_parameters
from src.visualization.phase_plot import plot_phase_portrait, plot_time_series

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
        param_ranges = {
            'alpha': (5, 20, 'Alpha'),       # 修改alpha的范围为5-20
            'beta': (20, 35, 'Beta'),        # C2/(L*G^2)
            'gamma': (0, 1, 'Gamma')         # r0/(L*G)
        }
        
        for param, (min_val, max_val, label) in param_ranges.items():
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(1000)
            initial_value = int((self.params[param] - min_val) * 1000 / (max_val - min_val))
            slider.setValue(initial_value)
            
            # 使用浮点数显示参数值
            value_label = QLabel(f'{label}: {self.params[param]:.2f}')
            control_layout.addWidget(value_label)
            control_layout.addWidget(slider)
            
            self.sliders[param] = {
                'slider': slider,
                'label': value_label,
                'range': (min_val, max_val)
            }
            slider.valueChanged.connect(self.update_plot)
        
        layout.addWidget(control_widget, 1, 0, 1, 2)
        
        # 初始绘图
        self.update_plot()
    
    def update_plot(self):
        # 更新参数
        for param, items in self.sliders.items():
            slider = items['slider']
            label = items['label']
            min_val, max_val = items['range']
            
            value = min_val + (slider.value() * (max_val - min_val) / 1000)
            self.params[param] = value
            label.setText(f'{param}: {value:.2f}')
        
        # 运行仿真（使用solver模块）
        t, X = solve_chua_system(self.params)
        
        # 清除原图
        self.fig.clear()
        
        # 创建网格布局 2x2
        # 左上角放相图，右边放三个时间序列图
        ax1 = self.fig.add_subplot(221, projection='3d')
        plot_phase_portrait(X, ax=ax1)
        
        # 添加三个时间序列图
        ax2 = self.fig.add_subplot(222)  # v1
        ax3 = self.fig.add_subplot(224)  # v2
        ax4 = self.fig.add_subplot(223)  # i3
        
        # 绘制时间序列
        ax2.plot(t, X[:,0], 'b-', linewidth=0.8)
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('v1')
        ax2.grid(True)
        
        ax3.plot(t, X[:,1], 'r-', linewidth=0.8)
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('v2')
        ax3.grid(True)
        
        ax4.plot(t, X[:,2], 'g-', linewidth=0.8)
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('i3')
        ax4.grid(True)
        
        self.fig.tight_layout()
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    gui = ChuaGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 