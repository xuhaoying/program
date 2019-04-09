#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter


root = tkinter.Tk()
 
def myquit():
    print("按钮被点击")
    import sys
    # sys.exit("退出程序")  # 不建议这样退出
    root.destroy()  # 退出程序

img = tkinter.PhotoImage(file="mybun.gif")
# button = tkinter.Button(root, text ="点我退出", command=myquit)
# button = tkinter.Button(root, bitmap="error")
# button = tkinter.Button(root, bitmap='question')
button = tkinter.Button(root,image=img, command=myquit)
 
button.pack()

root.mainloop()