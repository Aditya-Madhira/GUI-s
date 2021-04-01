import tkinter as tk
from tkinter import ttk
import sys
import pyrebase
from second_win import *



LARGEFONT = ("Verdana", 35)
def exit(master):
    master.withdraw()  # if you want to bring it back
    sys.exit()





class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)
        self.bind("<Escape>",lambda x:exit(self))



        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Mobilenet_ssd", font=LARGEFONT).place(x=560,y=55)
        label = ttk.Label(self, text="V1.0(only images supported)", font=LARGEFONT).place(x=560, y=55)
        lab_2=ttk.Label(self, text="press Escape to exit").place(x=1200,y=30)

        # putting the grid in its place by using
        # grid


        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(Page1)).place(x=600,y=400)

        # putting the button in its place by
        # using grid


        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Sign Up",
                             command=lambda: controller.show_frame(Page2)).place(x=800,y=400)

        # putting the button in its place by
        # using grid


    # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        emailvar = tk.StringVar()
        passvar=tk.StringVar()
        pathvar=tk.StringVar()
        downvar=tk.StringVar()
        example = '   example : c://users/aditya/desktop/img.jpg(do not use quotes or r) '
        downex = '   example : c://users/aditya/desktop(do not use quotes or r) '
        label = ttk.Label(self, text="Login", font=LARGEFONT).place(x=560,y=55)
        email_lab=ttk.Label(self, text="Email").place(x=560,y=180)
        pass_lab=ttk.Label(self, text="Password").place(x=560,y=340)
        email_inp=ttk.Entry(self,textvariable=emailvar,width=30).place(x=560,y=220)
        pass_inp=ttk.Entry(self,textvariable=passvar,width=30).place(x=560,y=370)
        path_inp=ttk.Entry(self,textvariable=pathvar,width=30).place(x=560,y=420)
        pathlab=ttk.Label(self, text="Before signing in ,enter path of img or video").place(x=560,y=400)
        pathlab_2 = ttk.Label(self, text=example).place(x=890, y=400)
        down_inp = ttk.Entry(self, textvariable=downvar, width=30).place(x=560, y=530)
        downlab = ttk.Label(self, text="Pre trained model will be downloaded from firebase(backend),specify a directory to download").place(x=560, y=500)
        downlab_2 = ttk.Label(self, text=downex).place(x=890, y=500)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Login,,Wait 10 seconds after clicking",
                             command=lambda: newwin(emailvar.get(), passvar.get(), pathvar.get(), 1,downvar.get())).place(x=560,
                                                                                                            y=720)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

    # third window frame page2


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        emailvar = tk.StringVar()
        passvar=tk.StringVar()
        pathvar=tk.StringVar()
        downvar = tk.StringVar()
        example='   example : c://users/aditya/desktop/img.jpg(do not use quotes or r) '
        downex = '   example : c://users/aditya/desktop(do not use quotes or r) '

        label = ttk.Label(self, text="Sign Up", font=LARGEFONT).place(x=560,y=55)
        email_lab=ttk.Label(self, text="Email").place(x=560,y=180)
        pass_lab=ttk.Label(self, text="Password").place(x=560,y=340)
        email_inp=ttk.Entry(self,textvariable=emailvar,width=30).place(x=560,y=220)
        pass_inp=ttk.Entry(self,textvariable=passvar,width=30).place(x=560,y=370)
        path_inp=ttk.Entry(self,textvariable=pathvar,width=30).place(x=560,y=420)
        pathlab=ttk.Label(self, text="Before signing in ,enter path of img or video").place(x=560,y=400)
        pathlab_2 = ttk.Label(self, text=example).place(x=890, y=400)
        down_inp = ttk.Entry(self, textvariable=downvar, width=30).place(x=560, y=530)
        downlab = ttk.Label(self, text="Pre trained model will be downloaded from firebase(backend),specify a directory to download").place(x=560, y=500)
        downlab_2 = ttk.Label(self, text=downex).place(x=890, y=500)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="SignUp,,wait 10 seconds after clicking",command=lambda :newwin(emailvar.get(),passvar.get(),pathvar.get(),0,downvar.get())).place(x=560,y=720)

        # putting the button in its place by
        # using grid


        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

    # Driver Code


app = tkinterApp()
app.mainloop()
