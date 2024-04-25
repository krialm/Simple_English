import pandas as pd
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import customtkinter
import time
from random import randint
import os
import json


class User:

    def __init__(self):

        customtkinter.set_appearance_mode("Dark")

        self.df = pd.DataFrame()
        self.current_path = ''
        self.timer = 5
        self.words_indexes = []
        self.window_width = 400
        self.window_height = 160
        self.is_new_user = True 
        self.user_data_path = '/Users/krialm/Documents/GitHub/Simple_English/user_data.json'
        files = os.listdir('/Users/krialm/Documents/GitHub/Simple_English/topics')

        self.topics = [x.replace('.xlsx', '') for x in files ]


        if not os.path.exists(self.user_data_path):
            self.setting_window()
        else:
            self.is_new_user = False
            user_data = self.load_user_data(self.user_data_path)
            self.topic = user_data['topic']
            self.timer = user_data['timer']
            self.geometry = user_data['geometry']
            self.start_app()
            

    def load_user_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return data

    def create_user(self):
        with open(self.user_data_path, "w") as file:
            json.dump({'topic': self.topics_var.get(), 'timer': self.timer.get(), 'geometry': self.geometry}, file)
        self.root.destroy()
        self.start_app()

    # creating a setting window
    def setting_window(self):

        # creating a window
        self.root = customtkinter.CTk() 
        self.root.title("Cookie's english🍪")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x_position = (self.screen_width - self.window_width) // 2
        self.y_position = (self.screen_height - self.window_height) // 2
        
        self.geometry = f"{self.window_width}x{self.window_height}+{self.x_position}+{self.y_position}"

        self.root.geometry(self.geometry)

        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill='both', expand=True)



        def getting_path():
            # selecting path to csv file with data
            self.current_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("xlsx files", "*.xlsx"), ('CSV files', '.csv'), ("all files", "*.*")))
            if '.csv' in self.current_path:
                self.df = pd.read_csv(self.current_path)
            elif '.xlsx' in self.current_path:
                self.df = pd.read_excel(self.current_path)
            print(self.current_path)
            print(self.df)
            self.filename_path.set(self.current_path)
        


        self.filename_path = StringVar(value=self.current_path)

        self.timer = StringVar(value=self.timer)

        self.topics_var = StringVar(value=self.topics[0])   


        combobox = customtkinter.CTkComboBox(frame, variable=self.topics_var, values=self.topics)
        combobox.grid(row=2, column=0,  columnspan = 1,sticky=W)
 

        path_entry = customtkinter.CTkEntry(frame, width=270, textvariable=self.filename_path)
        path_entry.grid(row=1, column=0,  columnspan = 2,sticky=E)

        timer_entry = customtkinter.CTkEntry(frame, width=50, textvariable=self.timer)
        timer_entry.grid(row=2, column=0,  columnspan = 2,sticky=E)


        path_label = customtkinter.CTkLabel(frame, text='Path to .xlsx or .csv file')
        path_label.grid(row=0, column=0)
        timer_label = customtkinter.CTkLabel(frame, text='Timer (in min)')
        timer_label.grid(row=2, column=2)

        customtkinter.CTkButton(frame, text="Browse", command=getting_path).grid(column=2, row=1)
        customtkinter.CTkButton(frame, text="Continue", command=self.create_user).grid(column=1, row=3)
        self.root.mainloop()

    def start_timer(self):

        self.root.destroy()
        self.root = customtkinter.CTk() 
        if self.is_new_user: 
            time.sleep(int(self.timer.get()))
        else:
            time.sleep(int(self.timer))
        self.start_app()

    def get_word(self):
        
        word_ind = randint(0, len(self.df))
        while True:
            if word_ind not in self.words_indexes:
                self.words_indexes.append(word_ind)
                return word_ind
            word_ind = randint(0, len(self.df))
        

    # @staticmethod
    # def from_dict(data):
    #     return UserData(data["name"], data["age"], data["email"], data["numbers"])

    # def save_user_data(user_data, filename):
    #     with open(filename, "w") as file:
    #         json.dump(user_data.to_dict(), file)

    # def load_user_data(filename):
    #     with open(filename, "r") as file:
    #         data = json.load(file)
    #         return UserData.from_dict(data)


    def start_app(self):


        self.root = customtkinter.CTk() 
        self.root.title("Cookie's English🍪")


        self.root.geometry(self.geometry)


        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)  # Add padding to the frame



        word_ind = self.get_word()

        # Configure fonts and colors for labels
        label_font = ("Arial", 14, "bold")

        word = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 0]}', font=label_font)

        word.grid(row=0, column=0, sticky='e', padx=10, pady=10)  # Add padding to the labels

        translation = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 1]}', font=label_font)

        translation.grid(row=0, column=2, sticky='e', padx=10, pady=10)

        got_it_button = customtkinter.CTkButton(frame, text="Got It!", command=self.start_timer)


        got_it_button.grid(column=1, row=3, pady=20)  # Add padding to the button

        self.root.mainloop()

if __name__ == '__main__':
    user = User()