from cgitb import text
from fileinput import filename
from logging import root
from tkinter import *
import shutil
import os
from tkinter import font
from click import command
import easygui
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def open_window():
    read=easygui.fileopenbox()
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

def copy_file():
    file_to_copy = fd.askopenfilename(title="Choose a file of any type", filetypes=[("All files","*.*")])
    dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title='File Copied!', message="our file has been copied!")
    except:
        mb.showerror(title="Error!", message="Unable to copy your file to teh requestion location")

def delete_file():
    file = fd.askopenfile(title="Chose a file to delete", filetypes=[("All Files","*.*")])
    os.remove(os.path.abspath(file))
    mb.showinfo(title="File Deleted", message="File has been Deleted.")

def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")

def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)

def delete_folder():
    folder_to_delete = fd.askdirectory(title="Choose a folder to delete")
    os.rmdir(folder_to_delete)
    mb.showinfo("Folder Deleted", "Your folder has been deleted")

def move_folder():
    folder_to_move = fd.askdirectory(title="Select te folder you wan to move")
    mb.showinfo(messgae="You just selected the folder to move, now select the desired destionation where you want to move the folder to")
    destination = fd.askdirectory(title="Where to move the folder to")

    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo("Folder moved", "Your folder has been move to the location given by you.")
    except:
        mb.showerror("Error","Cannot move your folder. Please Make sure that the destination exists.")

def list_files_in_folder():
    folder = fd.askdirectory(title="Select the folder whose files you want to lsit")

    files = os.listdir(os.path.abspath(folder))

    list_files_wn = Toplevel(root)
    list_files_wn.title(f"Files in {folder}")
    list_files_wn.geometry("250x250")
    list_files_wn.resizable(0,0)

    listbox = Listbox(list_files_wn, selectbackground="SteelBlue", font=("Georgia",10))
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT,fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)
    i=0
    while i<len(files):
        listbox.insert(END, files[i])
        i+=1


title = 'File Manager'
background = 'Yellow'
button_font = ("Times New Roman", 13)
button_background = 'Turquoise'

#WINDOW CREATION
root = Tk()
root.title(title)
root.geometry('250x400')
root.resizable(0, 0)
root.config(bg=background)

# Creating and placing the components in the window
Label(root, text=title, font=("system", 15), bg=background, wraplength=250).place(x=20, y=0)

Button(root, text='Open a file', width=20, font=button_font, bg=button_background, command=open_file).place(x=30, y=50)

Button(root, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).place(x=30, y=90)

Button(root, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).place(x=30, y=130)

Button(root, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).place(x=30, y=170)

Button(root, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).place(x=30, y=210)

Button(root, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).place(x=30, y=250)

Button(root, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).place(x=30, y=290)

Button(root, text='List all files in a folder', width=20, font=button_font, bg=button_background,command=list_files_in_folder).place(x=30, y=330)

# Finalizing the window
root.update()
root.mainloop()