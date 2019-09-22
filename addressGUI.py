import tkinter
import tkinter.messagebox

stored_info = '''
       John Doe
  555 Generic Street
Where ever, FL 55555
           '''


# Message box
def display_info():
    msg_box = tkinter.messagebox.showinfo(title='Address', message=stored_info)


# Call function for main window.
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=300, height=18)
canvas.pack()

# Title
window.title('Address Display')

# Frames
window_top = tkinter.Frame(window)
window_bot = tkinter.Frame(window)

# Label
addy_label = tkinter.Label(window_top,
                           text='Click to show the stored address!')

# Pack top frame
addy_label.pack(side='left')

# Bottom Frame Widget
show_addy = tkinter.Button(window_bot,
                           text='Show Info!',
                           command=display_info)
close_window = tkinter.Button(window_bot,
                              text='Quit',
                              command=window.destroy)

# Pack buttons
show_addy.pack(side='left')
close_window.pack(side='left')

# Pack Frames
window_top.pack()
window_bot.pack()

# Screen refresh
window.mainloop()
