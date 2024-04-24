        self.root.destroy()
        self.root = customtkinter.CTk() 
        self.root.title("Cookie's English🍪")

        x_position = (self.screen_width - self.window_width) // 2
        y_position = (self.screen_height - self.window_height) // 2

        self.root.geometry(f"{self.window_width}x{self.window_height}+{x_position}+{y_position}")

        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)  # Add padding to the frame

        word_ind = self.get_word()

        # Configure fonts and colors for labels
        label_font = ("Arial", 14, "bold")
        label_bg = "#f0f0f0"  # Light gray background color

        word = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 0]}', font=label_font)
        # Filter out unsupported arguments before configuring the widget
        supported_word_args = {k: v for k, v in kwargs_dict.items() if k in word.keys()}
        word.config(**supported_word_args)  # Apply supported arguments
        word.grid(row=0, column=0, sticky='e', padx=10, pady=10)  # Add padding to the labels

        translation = customtkinter.CTkLabel(frame, text=f'{self.df.iat[word_ind, 1]}', font=label_font)
        # Filter out unsupported arguments before configuring the widget
        supported_translation_args = {k: v for k, v in kwargs_dict.items() if k in translation.keys()}
        translation.config(**supported_translation_args)  # Apply supported arguments
        translation.grid(row=0, column=2, sticky='e', padx=10, pady=10)

        got_it_button = customtkinter.CTkButton(frame, text="Got It!", command=self.start_timer)
        # Filter out unsupported arguments before configuring the widget
        supported_button_args = {k: v for k, v in kwargs_dict.items() if k in got_it_button.keys()}
        got_it_button.config(**supported_button_args)  # Apply supported arguments
        got_it_button.grid(column=1, row=3, pady=20)  # Add padding to the button

        self.root.mainloop()