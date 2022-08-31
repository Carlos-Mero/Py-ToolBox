#这是一个由2022年《信息科学理论与实践》课程第01小组合作开发的程序
#这个程序最早是作为期末小组作业编写的
#各位可以随意使用或转载、修改。
__license__ = "MIT"

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
QHBoxLayout, QVBoxLayout, QWidget, QListWidget, QListWidgetItem)
import sys
import os.path

Dir_Path = os.path.abspath('output')
#以上是导入包内容并设定路径

import tools
#以上是导入用户内容

#这里首先新建一个类用于存储所需的各种常数
class Const():
    '''程序中所使用的常数均可在这里查询或统一修改'''
    Version = '0.1.0'
    Project_Name = 'Py实用工具盒'
    #以下是格式信息，请至style.qss中修改
    #Card_Hlen = '110px'
    #Card_Vlen = '50px'

class Tools():
    '''这里将各类Python脚本封装成“工具”使用。其各项属性都需要单独进行设置'''
    def __init__(self, script):
        self.script = script #这是执行该工具的脚本
        self.title = '' #工具名称
        self.description = '' #对该工具的描述
        self.parameters = [] #工具的参数列表
        self.card = QWidget() #这是工具所对应的选项卡
        self.widget = None #工具的图形化控制界面
        self.source = '' #该工具的来源
    
    def Run(self):
        '''这一函数用于运行该工具'''
        self.script(self.parameters)

#使用类方法构建主要窗口
class MainWindow(QMainWindow):
    '''这里对主要窗口进行设定布局'''
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(Const.Project_Name)
        self.Tool_List = tools.Create_Tool_List() #这是工具列表
        self.Layout = QHBoxLayout() #这是主窗口的排版方式
        Card_Menu = QListWidget() #这是左侧选项卡的界面
        Card_Menu.setFixedWidth(113) #设定Card——Menu的宽度为113px

        #这里为每一个工具构建出其图形界面
        for tool in self.Tool_List:
            item = QListWidgetItem(tool.title)
            Card_Menu.addItem(item)
            tool_layout = QVBoxLayout()
            Tl = QLabel(tool.title)
            Tl.setStyleSheet('''
                font-size: 23px;
            ''')
            Content = QLabel(tool.description)
            Content.setStyleSheet('''
                font-size: 14px;
            ''')
            source = QLabel('出自：' + tool.source)
            source.setStyleSheet('''
                font-size: 9px;
            ''')
            tool_layout.addWidget(Tl)
            tool_layout.addWidget(Content)
            tool_layout.addWidget(tool.widget)
            tool_layout.addWidget(source)
            tool.card.setLayout(tool_layout)


        self.Layout.addWidget(Card_Menu)#将左侧选项卡添加到排版中
        self.window = QWidget() #这是主窗口
        self.window.setLayout(self.Layout) #将排版添加到主窗口中

        Card_Menu.itemClicked.connect(self.show_detail) #连接左侧选项卡的点击事件
        Card_Menu.itemDoubleClicked.connect(self.quick_run_tool) #连接左侧选项卡的双击事件

        #默认选中Card_Menu的第一个选项卡
        Card_Menu.item(0).setSelected(True)
        self.Layout.addWidget(self.Tool_List[0].card) #将第一个工具的选项卡添加到排版中

        self.setCentralWidget(self.window) #将主窗口添加到对象中

    def show_detail(self, item):
        '''点击左侧选项卡将会调用这一方法，用于显示工具的详细信息'''
        for tool in self.Tool_List:
            if tool.title == item.text():
                self.Layout.itemAt(1).widget().setParent(None) #将原有的工具选项卡移除
                self.Layout.addWidget(tool.card) #将该工具的选项卡添加到排版中
                break
        QApplication.processEvents() #刷新窗口
        self.adjustSize() #调整窗口大小
        return

    def quick_run_tool(self, item):
        '''双击左侧选项卡将会调用这一方法，用于快速运行工具'''
        for tool in self.Tool_List:
            if tool.title == item.text():
                tool.Run()
                break
        return

#定义主函数
def main():
    app = QApplication(sys.argv)
    Tool_Box = MainWindow()
    Tool_Box.show()

    #这里通过style.qss文件对窗口样式进行调整美化
    with open("style.qss") as f:
        app.setStyleSheet(f.read())

    sys.exit(app.exec())

if __name__ == '__main__':
    main()