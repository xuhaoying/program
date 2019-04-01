import tkinter

root = tkinter.Tk()

tkinter.Button(root, text="left").pack(side="left")
tkinter.Button(root, text="right").pack(side="right")
tkinter.Button(root, text="top").pack(side="top")
tkinter.Button(root, text="bottom").pack(side="bottom")

root.mainloop()
