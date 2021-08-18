import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import hashlib
import os


class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("Project_Merge")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('700x400+10+10')

        #标签
        # self.init_data_label = Label(self.init_window_name, text='平台目录：', )
        # self.init_data_label.grid(row=0, column=0)
        self.init_data_label = Label(self.init_window_name, text='本地目录：', )
        self.init_data_label.grid(row=1, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag1：', )
        self.init_data_label.grid(row=2, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag2：', )
        self.init_data_label.grid(row=3, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag3：', )
        self.init_data_label.grid(row=4, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag4：', )
        self.init_data_label.grid(row=5, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag5：', )
        self.init_data_label.grid(row=6, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag6：', )
        self.init_data_label.grid(row=7, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag7：', )
        self.init_data_label.grid(row=8, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag8：', )
        self.init_data_label.grid(row=9, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag9：', )
        self.init_data_label.grid(row=10, column=0)
        self.init_data_label = Label(self.init_window_name, text='tag10：', )
        self.init_data_label.grid(row=11, column=0)

        #文本框
        # self.Edit_PrjName = Text(self.init_window_name, width=60, height=1)
        # self.Edit_PrjName.grid(row=0, column=1, rowspan=1, columnspan=7)
        self.Edit_localpath = Text(self.init_window_name, width=60, height=1)
        self.Edit_localpath.grid(row=1, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath1 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath1.grid(row=2, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath2 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath2.grid(row=3, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath3 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath3.grid(row=4, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath4 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath4.grid(row=5, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath5 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath5.grid(row=6, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath6 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath6.grid(row=7, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath7 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath7.grid(row=8, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath8 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath8.grid(row=9, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath9 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath9.grid(row=10, column=1, rowspan=1, columnspan=7)
        self.Edit_tagpath10 = Text(self.init_window_name, width=60, height=1)
        self.Edit_tagpath10.grid(row=11, column=1, rowspan=1, columnspan=7)

        #按钮
        # self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.localFolderSelect)  # 调用内部方法  加()为直接调用
        # self.btn_browser.grid(row=0, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.localFolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=1, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag1FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=2, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag2FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=3, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag3FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=4, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag4FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=5, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag5FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=6, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag6FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=7, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag7FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=8, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag8FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=9, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag9FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=10, column=9)
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.tag10FolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=11, column=9)

        self.btn_OK = Button(self.init_window_name, text="合并", bg="lightblue", width=5, command=self.merge)  # 调用内部方法  加()为直接调用
        self.btn_OK.grid(row=15, rowspan=20, column=2)

        self.btn_Cancel = Button(self.init_window_name, text="退出", bg="lightblue", width=5, command=self.init_window_name.quit)  # 调用内部方法  加()为直接调用
        self.btn_Cancel.grid(row=15, rowspan=20, column=5)


    #功能函数
    def localFolderSelect(self):
        Folderpath = filedialog.askdirectory()
        # self.localFolder_Text.delete(0, 'end')
        self.Edit_localpath.insert(1.0,Folderpath)

    def tag1FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath1.insert(1.0,Folderpath)

    def tag2FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath2.insert(1.0,Folderpath)

    def tag3FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath3.insert(1.0,Folderpath)

    def tag4FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath4.insert(1.0,Folderpath)

    def tag5FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath5.insert(1.0,Folderpath)

    def tag6FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath6.insert(1.0,Folderpath)

    def tag7FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath7.insert(1.0,Folderpath)

    def tag8FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath8.insert(1.0,Folderpath)

    def tag9FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath9.insert(1.0,Folderpath)

    def tag10FolderSelect(self):
        Folderpath = filedialog.askdirectory()
        self.Edit_tagpath10.insert(1.0,Folderpath)

    def merge(self):
        localpath = self.Edit_localpath.get(1.0,END).strip().replace("\n","")
        os.chdir(localpath)
        # print(os.getcwd())
        os.system('svn update')
        tagpath1 = self.Edit_tagpath1.get(1.0,END).strip().replace("\n","")
        tagpath2 = self.Edit_tagpath2.get(1.0,END).strip().replace("\n","")
        tagpath3 = self.Edit_tagpath3.get(1.0,END).strip().replace("\n","")
        tagpath4 = self.Edit_tagpath4.get(1.0,END).strip().replace("\n","")
        tagpath5 = self.Edit_tagpath5.get(1.0,END).strip().replace("\n","")
        tagpath6 = self.Edit_tagpath6.get(1.0,END).strip().replace("\n","")
        tagpath7 = self.Edit_tagpath7.get(1.0,END).strip().replace("\n","")
        tagpath8 = self.Edit_tagpath8.get(1.0,END).strip().replace("\n","")
        tagpath9 = self.Edit_tagpath9.get(1.0,END).strip().replace("\n","")
        tagpath10 = self.Edit_tagpath10.get(1.0,END).strip().replace("\n","")
        if tagpath1:
            os.system("rd /s/q %s\.settings" % (tagpath1))
            os.system("rd /s/q %s\.svn" % (tagpath1))
            os.system("rd /s/q %s\.vscode" % (tagpath1))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath1))
            try:
                os.system("svn merge %s" % (tagpath1))
            except Exception as e:
                print(e)
        if tagpath2:
            os.system("rd /s/q %s\.settings" % (tagpath2))
            os.system("rd /s/q %s\.svn" % (tagpath2))
            os.system("rd /s/q %s\.vscode" % (tagpath2))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath2))
            try:
                os.system("svn merge %s" % (tagpath2))
            except Exception as e:
                print(e)
        if tagpath3:
            os.system("rd /s/q %s\.settings" % (tagpath3))
            os.system("rd /s/q %s\.svn" % (tagpath3))
            os.system("rd /s/q %s\.vscode" % (tagpath3))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath3))
            try:
                os.system("svn merge %s" % (tagpath3))
            except Exception as e:
                print(e)
        if tagpath4:
            os.system("rd /s/q %s\.settings" % (tagpath4))
            os.system("rd /s/q %s\.svn" % (tagpath4))
            os.system("rd /s/q %s\.vscode" % (tagpath4))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath4))
            try:
                os.system("svn merge %s" % (tagpath4))
            except Exception as e:
                print(e)
        if tagpath5:
            os.system("rd /s/q %s\.settings" % (tagpath5))
            os.system("rd /s/q %s\.svn" % (tagpath5))
            os.system("rd /s/q %s\.vscode" % (tagpath5))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath5))
            try:
                os.system("svn merge %s" % (tagpath5))
            except Exception as e:
                print(e)
        if tagpath6:
            os.system("rd /s/q %s\.settings" % (tagpath6))
            os.system("rd /s/q %s\.svn" % (tagpath6))
            os.system("rd /s/q %s\.vscode" % (tagpath6))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath6))
            try:
                os.system("svn merge %s" % (tagpath6))
            except Exception as e:
                print(e)
        if tagpath7:
            os.system("rd /s/q %s\.settings" % (tagpath7))
            os.system("rd /s/q %s\.svn" % (tagpath7))
            os.system("rd /s/q %s\.vscode" % (tagpath7))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath7))
            try:
                os.system("svn merge %s" % (tagpath7))
            except Exception as e:
                print(e)
        if tagpath8:
            os.system("rd /s/q %s\.settings" % (tagpath8))
            os.system("rd /s/q %s\.svn" % (tagpath8))
            os.system("rd /s/q %s\.vscode" % (tagpath8))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath8))
            try:
                os.system("svn merge %s" % (tagpath8))
            except Exception as e:
                print(e)
        if tagpath9:
            os.system("rd /s/q %s\.settings" % (tagpath9))
            os.system("rd /s/q %s\.svn" % (tagpath9))
            os.system("rd /s/q %s\.vscode" % (tagpath9))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath9))
            try:
                os.system("svn merge %s" % (tagpath9))
            except Exception as e:
                print(e)
        if tagpath10:
            os.system("rd /s/q %s\.settings" % (tagpath10))
            os.system("rd /s/q %s\.svn" % (tagpath10))
            os.system("rd /s/q %s\.vscode" % (tagpath10))
            os.system("rd /s/q %s\.Debug_FLASH" % (tagpath10))
            try:
                os.system("svn merge %s" % (tagpath10))
            except Exception as e:
                print(e)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
