
import tkinter as tk  
window = tk.Tk()
window.title('my first GUI')
window.geometry('300x300')
label = tk.Label(window, text='GUI')
label.pack()
entry = tk.Entry(window,width='20')
entry.pack()
button = tk.Button(window,text='按鈕')
button.pack()
window.mainloop()
