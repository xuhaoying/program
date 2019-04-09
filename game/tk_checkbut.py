import tkinter

root = tkinter.Tk()

def onCheckBtn():
    v = myvar.get()
    print("CheckButton被点击， v=", v)

# 创建一个整型变量
myvar = tkinter.IntVar()
# 选框
# 让 checkbtn关联myvar
checkbtn = tkinter.Checkbutton(root, text="自动登录", 
                command=onCheckBtn, variable=myvar)

checkbtn.pack()

myvar2 = tkinter.IntVar(value=1)
checkbtn2 = tkinter.Checkbutton(root, text='真值', variable=myvar2)

checkbtn2.pack()
root.mainloop()