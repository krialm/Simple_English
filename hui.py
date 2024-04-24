import pandas as pd
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import customtkinter
import time
from random import randrange
import os



class User():

    current_path = ''
    delay = 5

    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        self.setting_window()
        self.df = pd.DataFrame()

    # creating a setting window
    def setting_window(self):

        # creating a window
        root = customtkinter.CTk() 
        root.title("Cookie's english🍪")
        root.geometry("300x120+500+300")
        frame = customtkinter.CTkFrame(root, padding=10)
        frame.grid()

        def getting_path():
            # selecting path to csv file with data
            self.current_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
            self.df = pd.read_excel(self.current_path)
            print(self.current_path)
            print(self.df)
            filename_path.set(self.current_path)
        
        def save():
            self.delay = timer_entry.get()
            self.current_path = path_entry.get()
            
            root.destroy()


        # processing the received file
        filename_path = StringVar()
        filename_path.set(self.current_path)

        path_entry = customtkinter.CTkEntry(frame, width=18, textvariable=filename_path)
        path_entry.grid(row=1, column=0)

        delay = IntVar()
        delay.set(self.delay)
        timer_entry = customtkinter.CTkEntry(frame, width=8, textvariable=delay)
        timer_entry.grid(row=2, column=0)

        path_label = customtkinter.CTkLabel(frame, text='Path (xlsx or csv)')
        path_label.grid(row=0, column=0)
        timer_label = customtkinter.CTkLabel(frame, text='Timer (in min)')
        timer_label.grid(row=2, column=2)

        customtkinter.CTkButton(frame, text="Browse", command=getting_path).grid(column=2, row=1)
        customtkinter.CTkButton(frame, text="Save", command=save).grid(column=2, row=3)
        root.mainloop()

    def create_window_task(self):
        index = randrange(1,len(self.df))
        command = f'''
        osascript -e 'set theDialogText to "{self.df.at[index,'Words']}" & "      {self.df.at[index,'Translate']}"
        display dialog theDialogText'
         '''
        os.system(command)

if __name__ == '__main__':
    user = User()
    print(user.delay, user.current_path)
    user.create_window_task()