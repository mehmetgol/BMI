import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("BMI")
window.minsize(width=300,height=300)
image_path = "WhatsApp Image 2024-12-07 at 8.03.05 PM.jpeg"
img = Image.open(image_path)
img = img.resize((100, 100))

photo = ImageTk.PhotoImage(img)

label = tkinter.Label(window, image=photo)
label.pack()

weightTk = tkinter.Label(text = "please enter your weight")
weightTk.pack()
weightEnter = tkinter.Entry()
weightEnter.pack()

heightTk = tkinter.Label(text = "please enter your height(example 1.75)")
heightTk.pack()

heightEnter =tkinter.Entry()
heightEnter.pack()
def BMI():
    try :
        weightGet = float(weightEnter.get())
        heightGet = float(heightEnter.get())
        BMIresult = weightGet / (heightGet * heightGet )
        if BMIresult < 18.5 :
            underweightLabel = tkinter.Label(text ="you are underweight")
            underweightLabel.pack()
        elif 24.9 >=BMIresult >= 18.5 :
            normalweightLabel = tkinter.Label(text ="you are normalweight")
            normalweightLabel.pack()
        elif 29.9 >= BMIresult >= 25 :
            overweightLabel = tkinter.Label(text ="you are overweight")
            overweightLabel.pack()
        elif 34.9 > BMIresult >= 30 :
            o1weightLabel = tkinter.Label(text ="you are obesity 1 weight")
            o1weightLabel.pack()
        elif 39.9 >= BMIresult >=35 :
            o2weightLabel = tkinter.Label(text ="you are obesity 2 weight")
            o2weightLabel.pack()
        else :
            o3weightLabel = tkinter.Label(text ="you are obesity 3 weight")
            o3weightLabel.pack()

        resultBMI = tkinter.Label(text = f"your BMI is :{BMIresult}")
        resultBMI.pack()
    except ValueError:
        print("Please enter valid numbers for both weight and height.")
weightB = tkinter.Button(text= "enter", command=BMI)
weightB.pack()


window.mainloop()
