import tkinter

window = tkinter.Tk()
window.title("Miles to KM")
window.minsize(300,200)
window.config(padx=20,pady=20)




equal = tkinter.Label(text="Equals", font=('Arial',14,'bold'))
equal.grid(column=0,row=3)
Miles = tkinter.Label(text="Miles", font=('Arial',14,'bold'))
Miles.grid(column=3, row=2)
Kilo = tkinter.Label(text="KM", font=('Arial',14,'bold'))
Kilo.grid(column=3,row=3)
KM = tkinter.Label(text=0, font=('Arial',14,'bold'))
KM.grid(column=2, row=3)

def button_click():
  calc = round(int(input.get()) / 0.62,1)
  KM.config(text=calc)



button = tkinter.Button(text="click me",command=button_click)
button.grid(column = 2,row = 4)



input = tkinter.Entry(width=10)
input.grid(column = 2, row = 2)
print(input.get())


window.mainloop()