from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    print(BMI)
    if BMI >=30:
        labelResult.configure(text=BMI)
        result.configure(text = "อ้วนเกินไป")
    elif BMI >=25:
        labelResult.configure(text=BMI)
        result.configure(text = "อ้วน")
    elif BMI >= 23:
        labelResult.configure(text=BMI)
        result.configure(text="ท้วม")
    elif BMI >= 18.6:
        labelResult.configure(text=BMI)
        result.configure(text="น้ำหนักปกติ")
    elif BMI <= 18.5:
        labelResult.configure(text=BMI)
        result.configure(text="ผอมเกินไป")
    else:
        print("ERROR!")

MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
lablelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)")
lablelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow, text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row = 2,column=0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
result = Label(MainWindow,text = "ผลประเมิน",fg = "red",bg = "yellow")
result.grid(row=3,column=1)
MainWindow.mainloop()