#这里用于构建各类小工具，对各类Python脚本进行封装
#包括针对性地说明，制作接口，制作独立的GUI界面等

from main import Tools
import os
from PyQt6.QtWidgets import (QPushButton, QWidget, QDialog, QVBoxLayout, QLabel, QDialogButtonBox, 
QGridLayout, QLineEdit, QFileDialog, QComboBox, QHBoxLayout, QColorDialog, QFontDialog)

from Modules import learn
from Modules import format_convert
from Modules import make_qrcode
from Modules import word_cloud
from Modules import img_cut

#这里制作一个列表，列表中将存储软件中所有能用到的工具
def Create_Tool_List():
    '''这一函数会创建并返回工具列表'''
    Tools_List = []
    Tools_List.append(Welcome_Init())
    Tools_List.append(THU_Learn_Init())
    Tools_List.append(Img_Cut_Init())
    Tools_List.append(Word_Cloud_Init())
    Tools_List.append(Quick_QR_Init())
    Tools_List.append(Csv_Convert_Init())
    Tools_List.append(Performance_Monitor_Init())
    Tools_List.append(Img_Mark_Init())

    return Tools_List

def Welcome_Init():
    '''这一函数用于创建起始介绍页面'''
    Welcome_Tool = Tools(Welcome)
    Welcome_Tool.title = '欢迎!'
    Welcome_Tool.description = '''
这里是Py实用工具盒！
我们在这个小软件当中整合了许多
有趣或有用的Python脚本，使用这些
可以便捷地实现很多有趣的功能。

想要了解各工具的详情，请在左侧选
项卡中选中对应的工具，也可以双击
选项卡快速执行对应的脚本。'''
    Welcome_Tool.parameters = []
    Welcome_Tool.source = '_01小组'
    Welcome_Tool.widget = QWidget()
    return Welcome_Tool

def THU_Learn_Init():
    '''这里对清华大学网络学堂爬虫脚本进行封装'''
    THU_Learn_Tool = Tools(THU_Learn)
    THU_Learn_Tool.title = '学堂自助'
    THU_Learn_Tool.description = '''
这是专为华大学开发的网络学堂自动下载脚本！
只需输入你的学号和info密码，轻轻点击，
即可实现课程信息/公告/课程文件的全自动下载

长期使用，更可使你的后台活跃程度在课程中一骑绝尘！
老师直呼：“太哈人了！”
（相关信息只需存入一次，此后即可直接运行）'''
    THU_Learn_Tool.parameters = []
    THU_Learn_Tool.source = 'https://github.com/Trinkle23897/learn2018-autodown'
    THU_Learn_Tool.widget = QWidget()
    Lay = QGridLayout()
    Account_In = QLineEdit()
    Account_In.setPlaceholderText('在这里输入学号……')
    Password_In = QLineEdit()
    Password_In.setPlaceholderText('这里要输入的是info密码……')
    Write_Password = QPushButton('保存信息...')
    Start_Download = QPushButton('开始下载!')

    def Write_In_Info():
        '''这一函数首先会清除掉.pass中的所有内容，然后将用户输入的各项信息写入其中'''
        with open('.pass', 'w') as f:
            f.write(Account_In.text() + '\n')
            f.write(Password_In.text())
        f.close()
        print('信息已保存！')

    Write_Password.clicked.connect(Write_In_Info)
    Start_Download.clicked.connect(THU_Learn_Tool.Run)
    Lay.addWidget(Account_In, 0, 0)
    Lay.addWidget(Password_In, 1, 0)
    Lay.addWidget(Write_Password, 0, 1)
    Lay.addWidget(Start_Download, 1, 1)
    THU_Learn_Tool.widget.setLayout(Lay)
    return THU_Learn_Tool

