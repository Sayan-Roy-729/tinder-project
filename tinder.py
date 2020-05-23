from tkinter import *
from dbhelper import DBHelper
from PIL import Image, ImageTk
from tkinter import messagebox
import re
from tkinter import filedialog
import shutil, os 



class Tinder:

    def __init__(self):

        '''In this constructor we put all the essential items that must be there when an onject is created. When obj = Tinder() is called, it opens up the constructor and creates a private object variable _root of type Tk(). Next it connects to the database and finally opens the window'''

        #self.dbconnect()
        self.db = DBHelper()

        self.load_login_window()

    def load_login_window(self):

        '''In this case, it opens up the initial login window after clearing whatever was there before.'''

        self._root = Tk()

        #Tinder Window Title
        self._root.title("Lovr\u00A9 | Match. Chat. Date ")
        self._root.minsize(550, 800)
        self._root.maxsize(550, 800)
        self._root.config(backgroung="#990033")

        #Heading creation
        self._label1 = Label(self._root, text="Lovr", fg="#F3EFE0", bg="#990033")
        self._label1.config(font=("Chalet-LondonNineteenSeventy", 50))
        self._label1.pack(pady=(30, 0))

        #Subtitle creation
        self._label2 = Label(self._root, text="Onestop Solution for Single-ism", fg="#F3EFE0", bg="#990033")
        self._label2.config(font=("Chalet-LondonNineteenEighty", 10))
        self._label2.pack(pady=(0, 30))

        # Input the Email after creating the label and input box
        self._email = Label(self._root, text="email", fg="#F3EFE0", bg="#990033")
        self._email.config(font=("Chalet-LondonNineteenSeventy", 16))
        self._email.pack(pady=(10,10))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(5,25), ipady=10, ipadx=30)

        #Input the password after creating the password label and input box
        self._password = Label(self._root, text="password", fg="#F3EFE0", bg="#990033")
        self._password.config(font=("Chalet-LondonNineteenEighty", 16))
        self._password.pack(pady=(10, 10))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        # Creating the button for Login
        self._login = Button(self._root, text="Login", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.check_login())
        self._login.config(font=("Chalet-LondonNineteenSeventy", 14), boderwidth=1)
        self._login.pack(pady=(30, 10))

        #mycode to print out if Invalid Password or email
        self._result = Label(self._root, fg="#F3EFE0", bg="#990033")
        self._result.pack()
        # done



        #Subtitle Creation
        self._label3 = Label(self._root, text=("-"*17) + (" OR ")+("-"*17), fg="#F3EFE0", bg="#990033")
        self._label3.config(font=("Chalet-LondonNineteenEighty", 20))
        self._label3.pack(pady=(25, 0))


        #Subtitle Creation
        self._label4 = Label(self._root, text="Register today to find the love of your life!", fg="#F3EFE0", bg="#990033")
        self._label4.config(font=("Chalet-LondonNineteenEighty", 12))
        self._label4.pack(pady=(15, 0))


        # Creating the Button for Registration
        self._reg = Button(self._root, text="SignUp", fg="#F3EFE0", bg="#990033", width=15, height=1, command=lambda: self.regWindow())
        self._reg.config(font=("Chalet-LondonNineteenEighty", 14), borderwidth=1)
        self._reg.pack(pady=(30, 10))

        self._root.mainloop()



    def check_login(self):

        """Retrieve the email and password and help a user to login"""

        email = self._emailInput.get()
        password = self._passwordInput.get()
        data = self.db.check_login(email, password)

        # print data
        if len(data)== 0:
            self._result.config(text="Incorrect Password or Email", font=("Arial", 10))
            messagebox.showerror("Error", "User Not Found!")
        else:
            self.user_id = data[0][0]
            self.is_logged_in = 1
            self.login_handler()


    def regWindow(self):

        self.clear()

        # Input the Email after creating the Email Label and Input Box

        # Heading creation
        self._label1 = Label(self._root, text = "Sign Up", fg="#F3EFE0", bg="#990033")
        self._label1.config(font=("Chalet-LondonNineteenSeventy", 50))
        self._label1.pack(pady=(25, 15))

        sec1 = Frame(self._root)
        sec1.pack(pady=(20, 20))

        self._email = Label(sec1, text="email", fg="#F3EFE0", bg="#990033")
        self._email.config(font=("Chalet-LondonNineteenSeventy", 16), anchor="e")
        self._email.pack(side=LEFT, pady=(0,0), ipady=6, ipadx=30)

        self._emailInput = Entry(sec1)
        self._emailInput.pack(side=LEFT, pady=(0,0), ipady = 6, ipadx=30)

        # Input the password after creating the password label and input box

        sec2 = Frame(self._root)
        sec2.pack(pady=(20,20))

        self._password = Label(sec2, text="password", fg="#F3EFE0", bg="#990033")
        self._password.config(font=("Chalet-LondonNinteenEighty", 16), anchore="e")
        self._password.pack(side=LEFT, pady=(0,0))

        self._passwordInput = Entry(sec2)
        self._passwordInput.pack(side=LEFT, pady=(0, 0), ipady = 6, ipadx=30)

        # Input the name after creating the email label and input box
        sec3 = Frame(self._root)
        sec3.pack(pady=(20, 20))

        self._name = Label(sec3, text="name", fg="#F3EFE0", bg="#990033")
        self._name.config(font=("Chalet-LondonNinteenSeventy", 16), anchor = "e")
        self._name.pack(side=LEFT, pady=(0, 0))

        self._nameInput = Entry(sec3)
        self._nameInput.pack(side= LEFT, pady=(0, 0), ipady = 6, ipadx = 30)


        # Input the age after creating the password label and input box
        sec4 = Frame(self._root)
        sec4.pack(pady=(20, 20))

        self._age = Label(sec4, text="age", fg="#F3EFE0", bg="#990033")
        self._age.config(font=("Chalet-LondonNinteenSeventy", 16), anchor = "e")
        self._age.pack(side=LEFT, pady=(0, 0))

        self._ageInput = Entry(sec4)
        self._ageInput.pack(side= LEFT, pady=(0, 0), ipady = 6, ipadx = 30)


        # Input the gender after creating the password label and input box
        sec5 = Frame(self._root)
        sec5.pack(pady=(20, 20))

        self._gender = Label(sec5, text="gender", fg="#F3EFE0", bg="#990033")
        self._gender.config(font=("Chalet-LondonNinteenSeventy", 16), anchor = "e")
        self._gender.pack(side=LEFT, pady=(0, 0))

        self._genderInput = Entry(sec5)
        self._genderInput.pack(side= LEFT, pady=(0, 0), ipady = 6, ipadx = 30)


        # Input the city after creating the password label and input box
        sec6 = Frame(self._root)
        sec6.pack(pady=(20, 20))

        self._city = Label(sec6, text="city", fg="#F3EFE0", bg="#990033")
        self._city.config(font=("Chalet-LondonNinteenSeventy", 16), anchor = "e")
        self._city.pack(side=LEFT, pady=(0, 0))

        self._cityInput = Entry(sec6)
        self._cityInput.pack(side= LEFT, pady=(0, 0), ipady = 6, ipadx = 30)


        # Input the intro after creating the password label and input box
        sec7 = Frame(self._root)
        sec7.pack(pady=(20, 20))

        self._intro = Label(sec7, text="intro", fg="#F3EFE0", bg="#990033")
        self._intro.config(font=("Chalet-LondonNinteenSeventy", 16), anchor = "e")
        self._intro.pack(side=LEFT, pady=(0, 0))

        self._introInput = Entry(sec7)
        self._introInput.pack(side= LEFT, pady=(0, 0), ipady = 6, ipadx = 30)

        self.dp = Button(self._root, texy="Upload a display picture", command=lambda: self.select_dp())
        self.dp.pack(pady=(10, 10))

        self.dp_filename = Label(self._root)
        self.dp_filename.pack(pady=(10, 10))


        # Creating button for SignUp
        self._signup = Button(self._root, text="Sign Up", fg="#F3EFE0", bg="#990033", width=10, height=1, command=lambda:self.reg_handler())
        self._signup.config(font=("Chalet-LondonNineteenSeventy", 14), borderwidth=1)
        self._signup.pack(pady=(5,5))



    def select_dp(self, f = 0):

        self.filename = filedialog.askopenfilename(initialdir = "/images", title="Browser")

        if f==1:
            self.dp_filename_edit.config(text=self.filename)
        else:
            self.dp_filename.config(text=self.filename)



    def mainWindow(self, data, flag = 0, index = 0):
        # Fetching data from database

        try:
            name = str(data[index][1])
            email = data[index][2]
            age = str(data[index][4])
            gender = str(data[index][5])
            city = str(data[index][6])
            dp = data[index][7]

        except:
            # No one is there code
            self._nouser = Label(self._root, text="Alas! There is no user currentrly. \nBut there's alawys someone out there. \nSo keep swiping.",fg="#F3EFE0", bg="#990033")
            self._nouser.config(font=("Chalet-LondonNineteenEighty", 15))
            self._nouser.pack(pady=(350, 30))

        else:
            newintro = str(data[index][8])
            newintro = newintro.replace(",", ".")
            intro = ""
            intro_sent = newintro.split('.')

            for sent in intro_sent:
                intro = intro + "\n" + sent

            intro = intro.strip()
            intro = "\u201c" + intro + "\u201D"

            if flag ==1:

                # Heading creation
                self._menu1 = Label(self._root, text="View Others", fg="#F3EFE0", bg="#990033")
                self._menu1.config(font=("Chalet-LondonNineteenEighty", 40))
                self._menu1.pack(pady=(20, 0))

                frame = Frame(self._root)
                frame.pack(pady=(10, 10))

                previous = Button(frame, text="<--- Previous", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_others(index - 1))
                previous.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                previous.pack(side=LEFT)

                propose = Button(frame, text="Propose", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.propose(self.user_id, data[index][0]))
                propose.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                propose.pack(side=LEFT)

                next = Button(frame, text="next --->", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_others(index + 1))
                next.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                next.pack(side=LEFT)


            elif flag == 2:
                
                # Heading creation
                self._menu2 = Label(self._root, text="You're Liked by", fg="#F3EFE0", bg="#990033")
                self._menu2.config(font=("Chalet-LondonNineteenEighty", 40))
                self._menu2.pack(pady=(20, 0))

                frame = Frame(self._root)
                frame.pack(pady=(10, 10))

                previous = Button(frame, text="<--- Previous", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_proposals(index - 1))
                previous.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                previous.pack(side=LEFT)

                propose = Button(frame, text="Propose", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.propose(self.user_id, data[index][0]))
                propose.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                propose.pack(side=LEFT)

                next = Button(frame, text="next --->", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_proposals(index + 1))
                next.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                next.pack(side=LEFT)

            elif flag ==3:

                # Heading creation
                self._menu3 = Label(self._root, text="Requests Sent to", fg="#F3EFE0", bg="#990033")
                self._menu3.config(font=("Chalet-LondonNineteenEighty", 40))
                self._menu3.pack(pady=(20, 0))

                frame = Frame(self._root)
                frame.pack(pady=(10, 10))

                previous = Button(frame, text="<--- Previous", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_requests(index - 1))
                previous.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                previous.pack(side=LEFT)

                next = Button(frame, text="next --->", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_requests(index + 1))
                next.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                next.pack(side=LEFT)


            elif flag == 4:

                # Heading creation
                self._menu4 = Label(self._root, text="You Liked Each Other!", fg="#F3EFE0", bg="#990033")
                self._menu4.config(font=("Chalet-LondonNineteenEighty", 40))
                self._menu4.pack(pady=(20, 0))

                frame = Frame(self._root)
                frame.pack(pady=(10, 10))

                previous = Button(frame, text="<--- Previous", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_matches(index - 1))
                previous.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                previous.pack(side=LEFT)

                next = Button(frame, text="next --->", fg="#F3EFE0", bg="#990033", width=25, height=2, command=lambda: self.view_matches(index + 1))
                next.config(font=("Chalet-LondonNineteenEighty", 10), boderwidth=1)
                next.pack(side=LEFT)


            elif flag ==0:

                #Heading creation
                self._menu5 = Label(self._root, text="My Profile", fg="#F3EFE0", bg="#990033")
                self._menu5.config(font=("Chalet-LondonNineteenEighty", 40))
                self._menu5.pack(pady=(20, 0))


            # Adding a Picture

            imageUrl = "images/" + str(dp)

            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack(pady=(2,2))

            name_label = Label(self._root, text="{}, {}".format(name, age), fg="#000", bg="#F3EFE0")
            name_label.config(font=("Arial", 12))
            name_label.pack(pady=(10, 0), ipadx = 300)

            info_label = Label(self._root, text="{} | {}".format(gender, city), fg="#000", bg="#F3EFE0")
            info_label.config(font=("Arial", 12))
            info_label.pack(pady=(10, 0), ipadx = 300)


            intro_label = Label(self._root, text="intro", fg="#000", bg="#990033")
            intro_label.config(font=("Comic Sans MS", 11))
            intro_label.pack(pady=(10, 10), ipadx = 20, ipady = 10)


            # city_label = Label(self._root, text=city, fg="#C70039", bg="#fff")
            # city_label.config(font=("Comic Sans MS", 11))
            # city_label.pack(pady=(0, 10), ipadx = 90, ipady = 10)



    def propose(self, romeo, juliet):
        

        flag=self.db.insert_proposal(romeo,juliet)

        if flag==1:
            messagebox.showinfo("Congrats","Proposal Sent. Fingers Crossed!")
        elif flag==2:
            messagebox.showerror("Error","Already done")
        else:
            messagebox.showerror("Error","INSERTION NOT DONE!")



    def login_handler(self):
        # To load user's profile
        # clear screen
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        self.mainWindow(data, flag=0)



    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()


    
    def view_others(self, index=0):

        # fetch data of all other users from db
        data = self.db.fetch_otheruserdata(self.user_id)

        if index==0:
            self.clear()
            self.mainWindow(data, flag=1, index=0)
        else:
            if index<0:
                messagebox.showerror("No User","Click on Next")

            elif index == len(data):
                messagebox.showerror("No User Left","Click on Previous")

            else:
                self.clear()
                self.mainWindow(data, flag=1, index=index)


    def logout(self):

        self.is_logged_in = 0
        self._root.destroy()
        self.load_login_window()


    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.login_handler())
        filemenu.add_command(label="Edit Profile", command=lambda: self.edit_profile())
        filemenu.add_command(label="View Profile", command=lambda: self.view_others())
        filemenu.add_command(label="LogOut", command=lambda : self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: self.view_proposals())
        helpmenu.add_command(label="My Requests", command=lambda: self.view_request())
        helpmenu.add_command(label="My Matches", command=lambda: self.view_matches())


    def edit_profile(self):

        data = self.db.fetch_userdata(self.user_id)

        self.clear()

        self._label1 = Label(self._root, text="Edit Profile", fg="#F3EF0", bg="#990033")
        self._label1.config(font=("Chalet-LondonNineteenSeventy", 25))
        self._label1.pack(pady=(30, 30))

        # Input the name after creating the Email Label and Input Box
        self._name_edit = Label(self._root, text = "name", fg="#F3EF0", bg="#990033")
        self._name_edit.config(font=("Chalet-LondonNineteenSeventy", 16))
        self._name_edit.pack(pady=(0, 0))

        self._name_editInput = Entry(self._root)
        self._name_editInput.insert(0, data[0][1])
        self._name_editInput.pack(pady=(5, 5), ipady = 10, ipadx = 30)


        # Input the age after creating the name label and input box
        self._age_edit = Label(self._root, text = "age", fg="#F3EF0", bg="#990033")
        self._age_edit.config(font=("Chalet-LondonNineteenSeventy", 16))
        self._age_edit.pack(pady=(0, 0))

        self._age_editInput = Entry(self._root)
        self._age_editInput.insert(0, data[0][4])
        self._age_editInput.pack(pady=(5, 5), ipady = 10, ipadx = 30)

        # Input the city after creating the age label and input box
        self._city_edit = Label(self._root, text = "city", fg="#F3EF0", bg="#990033")
        self._city_edit.config(font=("Chalet-LondonNineteenSeventy", 16))
        self._city_edit.pack(pady=(0, 0))

        self._city_editInput = Entry(self._root)
        self._city_editInput.insert(0, data[0][6])
        self._city_editInput.pack(pady=(5, 5), ipady = 10, ipadx = 30)

        # Input the intro after creating the city label and input box
        self._intro_edit = Label(self._root, text = "intro", fg="#F3EF0", bg="#990033")
        self._intro_edit.config(font=("Chalet-LondonNineteenSeventy", 16))
        self._intro_edit.pack(pady=(0, 0))

        self._intro_editInput = Entry(self._root)
        self._intro_editInput.insert(0, data[0][8])
        self._intro_editInput.pack(pady=(5, 5), ipady = 10, ipadx = 30)


        # Input the dp after creating the intro label and input box
        self.dp_edit = Button(self._root, text="Select a dp", command=lambda: self.select_dp(f = 1))
        self.dp_edit.pack(pady=(5,5))

        self.dp_filename_edit = Label(self._root)
        self.dp_filename_edit.pack(pady=(5, 5))


        # Creating the button for save changes
        self._edit = Button(self._root, text="Save Changes", bg="#990033", width=20, height=1, fg = "#F3EFE0", command=lambda: self.edit_handler())
        self._edit.config(font=("Chalet-LondonNineteenSeventy", 14), boderwidth=1)
        self._edit.pack(pady=(5, 5))

    

    def edit_handler(self):

        f_is_pic_edited = True

        try:
            filename_edit = self.filename.split("/")[-1]
        except:
            old_pic = (self.db.fetch_userdata(self.user_id))[0][7]
            filename_edit = old_pic
            f_is_pic_edited = False

        f_edit = self.db.update_info(self._name_editInput.get(), self._age_editInput.get(), self._city_editInput.get(), filename_edit, self._intro_editInput.get(), self.user_id)

        if f_edit == 1:
            if f_is_pic_edited == True:
                self.dpedit(filename_edit)

            messagebox.showinfo("Success", "Your information has been updated!")
        else:
            messagebox.showerror("Error", "Some error occured!")



    def view_proposals(self, index=0):

        data=self.db.fetch_proposals(self.user_id)

        new_data=[]

        for i in data:
            new_data.append(i[3:])

        if index == 0:
            self.clear()
            self.mainWindow(new_data, flag=2, index=0)
        else:
            if index<0:
                messagebox.showerror("Error","No user left")
            elif index == len(new_data):
                messagebox.showerror("Error","No user left")
            else:
                self.clear()
                self.mainWindow(new_data, flag=2, index=index)




    def view_request(self, index=0):

        data = self.db.fetch_requests(self.user_id)

        new_data = []

        for i in data:
            new_data.append(i[3:])

        if index == 0:
            self.clear()
            self.mainWindow(new_data, flag=3, index=0)
        else:
            if index < 0:
                messagebox.showerror("Error", "No user left")
            elif index == len(new_data):
                messagebox.showerror("Error", "No user left")
            else:
                self.clear()
                self.mainWindow(new_data, flag=3, index=index)
                

    def view_matches(self, index=0):

        data = self.db.fetch_matches(self.user_id)

        new_data = []

        for i in data:
            new_data.append(i[3:])

        if index == 0:
            self.clear()
            self.mainWindow(new_data, flag=4, index=0)
        else:
            if index < 0:
                messagebox.showerror("Error", "No user left")
            elif index == len(new_data):
                messagebox.showerror("Error", "No user left")
            else:
                self.clear()
                self.mainWindow(new_data, flag=4, index=index)


    def reg_handler(self):

        actual_filename = self.filename.split("/")[-1]

        flag = self.db.register(self._nameInput.get(), self._emailInput.get(), self._passwordInput.get(), self._ageInput.get(), self._genderInput.get(), self._cityInput.get(), actual_filename, self._introInput.get())

        if flag == 1:

            destination = "c:\\Users\\AICH\\PycharmProjects\\tinder\\images\\" + actual_filename
            shutil.copyfile(self.filename, destination)
            messagebox.showinfo("Success", "Registered Successfully")
            self._root.destroy()
            self.load_login_window()
        
        else:
            messagebox.showerror("Error", "Try again!")

    def dpedit(self, actual_filename_edit):
        destination_edit = "C:\\Users\\Sayan\\PycharmProjects\\tinder\\images\\" + actual_filename_edit
        shutil.copyfile(self.filename, destination_edit)





obj = Tinder()
        




               







        

