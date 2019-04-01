import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text="第一行")
label1.pack()

label2 = tkinter.Label(root, text="第二行", bg="green")
label2.pack()

label3 = tkinter.Label(root, text="第三行", bg="red")
label3.pack()

label4 = tkinter.Label(root, text="第四行", fg="blue", bg="yellow",
       width=10, height=3, font=("youyuan", 20))
label4.pack()

root.mainloop()