def Img_Cut_Init():
    '''这是由Yellow_GGG编写的图片裁剪工具'''
    Img_Cut_Tool = Tools(Img_Cut)
    Img_Cut_Tool.title = '图像分切'
    Img_Cut_Tool.description = '''
这是一个用于裁剪图片的小工具，
输入切分的大小（像素）后即可
选择图像并进行切分。
尤其适用于切割2D游戏素材哦！
'''
    Img_Cut_Tool.parameters = [0]
    Img_Cut_Tool.source = 'Yellow_GGG'
    Img_Cut_Tool.widget = QWidget()
    Lay = QVBoxLayout()

    Scale_Select = QLineEdit()
    Scale_Select.setPlaceholderText('切分尺度（像素）……')
    Scale_Select.textChanged.connect(lambda: Img_Cut_Tool.parameters.__setitem__(0, int(Scale_Select.text())))
    Button = QPushButton('选定分切')
    Button.clicked.connect(Img_Cut_Tool.Run)
    Lay.addWidget(Scale_Select)
    Lay.addWidget(Button)

    Img_Cut_Tool.widget.setLayout(Lay)
    return Img_Cut_Tool

def Word_Cloud_Init():
    '''这是由本小组成员开发的由本地文档快速生成词云的小工具'''
    NWC = Tools(Word_Cloud)
    NWC.title = '文档词云'
    NWC.description = '''
一个趣味小工具！
只需轻轻一点，选择字体后
即可快速选择读取docx文档
并以其中的关键词词频为基础
生成一幅精美的词云图！
一试便知～
（可编辑停用词库）
    '''
    NWC.parameters = ['']
    NWC.source = '_01小组'
    NWC.widget = QWidget()
    NWC.Layout = QVBoxLayout()
    NWC.Font_Select_Button = QPushButton('选择字体')
    NWC.Start_Button = QPushButton('开始!')

    def Font_Select():
        '''这一函数用于选择字体'''
        NWC.Font_Select_Dialog = QFontDialog()
        NWC.Font_Select_Dialog.setWindowTitle('选择字体')
        NWC.Font_Select_Dialog.exec()
        NWC.Font = NWC.Font_Select_Dialog.selectedFont().family()
        NWC.parameters[0] = NWC.Font

    NWC.Start_Button.clicked.connect(NWC.Run)
    NWC.Font_Select_Button.clicked.connect(Font_Select)
    NWC.Layout.addWidget(NWC.Font_Select_Button)
    NWC.Layout.addWidget(NWC.Start_Button)
    NWC.widget.setLayout(NWC.Layout)

    return NWC

def Quick_QR_Init():
    '''这是由本小组成员开发的二维码生成工具'''
    QR = Tools(Make_Qrcode)
    QR.title = '速速转码'
    QR.description = '''
这一个简单的小工具可以
将输入内容快速转换为二
维码！转换结果将以图片
格式输出到当前目录下
'''
    QR.parameters = ['']
    QR.source = '_01小组'
    QR.widget = QWidget()
    QR.Layout = QVBoxLayout()
    QR.Input = QLineEdit()
    QR.Input.setPlaceholderText('想要转换的内容是……')
    QR.Start_Button = QPushButton('开始转换')

    def Set_Content(txt):
        QR.parameters[0] = txt
        return

    QR.Input.textEdited.connect(Set_Content)
    QR.Start_Button.clicked.connect(QR.Run)
    QR.Layout.addWidget(QR.Input)
    QR.Layout.addWidget(QR.Start_Button)
    QR.widget.setLayout(QR.Layout)

    return QR

def Csv_Convert_Init():
    '''这是由本小组进行收集封装的文件格式转换工具'''
    CVC = Tools(Csv_Convert)
    CVC.title = '格式快转'
    CVC.description = '''
这个小工具可以方便地进行
许多不同文件格式之间的转换
选择模式并导入即可转换后文
件会存储在当前文件夹中哦
    '''
    CVC.parameters = ['', 0]
    CVC.source = '_01小组'
    CVC.widget = QWidget()
    CVC.Layout = QVBoxLayout()
    CVC.Mode = QComboBox()
    CVC.Mode.addItem('CSV转Excel')
    CVC.Mode.addItem('Excel转CSV')
    CVC.Mode.addItem('pdf转txt')
    CVC.Layout.addWidget(CVC.Mode)
    CVC.Start_Button = QPushButton('开始转换')
    CVC.Layout.addWidget(CVC.Start_Button)

    def Mode_Changed():
        '''这一函数用于改变转换模式'''
        if CVC.Mode.currentIndex() == 0:
            CVC.parameters[1] = 0
        elif CVC.Mode.currentIndex() == 1:
            CVC.parameters[1] = 1
        elif CVC.Mode.currentIndex() == 2:
            CVC.parameters[1] = 2
        return

    CVC.Start_Button.clicked.connect(CVC.Run)
    CVC.Mode.currentIndexChanged.connect(Mode_Changed)

    CVC.widget.setLayout(CVC.Layout)
    return CVC

