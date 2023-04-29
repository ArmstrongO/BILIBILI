# 定义一副扑克牌， 四个花色 红桃，梅花，方块，黑桃。 一个花色13张。 13 * 4 == 52  大小王 两张 一共54张
# 扑克牌要以列表保存， ["红桃",1-13] [[],[],[],[],[]54个] 大小王 ["Big_Joker"] ["Small_Joker"]
# python中有内置的库，叫做随机库
# 导入随机库的方式 import
import os


file_pp = fr"D:\puke.txt"
if os.path.exists(file_pp):
    os.remove(file_pp)
    pass
else:
    pass


def shengchan():
    file = open ( file="D:\puke.txt", mode="a", encoding="utf8" )
    color = ["红桃", "黑桃", "方块", "梅花"]
    file.write ( f"[Big_Joker]\n[Small_Joker]\n" )
    for c in color:
        for n in range ( 1, 14 ):
            # file.write(str(c)+str(n)+"\n")
            file.write ( f"[花色：{c} 点数：{n}]\n" )

shengchan()
import random

def chouka():
    with open(file="D:\puke.txt",encoding="utf8") as f:
        lines = f.readlines()
        random_line = random.choice(lines)
        return random_line
        # print(type(random_list))


import  datetime
def t_time():
    now=datetime.datetime.now()
    now_str=now.strftime("%Y-%m-%d %H:%M:%S")
    return now_str
print(t_time())
def wanjia():
    xuanshou = ["小孙", "小兰", "老赵", "老王"]
    for c in xuanshou:
        wanjia=random.choice(xuanshou)
        return wanjia
def danchou():
    jieguo = wanjia () + "在" + t_time () + "的时间，抽到了一张牌" + chouka ()
    file = open ( file="D:\jilu.txt", mode="a", encoding="utf8" )
    file.write (jieguo)
    print ( jieguo )
while True:
    print("这里是抽卡时间，请输入1开始随机抽卡：")
    number = input("\n1.一发入魂\n2.十连满命\n3.百连\n4.退出")
    if number == "0":
        shengchan()
        print("抽卡系统已经加载")
    elif number == "1":
        danchou()
    elif number == "2":
        for n in range ( 1, 11 ):
            danchou()
    elif number == "3":
        for n in range ( 1, 101):
            danchou()
    elif number == "4":
        break
    else:
        pass







'''''
python
import tkinter as tk
from tkinter import filedialog

# 打开文件选择对话框
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

# 读取文件内容并打印第二行
with open(file_path, 'r') as f:
lines = f.readlines()
if len(lines) >= 2:
print(lines[1])
'''''

# pk = ["Big_Joker", "Small_Joker"]
# str_pk = ', '.join(pk)
# file.write(str_pk)