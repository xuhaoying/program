import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, text="你好，欢迎来玩TKInter!")
label.pack()
btn = tkinter.Button(root, text="点我退出!", command=root.destroy)
btn.pack(fill=tkinter.X, expand=1)
root.mainloop()

