from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import PhotoImage
from PIL import Image, ImageTk


background = "#e6852c"

root=Tk()
root.title("Signup System")
root.geometry("1250x700+210+100")
root.config(bg=background)
# root.resizable(False, False)

#icon image
# image_icon = PhotoImage(file="images/login.png")
# root.iconphoto(False, image_icon)

#background image
frame = Frame(root, )
frame.pack(fill=Y)


def login():
    root.destroy()
    import login


def  signupuser():
    username = user.get()
    password = code.get()

    print(username, password)

    
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="********", database="student_registration")
        my_cursor = conn.cursor()
        print("Connection Successfull")
    except:
        messagebox.showerror("Invalid", "Database connection error")
        return
    

    # query = "INSERT INTO login (Username, Password) VALUES(%s, %s)"
    # my_cursor.execute("USE student_registration;")
    my_cursor.execute(f"INSERT INTO student_registration.login(Username, Password) VALUES('{username}', '{password}');")
    # print(query)
    conn.commit()
    conn.close()


    messagebox.showinfo("Success", "Successfully Signup")
    root.destroy()
    import login





bimg = (Image.open("images/login.png"))
resize_image = bimg.resize((700, 800))
backgroundimgage = ImageTk.PhotoImage(resize_image)
Label(frame, image=backgroundimgage, bg=background).pack()

#user entity
def user_enter(e):
    user.delete(0, 'end')

def user_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'UserId')


# user entry
user = Entry(frame,width=11,fg="#959aa3",bg="#344869", border=0,font=("Arial",18))
user.insert(0,'UserId')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=298, y=298)

#password entity
def password_enter(e):
    code.delete(0, 'end')

def password_leave(e):
    passw = code.get()
    if passw == '':
        code.insert(0, 'Password')


# user entry
code=Entry(frame,width=11,fg="#959aa3",bg="#344869", border=0,font=("Arial",18))
code.insert(0,'Password')
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=298, y=370)


#hide nad show button 
button_mode = True
def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye)
        code.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=openeye)
        code.config(show="")
        button_mode = True

openeye = Image.open("images/openeye.png").resize((20,20))
openeye = ImageTk.PhotoImage(openeye)
closeeye = Image.open("images/closeeye.png").resize((20,20))
closeeye = ImageTk.PhotoImage(closeeye)

eyeButton = Button(frame, image=openeye, bg="#344869",bd=0, command=hide)
eyeButton.place(x=435, y=375)

#login button
signupButton = Button(root, text='Signup', bg="#344869", fg="#fff", width=8, height=1, font=("Arial", 12), bd=0,command=signupuser)
signupButton.place(x=645, y=490)

label = Label(root, text="Already have an account?", fg="#959aa3", font=("Arial", 9))
label.place(x=560, y=438)

loginButton = Button(root, width=8, text="login", fg="#171b21", font=("Arial", 9),cursor="hand2",command=login)
loginButton.place(x=710, y=437)


root.mainloop()