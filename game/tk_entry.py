import tkinter

root = tkinter.Tk()

# 创建一个 entry
entry = tkinter.Entry(root)
entry.pack()

def get_text():
    text = entry.get()  # 获取文本框的内容
    print(text)

# 创建一个 button
button = tkinter.Button(root, text="获取entry的数据", command=get_text)

button.pack()

root.mainloop()
