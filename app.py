from tkinter import *
import os


root = Tk()

def action(event):
    global val
    value = event.widget.cget('text')

    if value == '=':
        if val.get().isdigit():
            int(val.get)
        else:
            try:
                sol = eval(val.get())
                val.set(sol)
            except Exception as c:
                val.set('Error')
                print(c)

    elif value == 'C':
        val.set('')

    else:
        val.set(val.get()+value)
    screen.update()

def backspace(event):
    back = len(val.get())
    if back > 0:
        val.set(val.get()[:-1])

root.geometry('800x700')
root.config(bg='grey')
root.title('Calculator By - Mohit Kumhar')

try:
    icon_path = os.path.join(os.path.dirname(__file__), 'calculator.ico')
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Icon loading error: {e}")

# root.iconbitmap('calculator.ico')

head = Label(root, text='Calculator', font='roboto 27 italic')
head.pack()

val = StringVar()
val.set('')
screen = Entry(root,textvariable=val, font='roboto 30 bold')
screen.pack(fill=X, padx=15, pady=15)

f = Frame(root,bg='#5A5A5A', padx=10, pady=7)

b = Button(f, text='7',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='8',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='9',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='←', bg='black',fg='white', font='roboto 31 bold', padx=11, pady=6)
b.bind('<Button-1>', backspace)
b.pack(side=LEFT, padx=15)

f.pack()

f = Frame(root,bg='#5A5A5A', padx=10)

b = Button(f, text='4',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='5',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='6',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='+',bg='black',fg='white', font='roboto 32 bold', padx=18, pady=3)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=15)

f.pack()

f = Frame(root,bg='#5A5A5A', padx=10, pady=7)

b = Button(f, text='1',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='2',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='3',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='-',bg='black',fg='white', font='roboto 32 bold', padx=24, pady=3)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=15)

f.pack()

f = Frame(root,bg='#5A5A5A', padx=10)

b = Button(f, text='.', font='roboto 35 bold', padx=16, pady=0)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='0',font='roboto 30 bold', padx=15, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='C', font='roboto 30 bold', padx=14, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='*', bg='black',fg='white', font='roboto 31 bold', padx=22, pady=6)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=15)

f.pack()

f = Frame(root, bg='#5A5A5A', padx=6, pady=7)

b = Button(f, text='(', bg='black', fg='white', font='roboto 30 bold', padx=18, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text=')', bg='black', fg='white', font='roboto 30 bold', padx=20, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='/', bg='black', fg='white', font='roboto 30 bold', padx=20, pady=7)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=3)

b = Button(f, text='=', bg='black', fg='white', font='roboto 35 bold', padx=17, pady=0)
b.bind('<Button-1>', action)
b.pack(side=LEFT, padx=15)

f.pack()

root.mainloop()