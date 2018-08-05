import requests
from config import * 
from tkinter import *
import tkinter.messagebox

user_input = ""
def clear_search(event):
   E1.delete(0, END) 

def getResponse():
    global user_input

    if(user_input):
        response = requests.get(URL,headers=Headers,params={"q":user_input,"appid":Api_key}).json()    
        message = "In "+user_input+",right now is "+response["weather"][0]["description"]+".Temperature is "+str(response["main"]["temp"])+".Pressure is "+str(response["main"]["pressure"])
        tkinter.messagebox.showinfo(f"Weather in {user_input}",message)
    else:
        tkinter.messagebox.showerror("Error","Please give a input")



   



def keyPressed(event):
  global E1
  global user_input
  user_input = E1.get()


root = Tk()
root.iconbitmap(r"c:/users/yash/desktop/python-weather-app/icon/icon.ico")
root.title("Weather App By Yashraj Basan")
root.geometry("1000x700")
frame = Frame(root,bg="#12c2e9",pady=200)
frame.pack()

label = Label( frame,  text="Weather App", relief="flat",bg="#12c2e9",bd=4,fg="white",pady=20)
label.config(font=('times', 30))
label.pack()

sv = StringVar()
E1 = Entry(frame,textvariable=sv,font=('times',18),relief="ridge",bd=1,bg="#12c2e9",fg="white",width=60)
E1.insert(0, 'city name or country name....')
E1.bind("<Button-1>", clear_search)
E1.bind("<KeyRelease>",keyPressed)
E1.pack()

btn = Button(frame, text ="Submit",relief="ridge",bd=1,bg="#12c2e9",fg="white",command=getResponse)
btn.config(font=('times',13))
btn.pack()


root.configure(background="#12c2e9")
root.mainloop(0)
# user_input = input("Enter a city name: ")
# response = requests.get(URL,headers=Headers,params={"q":user_input,"appid":Api_key})
# print(response.json())