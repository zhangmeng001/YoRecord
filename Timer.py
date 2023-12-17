
import sys
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QTime
from PyQt5.QtGui import QMouseEvent


class FloatTimer(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # 设置窗体的边框为无,且置顶窗体
        self.setWindowFlags(Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        # 窗体透明度
        self.setWindowOpacity(0.5)
        # 设置窗口置顶
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # 创建一个水平布局
        self.layout = QtWidgets.QHBoxLayout()

        # 创建计时器显示
        self.timer_label = QtWidgets.QLabel()
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)

        # 设置计时器显示的透明度
        # self.timer_label.setStyleSheet("background-color: rgba(0, 0, 0, 0.75);")

        # 设置计时器显示的字体颜色为红色
        self.timer_label.setStyleSheet("color: red;size:20px")
        self.timer_label.setText("00:00:00")

        # 创建计时器
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update_timer)

        # 添加计时器显示到容器
        self.layout.addWidget(self.timer_label)

        # 创建按钮
        self.button = QtWidgets.QPushButton("停止")
        self.button.setObjectName("stop_button")
        # self.button.clicked.connect(self.stop_timer)
        # self.button.clicked.connect(self.start_timer)

        # 添加按钮到窗口
        self.layout.addWidget(self.button)

        # 将容器设置为窗口的布局
        self.setLayout(self.layout)
        # self._start_time = time.time()  # 开始时间
        # 启动计时器,每隔 1000 毫秒（即 1 秒）触发一次
        # self.timer.start(1000)

        # # 获取主窗体句柄
        # self.parent = parent

    # threading
    # def timer2(self):
    #     while True:
    #         print(time.time())
    #         time.sleep(1)

    # #更新秒表
    # def update_timer(self):
    #     # now = time.time()
    #     # 更新计时器显示time.strftime("%H:%M:%S", time.localtime(now))
    #     run_time = time.time()-self._start_time
    #     run_time_str = self.convert(float(f"{run_time:0>8.2f}"))
    #     self.timer_label.setText(run_time_str)
    #
    # # 将时间表示为小时、分钟、秒的形式# 返回格式化字符串
    # def convert(self,raw_time):
    #     hour = int(raw_time // 3600)
    #     minute = int((raw_time % 3600) // 60)
    #     second = int(raw_time % 60)
    #     fmt = '{:0>2d}:{:0>2d}:{:0>2d}'
    #     return fmt.format(hour, minute, second)

    # 启动计时器
    # def start_timer(self,startTime):
    #     print('接收到的参数，%s'%startTime)
    #     if startTime:
    #         self._start_time = startTime
    #     else:
    #         self._start_time = time.time()
    #         # self._start_time = time.time()
    #     self.timer.start(1000)

    # def get_parent(self):
    #     # 获取主窗体句柄
    #     self.parent = parent

    # def stop_timer(self):
        # 停止计时器
        # self.timer.stop()
        # self.button.setText("开始")

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FloatTimer()
    window.show()
    app.exec_()
