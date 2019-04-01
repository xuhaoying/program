import tkinter

root = tkinter.Tk()

def onKeyDown(event):
    print("有键盘按键被按下, event=",event.keycode, event.keysym, event.char)

def onKeyUp(event):
    print("有键盘按键被抬起",event)

root.bind('<KeyPress>', onKeyDown)
root.bind('<KeyRelease>', onKeyUp)

def mouseDown(e):
    print("鼠标按下在", e.x, e.y, e.x_root, e.y_root)

root.bind("<Button>", mouseDown)

def mouseUp(e):
    print("鼠标抬起", e.x, e.y)
    if e.num == 2:
        print("中间键抬起！！！")

root.bind("<ButtonRelease>", mouseUp)

tkinter.Button(root, text="Quit", command=root.destroy).pack()



root.mainloop()