from tkinter import *
from turtle import bgcolor
from function import *
from PIL import Image, ImageTk

root = Tk()
root.title("File Handling")
root.geometry("800x800")
# frame = LabelFrame(root, bg = 'white', padx=15, pady=15)
# frame.pack(padx=15, pady=15)

ala_too = ImageTk.PhotoImage(Image.open('C:\\Users\\Hp\\Downloads\\unnamed.jpg').resize((50, 50)))
myImg = Label(image = ala_too)
myImg.grid(row=0, column=0)
text = StringVar()
text_ = StringVar()
text__ = StringVar()
entry_window = Entry(root, justify=LEFT, width=40, borderwidth=4, textvariable=text)
entry_window.grid(row=1, column=20, columnspan=3)

btn_check = Button(root, text="Open File", command=open_file)
btn_check.grid(row=2, column=20, columnspan=3)

entry_window2 = Entry(root,justify=LEFT, width=40,borderwidth=4, textvariable=text_)
entry_window2.grid(row=3, column=20, columnspan=3)

label = Label(root,text="Enter text for apeend:")
label.grid(row=4, column=20, columnspan=3)
entry_window3 = Entry(root,justify=LEFT, width=40, borderwidth=4, textvariable=text__)
entry_window3.grid(row=5, column=20, columnspan=3)

btn_check1 = Button(root, text="Create File", command=create_file, bg='blue', fg='white')
btn_check1.grid(row=6, column=20)

btn_check2 = Button(root, text="Append Text", command=append_text, bg='blue', fg='white')
btn_check2.grid(row=6, column=21)

btn_check3 = Button(root, text="Close File", command=root.destroy, bg='blue', fg='white')
btn_check3.grid(row=6, column=22)

root.mainloop()
