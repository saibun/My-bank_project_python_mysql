#Using Tkinter, a feature of python to load the Gaphical User Interface
from tkinter import *

#connect with the database query file
from connectdb import Connect
from tkinter import messagebox

class My_bank:

    def __init__(self):
        self.cd = Connect()
        
        #Creating GUI
        self.root = Tk()
        self.root.title('Bank Registration')

        self.root.maxsize(300, 500)
        self.root.minsize(300, 500)
        self.root.configure(background='#2906A8')

        self.label1 = Label(self.root, text="My Bank", bg='#2906A8', fg='#ffffff')
        self.label1.pack(pady=(10, 10))
        self.label1.configure(font=('Verdana', 22, 'bold'))




        self.load_reg_gui()



    
    def load_reg_gui(self):
        self.clear_gui()
        self.label1 = Label(self.root, text="My Bank", bg='#2906A8', fg='#ffffff')
        self.label1.pack(pady=(10, 10))
        self.label1.configure(font=('Verdana', 22, 'bold'))

        self.label2 = Label(self.root, text="SignUp Here", bg='#2906A8', fg='#ffffff')
        self.label2.pack(pady=(10, 10))
        self.label2.configure(font=('Verdana', 12, 'italic'))

        self.name_input = Entry(self.root)
        self.name_input.insert(0, 'Type your name')
        self.name_input.pack(pady=(20, 10), ipadx=80, ipady=10)



        self.account_input = Entry(self.root)
        self.account_input.insert(0, 'Type your 5 digit account number')
        self.account_input.pack(pady=(20, 10), ipadx=80, ipady=10)

        self.password_input = Entry(self.root)
        self.password_input.insert(0, 'Set a Password')
        self.password_input.pack(pady=(10, 10), ipadx=80, ipady=10)


        self.reg_btn = Button(self.root,text='Sign Up',bg='#ffffff',width=30,height=2,command=lambda: self.perform_reg())
        self.reg_btn.pack(pady=(20,20))
        self.reg_btn.configure(font=('Verdana',10))

        self.label3 = Label(self.root, text="Already a member?", bg='#2906A8', fg='#ffffff')
        self.label3.pack(pady=(10, 10))
        self.label3.configure(font=('Verdana', 8, 'italic'))

        self.login_btn = Button(self.root, text='Login', bg='#ffffff', width=20, height=2,command=lambda: self.load_login_gui())
        self.login_btn.pack(pady=(0, 20))
        self.login_btn.configure(font=('Verdana', 8))

        self.root.mainloop()
    def clear_gui(self,i=0):
        for i in self.root.pack_slaves()[i:]:
            i.destroy()



    def load_header_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Check Balance",command=lambda:self.check_balance())

        filemenu.add_command(label="Deposit ",command=lambda:self.deposit())
        filemenu.add_command(label="Withdrawl",command=lambda:self.withdrawl())
        filemenu.add_command(label="Log out",command=lambda:self.logout())
        menubar.add_cascade(label="Options",menu=filemenu)

        self.root.config(menu=menubar)

    def withdrawl(self):
        self.clear_gui()


        self.take_cash_input = Entry(self.root)
        self.take_cash_input.insert(0, 'Enter withdrawl  ammount')
        self.take_cash_input.pack(pady=(20, 10), ipadx=80, ipady=10)

        self.confirm_btn = Button(self.root, text='Confirm', bg='#ffffff', width=20, height=2,command=lambda:self.confirm_withdrawl())
        self.confirm_btn.pack(pady=(0, 20))
        self.confirm_btn.configure(font=('Verdana', 8))
        self.cancel_btn = Button(self.root, text='Cancel', bg='#ffffff', width=20, height=2,command=lambda:self.load_profile_gui())
        self.cancel_btn.pack(pady=(0, 20))
        self.cancel_btn.configure(font=('Verdana', 8))

    def confirm_withdrawl(self):
        data=self.cd.fetch_capital(self.user_id)
        account_id = data[0][0]
        capital = data[0][4]
        take_cash=int(self.take_cash_input.get())
        if data[0][4]<take_cash:
            messagebox.showerror("My Bank", "Insufficient ammont in your account")

        else:
            capital=capital-take_cash
            response1 = self.cd.store_capital(capital, account_id)
            if response1 == 1:
                print("ammount withdrawl successful")
                messagebox.showinfo("My Bank", "ammount withdrawl Successful")

            else:
                print("ammount withdrawl faild")
                messagebox.showerror("My Bank", "Some error occured")


    def check_balance(self):
        self.clear_gui()
        data=self.cd.fetch_capital(self.user_id)
        if data!=0:
            self.label2 = Label(self.root, text="Your total balance {}".format(data[0][4]), bg='#2906A8', fg='#ffffff')
            self.label2.pack(pady=(10, 10))
            self.label2.configure(font=('Verdana', 13))
        else:
            messagebox.showerror("My Bank", "Some error occured")

    def deposit(self):
        self.clear_gui()

        self.depo_input = Entry(self.root)
        self.depo_input.insert(0, 'Deposit Your ammount')
        self.depo_input.pack(pady=(20, 10), ipadx=80, ipady=10)

        self.confirm_btn = Button(self.root, text='Confirm', bg='#ffffff', width=20, height=2,command=lambda:self.confirm_ammount())
        self.confirm_btn.pack(pady=(0, 20))
        self.confirm_btn.configure(font=('Verdana', 8))
        self.cancel_btn = Button(self.root, text='Cancel', bg='#ffffff', width=20, height=2,command=lambda:self.load_profile_gui())
        self.cancel_btn.pack(pady=(0, 20))
        self.cancel_btn.configure(font=('Verdana', 8))

    def confirm_ammount(self):
        capital=int(self.depo_input.get())
        data = self.cd.fetch_capital(self.user_id)
        account_id=data[0][0]
        previous_balance=data[0][4]
        capital=capital+previous_balance

        response1 = self.cd.store_capital(capital,account_id)
        if response1 == 1:
            print("ammount deposit successful")
            messagebox.showinfo("My Bank", "ammount deposit Successful")

        else:
            print("ammount deposit faild")
            messagebox.showerror("My Bank", "Some error occured")

    def load_profile_gui(self):
        self.clear_gui(0)
        self.load_header_menu()
        data=self.cd.fetch_user_data(self.user_id)
        if data != 0:
            self.label2 = Label(self.root, text="Hello {}".format(data[0][1]), bg='#2906A8', fg='#ffffff')
            self.label2.pack(pady=(10, 10))
            self.label2.configure(font=('Verdana', 16))
    def load_login_gui(self):
        self.clear_gui()
        self.root.config(menu="")
        self.label1 = Label(self.root, text="My Bank", bg='#2906A8', fg='#ffffff')
        self.label1.pack(pady=(10, 10))
        self.label1.configure(font=('Verdana', 22, 'bold'))

        self.label4 = Label(self.root, text="Login Here", bg='#2906A8', fg='#ffffff')
        self.label4.pack(pady=(10, 10))
        self.label4.configure(font=('Verdana', 12, 'italic'))

        self.account_input = Entry(self.root)
        self.account_input.insert(0, 'Type your 5 digit account number')
        self.account_input.pack(pady=(20, 10), ipadx=80, ipady=10)

        self.password_input = Entry(self.root)
        self.password_input.insert(0, 'Enter your Password')
        self.password_input.pack(pady=(10, 10), ipadx=80, ipady=10)


        self.go_log_btn = Button(self.root,text='Log in',bg='#ffffff',width=30,height=2,command=lambda: self.perform_log())
        self.go_log_btn.pack(pady=(20,20))
        self.go_log_btn.configure(font=('Verdana',10))

        self.label5 = Label(self.root, text="NOt a member?", bg='#2906A8', fg='#ffffff')
        self.label5.pack(pady=(10, 10))
        self.label5.configure(font=('Verdana', 8, 'italic'))

        self.Signup_btn = Button(self.root, text='Sign up', bg='#ffffff', width=20, height=2,
                                command=lambda: self.load_reg_gui())
        self.Signup_btn.pack(pady=(0, 20))
        self.Signup_btn.configure(font=('Verdana', 8))


    def perform_log(self):
        store_account_no = self.account_input.get()
        store_account_no = store_account_no[0:5]
        store_password = self.password_input.get()
        data=self.cd.login_user( store_account_no,store_password)
        if data == 0:
            messagebox.showerror("My Bank", "Some error occured")
        else:
            if len(data) == 0:
                messagebox.showerror("My Bank", "Incorrect account no/password")
            else:

                self.user_id = data[0][0]

                self.load_profile_gui()


    def perform_reg(self):
        store_name=self.name_input.get()
        store_account_no=self.account_input.get()
        store_account_no=store_account_no[0:5]
        store_password=self.password_input.get()

        response = self.cd.register_user(store_name,store_account_no,store_password)
        if response == 1:
            print("Reg successful")
            messagebox.showinfo("My Bank", "Registration Successful")

        else:
            print("reg faild")
            messagebox.showerror("My Bank", "Some error occured")

    def logout(self):

        self.user_id = None
        self.clear_gui()
        self.load_login_gui()










obj = My_bank()
