from tkinter import ttk
from tkinter import *
import json
import tkinter as tk
from tkinter.constants import END


windows = Tk()  # 初始框的声明
windows.title('Checkout')  # 视窗名称


number = []
module = []
url = []
local = []


def openA13():
    global number, module, url, local
    for i in range(max(len(module), len(url), len(local))):
        items = treeview.get_children()[0:1]
        treeview.delete(items)
    number = []
    module = ['Adc', 'Base', 'Fee']
    url = ['10.71.223', '10.1.186', '10.1.163']
    local = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
    for i in range(min(len(module), len(url), len(local))):  # 写入数据
        number.append(i)
        treeview.insert('', i, values=(i, module[i], url[i], local[i]))


def openA18():
    global number, module, url, local
    for i in range(max(len(module), len(url), len(local))):
        items = treeview.get_children()[0:1]
        treeview.delete(items)
    number = []
    module = ['Adc', 'Base', 'Fee']
    url = ['10.71.3', '10.1.186', '10.1.163']
    local = ['10.13.71.223', '10.61.186', '10.25.11.163']
    for i in range(min(len(module), len(url), len(local))):  # 写入数据
        number.append(i)
        treeview.insert('', i, values=(i, module[i], url[i], local[i]))


def openA20():
    global number, module, url, local
    for i in range(max(len(module), len(url), len(local))):
        items = treeview.get_children()[0:1]
        treeview.delete(items)
    number = []
    module = ['Adc', 'Base', 'Fee']
    url = ['10.71.223', '10.1.16', '10.1.163']
    local = ['10.13.71.223', '10.25.61.186', '10.21.163']
    for i in range(min(len(module), len(url), len(local))):  # 写入数据
        number.append(i)
        treeview.insert('', i, values=(i, module[i], url[i], local[i]))


def openA29():
    global number, module, url, local
    for i in range(max(len(module), len(url), len(local))):
        items = treeview.get_children()[0:1]
        treeview.delete(items)
    number = []
    module = ['Adc', 'Base', 'Fee']
    url = ['10.73', '10.1.186', '10.1.163']
    local = ['10.13.71.223', '10.25.61.186', '10.25.3']
    for i in range(min(len(module), len(url), len(local))):  # 写入数据
        number.append(i)
        treeview.insert('', i, values=(i, module[i], url[i], local[i]))


def newrow():
    number.append(len(module))
    module.append('模块命名')
    url.append('服务端地址')
    local.append('本地地址')
    treeview.insert('', len(module)-1, values=(number[len(module)-1], module[len(
        module)-1], url[len(module)-1], local[len(module)-1]))
    treeview.update()


menubar = tk.Menu(windows)  # 定义菜单栏
filemenu = tk.Menu(menubar, tearoff=0)  # 在菜单栏中定义菜单
menubar.add_cascade(label='File', menu=filemenu)  # 添加到菜单栏中，设置标签
filemenu.add_command(label='A13', command=openA13)  # 在菜单中定义项的标签及功能
filemenu.add_command(label='A18', command=openA18)
filemenu.add_command(label='A20', command=openA20)
filemenu.add_command(label='A29', command=openA29)
filemenu.add_separator()  # 设置分隔符
filemenu.add_command(label='Save', command=newrow)
filemenu.add_command(label='Exit', command=windows.quit)  # 关闭菜单

submenubar = tk.Menu(filemenu)  # 在菜单中定义次级菜单
menubar.add_cascade(label='Import', menu=submenubar, underline=0)
submenubar.add_command(label='New', command=newrow)

windows.config(menu=menubar)

columns = ("number", "module", "url", "local")
headers = ("编号", "模块名称", "SVN路径", "本地路径")
widthes = (50, 100, 500, 500)
treeview = ttk.Treeview(
    windows, height=18, show="headings", columns=columns)  # 表格

for (column, header, width) in zip(columns, headers, widthes):
    treeview.column(column, width=width, anchor="w")
    treeview.heading(column, text=header, anchor="w")

treeview.pack(side=LEFT, fill=BOTH)


def set_cell_value(event):  # 双击进入编辑状态
    for item in treeview.selection():
        # item = I001
        item_text = treeview.item(item, "values")
        # print(item_text[0:2])  # 输出所选行的值
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(windows, width=10+(cn-1)*16, height=1)
    entryedit.place(x=16+(cn-1)*130, y=6+rn*20)

    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()
    okb = ttk.Button(windows, text='OK', width=4, command=saveedit)
    okb.place(x=90+(cn-1)*242, y=2+rn*20)

def NewModel(event):
    windows1 = tk.Tk()  # 定义视图窗口
    windows1.title('Change')  # 视窗名称
    windows1.geometry('500x40')  # 视窗大小
    for item in treeview.selection():
        # item = I001
        item_text = treeview.item(item, "values")
        # print(item_text[0:2])  # 输出所选行的值
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(windows1, width=10+(cn-1)*16, height=1)
    entryedit.pack()

    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()
        windows1.destroy()
    okb = ttk.Button(windows1, text='OK', width=4, command=saveedit)
    okb.pack()

    windows1.mainloop()

treeview.bind('<Double-1>', NewModel)  # 双击左键进入编辑


#----vertical scrollbar------------
vbar = ttk.Scrollbar(windows,orient=VERTICAL,command=treeview.yview)
treeview.configure(yscrollcommand=vbar.set)
treeview.grid(row=0,column=0,sticky=NSEW)
vbar.grid(row=0,column=1,sticky=NS)
 
#----horizontal scrollbar----------
hbar = ttk.Scrollbar(windows,orient=HORIZONTAL,command=treeview.xview)
treeview.configure(xscrollcommand=hbar.set)
hbar.grid(row=1,column=0,sticky=EW)

windows.mainloop()  # 进入消息循环