def Img_Mark_Init():
    '''这是由本小组成员收集改编的图像标注工具'''
    IM = Tools(Img_Mark)
    IM.title = '快速水印'
    IM.description = '''
    本工具可在设定一系列参数后，方便快捷地向图片
    中添加水印。默认会将处理后的图片保存在本工具
    所在目录中的output文件夹下……
    当然，什么都不输入的话，也可以以默认值运行。
    '''
    IM.parameters = ['你啥也没输啊？','','','','','','','Hiragino Sans GB']
    IM.source = 'https://github.com/2Dou/watermarker'
    IM.widget = QWidget()
    IM.Mark_Label = QLineEdit()
    IM.Mark_Label.setPlaceholderText('在这里输入需要添加的文字')
    IM.Font_Size = QLineEdit()
    IM.Font_Size.setPlaceholderText('字体大小')
    IM.Font_Space = QLineEdit()
    IM.Font_Space.setPlaceholderText('字间距')
    IM.Font_Angle = QLineEdit()
    IM.Font_Angle.setPlaceholderText('旋转角度')
    IM.Opacity = QLineEdit()
    IM.Opacity.setPlaceholderText('透明度')
    IM.Quality = QLineEdit()
    IM.Quality.setPlaceholderText('质量1-100')
    IM.Color_Select_Button = QPushButton('选择颜色')
    IM.Font_Select_Button = QPushButton('选择字体')
    IM.Output_Button = QPushButton('选择图片并输出')
    IM.Layout = QGridLayout()
    IM.Layout.addWidget(IM.Mark_Label, 0, 0, 1, 2)
    IM.Layout.addWidget(IM.Font_Select_Button, 1, 2)
    IM.Layout.addWidget(IM.Font_Size, 1, 0)
    IM.Layout.addWidget(IM.Font_Space, 1, 1)
    IM.Layout.addWidget(IM.Font_Angle, 0, 2)
    IM.Layout.addWidget(IM.Opacity, 2, 0)
    IM.Layout.addWidget(IM.Quality, 2, 1)
    IM.Layout.addWidget(IM.Color_Select_Button, 2, 2)
    IM.Layout.addWidget(IM.Output_Button, 3, 0, 1, 3)
    IM.widget.setLayout(IM.Layout)

    def Set_Parameter_0(str):
        IM.parameters[0] = str
        return
    def Set_Parameter_1(str):
        IM.parameters[1] = str
        return
    def Set_Parameter_2(str):
        IM.parameters[2] = str
        return
    def Set_Parameter_3(str):
        IM.parameters[3] = str
        return
    def Set_Parameter_4(str):
        IM.parameters[4] = str
        return
    def Set_Parameter_5(str):
        IM.parameters[5] = str
        return

    IM.Mark_Label.textEdited.connect(Set_Parameter_0)
    IM.Font_Size.textEdited.connect(Set_Parameter_1)
    IM.Font_Space.textEdited.connect(Set_Parameter_2)
    IM.Font_Angle.textEdited.connect(Set_Parameter_3)
    IM.Opacity.textEdited.connect(Set_Parameter_4)
    IM.Quality.textEdited.connect(Set_Parameter_5)

    def Choose_Color():
        '''这一函数用于选择颜色'''
        ui = QColorDialog()
        IM.parameters[6] = ui.getColor().name()
    def Choose_Font():
        '''这一函数用于选择字体'''
        ui = QFontDialog()
        IM.parameters[7] = ui.getFont()[0].family()

    IM.Color_Select_Button.clicked.connect(Choose_Color)
    IM.Font_Select_Button.clicked.connect(Choose_Font)
    IM.Output_Button.clicked.connect(IM.Run)
    return IM

