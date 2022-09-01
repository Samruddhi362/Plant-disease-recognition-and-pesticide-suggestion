#import modules
 
from tkinter import *
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import os
from keras.preprocessing import image
import numpy as np
from deeplearning import graph, model, output_list,output_list1
import cv2
print(output_list)

import time
import glob
global path
# Designing window for registration
def mains():
    main_screen.destroy()
    root = Tk()
    root.geometry("1500x1000")
    root.title('Leaf disease detection')

    newline= Label(root)
    uploaded_img=Label(root)
    ##scrollbar = Scrollbar(root)
    ##scrollbar.pack( side = RIGHT, fill = Y )
    def extract():
        global path
        Actual_image = cv2.imread(path)
        Sample_img = cv2.resize(Actual_image,(400,350))
        Image_ht,Image_wd,Image_thickness = Sample_img.shape
        Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
        myfile = path
        img = image.load_img(myfile, target_size=(150,150))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img/255
        
        with graph.as_default():
            prediction = model.predict(img)
            
            

        prediction_flatten = prediction.flatten()
        var= (prediction_flatten[0])


        max_val_index = np.argmax(prediction_flatten)
        print(max_val_index)
        acc=(prediction_flatten[max_val_index])
        acc=acc*100
        print(acc)
        acc=str(acc)
        result = output_list[max_val_index]
        result1 = output_list1[max_val_index]
        l1="Disease "+result
        l2="Pesticide recomended "+result1
        l3="Accuracy "+acc
        print (l1)
        print (l2)
        print (l3)

       
        labelA = tk.Label(root, text = l1, fg="black", bg="#FFF",font=('Times',20,'bold'))
        labelB = tk.Label(root, text = l2, fg="black", bg="#FFF",font=('Times',20,'bold'))
        labelC = tk.Label(root, text = l3, fg="black", bg="#FFF",font=('Times',20,'bold'))
       

        labelA.place(x=950, y=200)
        labelB.place(x=950, y=250)
        labelC.place(x=950, y=300)
        
    def show_extract_button():
        extractBtn= Button(root,text="Predict",command=lambda: extract(),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
        extractBtn.pack()
    def upload():
        
        try:
            global path
            path=filedialog.askopenfilename()
            
            image=Image.open(path)
            img=ImageTk.PhotoImage(image)
            uploaded_img.configure(image=img)
            uploaded_img.image=img
            
            
        except:
            pass
##    def reset():
##        labelA = tk.Label(root, text = "", fg="black", bg="#FFF",font=('Times',20,'bold'))
##        labelB = tk.Label(root, text = "", fg="black", bg="#FFF",font=('Times',20,'bold'))
##        labelC = tk.Label(root, text = "", fg="black", bg="#FFF",font=('Times',20,'bold'))
##       
##
##        labelA.place(x=650, y=200)
##        labelB.place(x=650, y=250)
##        labelC.place(x=650, y=300)
##        print('k')
    def exits():
        
        root.destroy()
    
    uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
    show_extract_button()
    #reset = Button(root,text="Reset",command=reset,bg="#2f2f77",fg="gray",height=2,width=10,font=('Times',10,'bold')).place(x=650, y=400)
    exits = Button(root,text="Exit",command=exits,bg="#2f2f77",fg="gray",height=2,width=10,font=('Times',10,'bold')).place(x=750, y=600)
    #reset.place(x=650, y=400)
    newline.configure(text='\n')

    newline.pack()
    uploaded_img.pack()
    root.mainloop()

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    mains()
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
