from tkinter import *
root = Tk()
root.title("Broughton Login Portal")

# reads user credentials from 'username.txt' and 'password.txt'

u = open("username.txt", "r")
p = open("password.txt", "r")
name = str(u.read())
passw = str(p.read())

# username field
userLabel = Label(root,text=" username: ", font=("monospace"))
userLabel.grid(row=1,column=0)
u = Entry(root, width=35, borderwidth=5)
u.grid(row=1,column=1,columnspan=3,padx=10,pady=10)

# password field
passLabel = Label(text=" password: ", font=("monospace"))
passLabel.grid(row=2,column=0)
p = Entry(root, width=35, borderwidth=5)
p.grid(row=2,column=1,columnspan=3,padx=10,pady=10)

# login label
loginStatus = Label(text="")
loginStatus.grid(row=3,column=1)

title = Label(text="Login", font=("monospace", 30))
title.grid(row=0,column=2)

num_lines = 0
ulines = list()
plines = list()

# create list of usernames
with open('username.txt') as un:
   line = un.readline()
   cnt = 0
   while line:
       ulines.append(line.strip())
       line = un.readline()
       cnt += 1

# create list of passwords
with open('password.txt') as pw:
   line = pw.readline()
   cnt = 0
   while line:
       plines.append(line.strip())
       line = pw.readline()
       cnt += 1


from tkinter import *
a = Tk()
a.title("Message")
a.withdraw()

# login button
def login(uname, pword):
    loginStatus.config(text="")
    for i in range(len(ulines)):
        if (str(uname) == ulines[i] and str(pword) == plines[i]):
            loginStatus.config(text="success!")
            p.delete(0,END)
            a.deiconify()# show the window
            break
        else:
            loginStatus.config(text="failure")
            p.delete(0,END)


testLabel = Label(a, text="Hello")
testLabel.grid(row=0,column=0)

loginButton = Button(root, text="login", padx=40, pady=10, bg='#cc0000', fg='#d9d9d9',command=lambda: login(u.get(),p.get()))
loginButton.grid(row=3,column=3)


a.mainloop()
root.mainloop()