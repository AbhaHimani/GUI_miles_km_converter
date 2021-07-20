import tkinter
window= tkinter.Tk()
window.title("Mile to Km converter")
window.wm_minsize(300,300)
my_Label = tkinter.Label(text= "Mile to Km converter")
my_Label.place(x=40, y=20)
input= tkinter.Entry()
input.place(x=40, y=50)

my_Label= tkinter.Label(text="miles")
my_Label.place(x=150, y=50)
kilo_result= tkinter.Label()

def on_click():
    answer = float(input.get())
    km= float(answer*1.609)
    kilo_result.config(text=f"{km}")
    kilo_result.place(x=100,y=70)
my_Label= tkinter.Label(text="kms")
my_Label.place(x=150, y=70)

#Button
button= tkinter.Button(text="Convert", command=on_click)
button.place(x=10,y=90)





my_Label.mainloop()