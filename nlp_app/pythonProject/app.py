from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API


class NLPApp:
    def __init__(self):
        # create db object
        self.db = Database()
        self.api_obj = API()

        # to load login gui
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('300x500')
        self.root.configure(bg='#067D74')
        self.login_gui()


        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text="NLP Application",bg='#067D74',fg='yellow')
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',20,'bold'))

        label1 = Label(self.root,text="Enter your email",bg='#067D74',fg='black')
        label1.pack(pady=(15,15))
        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter your password",bg='#067D74',fg='black')
        label2.pack(pady=(15,15))
        self.password_input = Entry(self.root,width=35,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        login_bttn = Button(self.root,text='Login',width=15,height=2,command=self.perform_login)
        login_bttn.pack(pady=(15,15))

        label3 = Label(self.root,text="Not a member yet?..",bg='#067D74',fg='black')
        label3.pack(pady=(15,15))

        register_bttn = Button(self.root,text='Register Now!',width=13,height=2,command=self.register_gui)
        register_bttn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text="NLP Application",bg='#067D74',fg='yellow')
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',20,'bold'))

        label0 = Label(self.root,text="Enter your name",bg='#067D74',fg='black')
        label0.pack(pady=(10,10))
        self.name_input = Entry(self.root,width=35)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text="Enter your email",bg='#067D74',fg='black')
        label1.pack(pady=(10,10))
        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text="Enter your password",bg='#067D74',fg='black')
        label2.pack(pady=(10,10))
        self.password_input = Entry(self.root,width=35,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        register_bttn = Button(self.root,text='Register',width=15,height=2,command=self.perform_registration)
        register_bttn.pack(pady=(15,15))

        label3 = Label(self.root,text="Already a member?",bg='#067D74',fg='black')
        label3.pack(pady=(10,10))

        redirect_bttn = Button(self.root,text='Login Now!',width=13,height=2,command=self.login_gui)
        redirect_bttn.pack(pady=(10,10))

    def clear(self):
        # clear the exising gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fletch data from gui
        name = self.name_input.get() # to fletch the data from name_input from registration_gui()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.db.add_data(name,email,password) # to store the response in a variable
        if response:
            messagebox.showinfo('Registration successful!','You can login now')
        else:
            messagebox.showerror('Email exits!','Try using a different email')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.db.search_login(email,password) # to store the response in a variable
        if response:
            messagebox.showinfo('Successful!','Welcome')
            self.home_gui() # to redirect the user to home wire frame
        else:
            messagebox.showerror('Error','Incorrect email or password')

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text="Home",bg='#067D74',fg='yellow')
        heading.pack(pady=(25,25))
        heading.configure(font=('verdana',20,'bold'))
        sentiment_bttn = Button(self.root, text='Sentiment Analysis', width=20, height=3, command=self.sentiment_gui)
        sentiment_bttn.pack(pady=(10, 10))

        ner_bttn = Button(self.root, text='NER', width=20, height=3, command=self.login_gui)
        ner_bttn.pack(pady=(10, 10))
        emotion_bttn = Button(self.root, text='Emotion Detection', width=20, height=3, command=self.login_gui)
        emotion_bttn.pack(pady=(10, 10))

        logout_bttn = Button(self.root, text='Log out', width=13, height=2, command=self.login_gui)
        logout_bttn.pack(pady=(10, 10))
        #messagebox.showinfo('Logout successfully!', 'Login again')

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="Sentiment Analysis", bg='#067D74', fg='yellow')
        heading.pack(pady=(25, 25))
        heading.configure(font=('verdana', 20, 'bold'))

        label1 = Label(self.root, text="Enter the text", bg='#067D74', fg='black')
        label1.pack(pady=(10, 10))
        self.sentiment_input = Entry(self.root, width=35)
        self.sentiment_input.pack(pady=(5, 10), ipady=10)

        sentiment_bttn = Button(self.root, text='Analyze Sentiment', width=20, height=3, command=self.do_sentiment_analysis)
        sentiment_bttn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="", bg='#067D74', fg='orange')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 10, 'bold'))

        goback_bttn = Button(self.root, text='Go back', width=15, height=2, command=self.home_gui)
        goback_bttn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        print(text)
        result = self.api_obj.sentiment_analysis(text)
        self.sentiment_result['text'] = result








nlp = NLPApp()

