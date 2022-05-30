def open_file():
    global text1
    text1.set("")
    if entry_window.get():
        file = open(entry_window.get(),'r')
        for each in file:
            text1.set(each)

def create_file():
    global text1
    text1.set("")
    if entry_window.get():
        f = open(entry_window.get(), "x")
        text1.set("Create File Successfully")


def append_text():
    global text2
    text1.set("")
    if entry_window.get():
        file = open(entry_window.get(),'r')
        for each in file:
            text1.set(each)
        file3=open(entry_window.get(),"a")
        #c=input("Enter string to append: \n")
        if entry_window3.get():
            #file3.write("\n")
            file3.write(entry_window3.get())
            file3.close()
            text1.set("Append Successfully")