def Performance_Monitor_Init():
    '''这是由本小组成员收集改编的性能监控工具'''
    PM = Tools(Performance_Monitor)
    PM.title = '性能监控'
    PM.description = '''
！本工具(Asitop)仅适用于搭载M系芯片的Mac产品！

初次使用需要首先安装。
这一工具可实时监测性能使用情况及功耗数据。
本工具需要管理员权限，因此需要输入密码以启用。
（管理员密码在输入时不会显示）
    '''
    PM.parameters = []
    PM.source = 'https://github.com/tlkh/asitop'
    PM.widget = QWidget()
    PM.Install_Button = QPushButton('安装')
    PM.Start_Button = QPushButton('开始')

    def Install():
        '''这一函数用于安装asitop'''
        os.system('pip install asitop')
        return

    PM.Install_Button.clicked.connect(Install)
    PM.Start_Button.clicked.connect(PM.Run)
    PM.Layout = QHBoxLayout()
    PM.Layout.addWidget(PM.Install_Button)
    PM.Layout.addWidget(PM.Start_Button)
    PM.widget.setLayout(PM.Layout)

    return PM

def Img_Cut(Parameters = []):
    '''这一工具用于快速裁切图片'''
    ui = QFileDialog()
    Path = ui.getOpenFileUrl()[0].path()
    img_cut.main(Path, Parameters[0])

def Performance_Monitor(Parameters = []):
    '''这一脚本可以快速调用Mac上的实用性能监视工具，需要输入管理员密码以使用'''
    os.system('sudo asitop')

def Img_Mark(Parameters = []):
    '''这一脚本用于给图片快捷添加水印，参数可调'''
    ui = QFileDialog()
    Path = ui.getOpenFileUrl()[0].path()
    command = "python3 marker.py -f " + Path
    for i in range(0, 8):
        if Parameters[i] != '':
            if i == 1:
                command += " --size " + Parameters[1]
            elif i == 2:
                command += " -s " + Parameters[2]
            elif i == 3:
                command += " -a " + Parameters[3]
            elif i == 4:
                command += " --opacity " + Parameters[4]
            elif i == 5:
                command += " --quality " + Parameters[5]
            elif i == 6:
                command += " -c" + Parameters[6]
            elif i == 7:
                command += " --font-family " + Parameters[7].replace(' ', '\ ')
            elif i == 0:
                command += " -m " + Parameters[0]

    os.system(command)

def Csv_Convert(Parameters = []):
    '''用于进行csv与xlsx两种文件格式的快速转换'''
    ui = QFileDialog()
    Path = ui.getOpenFileUrl()[0].path()
    Parameters[0] = Path
    format_convert.main(Parameters[0], Parameters[1])

def Make_Qrcode(Parameters = []):
    '''这一脚本用于将链接快速转换为二维码'''
    make_qrcode.main(Parameters[0])

def THU_Learn(Parameters = []):
    '''这是由GitHub上@Trinkle23897大神开发的清华大学网络学堂爬虫脚本'''
    learn.main(learn.get_args())

def Word_Cloud(Parameters = []):
    '''这是由本组成员开发的快速词云小工具'''
    ui = QFileDialog()
    Path = ui.getOpenFileUrl()[0].path()
    if Parameters[0] == '':
        word_cloud.main(Path)
    else:
        word_cloud.main(Path, Parameters[0])

def Welcome(parameters = []):
    '''你在期待些什么呢？'''
    class weldialog(QDialog):
        def __init__(self):
            super().__init__()
            self.label = QLabel('不行啦，这个怎么想都运行不了的啦！')
            self.butt = QDialogButtonBox.StandardButton.Ok
            self.buttbx = QDialogButtonBox(self.butt)
            self.buttbx.accepted.connect(self.accept)
            self.setWindowTitle('Σ（ﾟдﾟlll）')
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.buttbx)
            self.setLayout(self.layout)
            self.show()
        def accept(self):
            self.close()
    ui = weldialog()
    ui.exec()