
import tkinter as tk
import tkinter.messagebox

def clickme():
    tkinter.messagebox.showinfo(title='訊息',message='按鈕已被點選')
      
window = tk.Tk()
window.title('my first GUI')
window.geometry('300x300')

label = tk.Label(window, text='GUI')
label.pack()
entry = tk.Entry(window,width='20')
entry.pack()
button = tk.Button(window,text='按鈕',command = clickme)
button.pack()
window.mainloop()
