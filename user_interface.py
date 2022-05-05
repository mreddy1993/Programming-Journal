import tkinter as tk

def main_page():
    window = tk.Tk()
    frame_welcome = tk.Frame()
    frame_instruction = tk.Frame()
    frame_option_one = tk.Frame()
    frame_option_two = tk.Frame()
    frame_option_three = tk.Frame()

    welcome_label = tk.Label(
    master= frame_welcome,
    text = "Welcome to the Journal",
    foreground="black",
    )

    instruction_label = tk.Label(
    master= frame_instruction,
    text = "Please Select an Option Below",
    foreground = "black",
    )

    option_one = tk.Button(
    master= frame_option_one,
    text = "1)Add a New Entry",
    width = "30",
    height = "10",
    fg = "black",
    command = lambda:[window.destroy, add_entry()]
    )

    option_two = tk.Button(
    master= frame_option_two,
    text = "2)View Existing Entries",
    width = "30",
    height = "10",
    fg = "black"
    )

    option_three = tk.Button(
    master= frame_option_three,
    text = "3)Exit",
    width = "30",
    height = "10",
    fg = "black",
    command = window.destroy
    )

    welcome_label.pack()
    frame_welcome.pack()

    instruction_label.pack()
    frame_instruction.pack()

    option_one.pack()
    frame_option_one.pack()

    option_two.pack()
    frame_option_two.pack()

    option_three.pack()
    frame_option_three.pack()

    window.mainloop()


def add_entry():
    window = tk.Tk()
    
    entry_box = tk.StringVar()
    title_entry = tk.StringVar()
    entry = ""
    title = ""
    data = list()
    def getText(entry,title):
        entry = entry_box.get("1.0", "end")
        title = title_entry.get()
        data.append(title)
        data.append(entry)
        return data
    
        
    frame_title_label = tk.Frame()
    frame_entry = tk.Frame()
    
    title_label = tk.Label(
    master = frame_title_label,
    text = "Title",
    foreground = "black",
    )

    entry_label = tk.Label(
    master = frame_entry,
    text = "Entry Text",
    foreground = "black"
    )

    entry_box = tk.Text()
    title_entry = tk.Entry(window, textvariable=title_entry)

    save_button = tk.Button(
    text = "Save",
    command = lambda:[getText(entry,title), window.destroy]
    )


    title_label.pack()
    frame_title_label.pack()
    title_entry.pack()
    entry_label.pack()
    frame_entry.pack()
    entry_box.pack()
    save_button.pack()

    window.mainloop()
    

    