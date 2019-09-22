import tkinter


class CelsiusConvertGUI:
    
    def __init__(self):
        # Call the module
        self.calc_window = tkinter.Tk()
        
        # Make a title at the top of window
        self.calc_window.title('Celsius to Fahrenheit Converter')
        self.canvas = tkinter.Canvas(self.calc_window, width=350, height=10)
        self.canvas.pack()
    
        # Frames
        self.top_frame = tkinter.Frame(self.calc_window)
        self.mid_frame = tkinter.Frame(self.calc_window)
        self.bottom_frame = tkinter.Frame(self.calc_window)
        
        # Widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter the Celsius Temperature: ')
        self.celsius_entry = tkinter.Entry(self.top_frame,
                                           width=10)
        
        # Pack top frame
        self.prompt_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        # Widgets for middle frame
        self.convert_fahrenheit = tkinter.Label(self.mid_frame,
                                                text='Fahrenheit Converted:')

        # Store empty string
        self.value = tkinter.StringVar()

        # Label for stringvar object
        self.fahren_label = tkinter.Label(self.mid_frame,
                                          textvariable=self.value)

        # Pack middle frame
        self.convert_fahrenheit.pack(side='left')
        self.fahren_label.pack(side='left')

        # Need to add button for conversion
        self.convert = tkinter.Button(self.bottom_frame,
                                      text='Convert!',
                                      command=self.conv_cel_to_faren)
        self.close_window = tkinter.Button(self.bottom_frame,
                                           text='Quit!',
                                           command=self.calc_window.destroy)

        # Pack buttons
        self.convert.pack(side='left')
        self.close_window.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # Refreshes main tk screen
        self.calc_window.mainloop()

    def conv_cel_to_faren(self):
        """
        Converts a given number in celsius
        to its fahrenheit equivalent.
        """
        # Gets value entered by user.
        celsius = float(self.celsius_entry.get())

        # Store calculation into a variable
        conversion = celsius * (9/5) + 32

        # Assign conversion to the stringvar object
        self.value.set(format(conversion, '.2f'))


# Create an instance
celsius_conversion = CelsiusConvertGUI()
