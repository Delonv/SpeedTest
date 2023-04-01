from tkinter import *
from speedtest import Speedtest
from PIL import Image, ImageTk


def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Скорость загрузки:\n" + str(download_speed) + " MbPs")
    upload_label.config(text="Скорость отдачи:\n" + str(upload_speed) + " MbPs")


root = Tk()

root.title("Speedtest")
root.geometry("300x400")
root.resizable(width=False, height=False)

logo = PhotoImage(file='logo.png')
label1 = Label(root, image= logo)
label1.place(x=0,y=0)

button = Button(root, text="Проверка", font=35,bg='black',fg='lime', command=test)
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text="Скорость загрузки:\n",bg='orange', fg='black', font=30)
download_label.pack(pady=(50, 0))

upload_label = Label(root, text="Скорость отдачи:\n",bg='orange', fg='black', font= 35)
upload_label.pack(pady=(40,20))

root.mainloop()