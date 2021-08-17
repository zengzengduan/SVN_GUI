#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
from tkinter import filedialog

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("项目配置")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('700x800+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高

        #标签
        self.init_data_label = Label(self.init_window_name, text='项目名称：', )
        self.init_data_label.grid(row=0, column=0)
        self.init_data_label = Label(self.init_window_name, text='平台根目录：', )
        self.init_data_label.grid(row=1, column=0)
        self.init_data_label = Label(self.init_window_name, text='本地根目录：', )
        self.init_data_label.grid(row=2, column=0)
        self.init_data_label = Label(self.init_window_name, text="平台模块", )
        self.init_data_label.grid(row=3, column=1)
        self.result_data_label = Label(self.init_window_name, text="项目使用模块", )
        self.result_data_label.grid(row=3, column=3)
        self.log_label = Label(self.init_window_name, text="项目专属模块", )
        self.log_label.grid(row=3, column=5)

        #文本框
        self.Edit_PrjName = Text(self.init_window_name, width=60, height=1)  # 项目名称
        self.Edit_PrjName.grid(row=0, column=1, rowspan=1, columnspan=7)
        self.Edit_PFRoot = Text(self.init_window_name, width=60, height=1)  # 平台根目录
        self.Edit_PFRoot.grid(row=1, column=1, rowspan=1, columnspan=7)
        self.Edit_LocalRoot = Text(self.init_window_name, width=60, height=1)  # 本地根目录
        self.Edit_LocalRoot.grid(row=2, column=1, rowspan=1, columnspan=7)

        #列表框
        self.ListBox_PfBlocks = Listbox(self.init_window_name, width=20, height=35)  #平台模块列表
        self.ListBox_PfBlocks.grid(row=4, column=1, rowspan=10, columnspan=1)
        self.ListBox_UseBlocks = Listbox(self.init_window_name, width=20, height=35)  #项目使用模块列表
        self.ListBox_UseBlocks.grid(row=4, column=3, rowspan=10, columnspan=1)
        self.ListBox_PrjBlocks = Listbox(self.init_window_name, width=20, height=35)  # 项目专属模块列表
        self.ListBox_PrjBlocks.grid(row=4, column=5, rowspan=10, columnspan=1)

        #按钮
        self.btn_browser = Button(self.init_window_name, text="浏览", bg="lightblue", width=10, command=self.localFolderSelect)  # 调用内部方法  加()为直接调用
        self.btn_browser.grid(row=2, column=6)

        self.btn_PfToUse = Button(self.init_window_name, text=">>", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_PfToUse.grid(row=6, column=2)

        self.btn_UseToPrj = Button(self.init_window_name, text=">>", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_UseToPrj.grid(row=6, column=4)

        self.btn_UseToPf = Button(self.init_window_name, text="<<", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_UseToPf.grid(row=9, column=2)

        self.btn_PrjToUse = Button(self.init_window_name, text="<<", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_PrjToUse.grid(row=9, column=4)

        self.btn_OK = Button(self.init_window_name, text="确定", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_OK.grid(row=15, rowspan=20, column=1)

        self.btn_Cancel = Button(self.init_window_name, text="取消", bg="lightblue", width=5, command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.btn_Cancel.grid(row=15, rowspan=20, column=5)


    #功能函数
    def localFolderSelect(self):
        Folderpath = filedialog.askdirectory()
       # self.localFolder_Text.delete(0, 'end')
        self.Edit_LocalRoot.insert(1.0,Folderpath)

    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()