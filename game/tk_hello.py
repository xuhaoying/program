import tkinter

# 创建顶层窗口
root = tkinter.Tk()

# 创建一个标签控件
label = tkinter.Label(root, text="hello world")

# 把label放置在root窗口上
label.pack()

label2 = tkinter.Label(root, text="你好中国", 
        font=("黑体", 24, "bold"), bg="#bbada0", fg="#eee4da")
label2.pack()

# 进入主事件循环
print("正在进入主事件循环")
root.mainloop()
print("程序退出")

