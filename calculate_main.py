import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculate import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.Num = 0  # 设置当前数字为0
        self.num_list = []  # 设置一个列表存放往期数字
        self.action_list = [] # 存放操作

    def clickNum(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        btn = int(self.sender().text())  # 获取信号发送者的名字
        self.Num = self.Num * 10 + btn  # 将新输入的数字插入到Num的最后面
        self.lcdNumber.display(self.Num)  # 将数字显示到上面

    def clickAdd(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list.append(self.Num)  # 将数字缓存到列表里
        self.Num = 0  # 清空Num准备接受下一个数字
        self.lcdNumber.display(0)  # 显示0
        self.action_list.append(1)

    def clickMinus(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list.append(self.Num)  # 将数字缓存到列表里
        self.Num = 0  # 清空Num准备接受下一个数字
        self.lcdNumber.display(0)  # 显示0
        self.action_list.append(2)

    def clickMul(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list.append(self.Num)  # 将数字缓存到列表里
        self.Num = 0  # 清空Num准备接受下一个数字
        self.lcdNumber.display(0)  # 显示0
        self.action_list.append(3)

    def clickDiv(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list.append(self.Num)  # 将数字缓存到列表里
        self.Num = 0  # 清空Num准备接受下一个数字
        self.lcdNumber.display(0)  # 显示0
        self.action_list.append(4)

    def clickEqu(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list.append(self.Num)  # 将数字缓存到列表里
        if (len(self.action_list)>0):
            action = self.action_list.pop() # 获取最后一个操作
            if action == 1:
                if len(self.num_list)>=2:
                    self.lcdNumber.display(self.num_list[-2]+self.num_list[-1])  # 加
                    self.Num = self.num_list[-2]+self.num_list[-1]
                else:
                    self.lcdNumber.display(0 + self.num_list[-1])  # 加（考虑第一个输入是符号的情况，默认为0+输入值）
                    self.Num = 0 + self.num_list[-1]
            elif action ==2:
                if len(self.num_list) >= 2:
                    self.lcdNumber.display(self.num_list[-2]-self.num_list[-1])  # 减
                    self.Num = self.num_list[-2] - self.num_list[-1]
                else:
                    self.lcdNumber.display(0 - self.num_list[-1])  # 减（考虑第一个输入是符号的情况，默认为0-输入值）
                    self.Num =0 - self.num_list[-1]
            elif action ==3:
                if len(self.num_list)>=2:
                    self.lcdNumber.display(self.num_list[-2]*self.num_list[-1])  # 乘
                    self.Num = self.num_list[-2] * self.num_list[-1]
                else:
                    self.lcdNumber.display(0)  # 乘（考虑第一个输入是符号的情况，默认为0*输入值）
                    self.Num = 0
            else:
                if self.num_list[-1]==0:
                    self.lcdNumber.display(0) # 被除数为0，发生错误
                    self.Num = 0
                else:
                    if len(self.num_list)>=2:
                        self.lcdNumber.display(self.num_list[-2]/self.num_list[-1])  # 除
                        self.Num = self.num_list[-2] / self.num_list[-1]
                    else:
                        self.lcdNumber.display(0)  # 除（考虑第一个输入是符号的情况，默认为0/输入值）
                        self.Num = 0
            self.action_list = []  # 清空操作
            self.num_list = []
        else:
            self.lcdNumber.display(self.num)

    def clickClear(self):
        # self.Num = self.lcdNumber.value() #将显示的数字放到Num里
        self.num_list = [] # 清空列表
        self.Num = 0 # 清空Num缓存
        self.lcdNumber.display(0)  # 显示0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())