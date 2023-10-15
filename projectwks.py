import random
import string
from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Password Generator")
root.geometry("280x190") # window size, just big enough to read the password generator. 


# this def will make a random password, but leave out uncommon password punc.s
# that are not allowed sometimes. 

def getpsswd(lenghth: int = 12):

    remove = string.punctuation
    remove = remove.replace(".", "")
    remove = remove.replace("'", "")
    remove = remove.replace(";", "") 
    remove = remove.replace(",", "")
    remove = remove.replace("{", "")
    remove = remove.replace("}", "")

    
    abc = string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + remove   
    psswd = "".join(random.choice(abc) for x in range(lenghth))

    return psswd

psswd = getpsswd()

# below is connected to the generate button to generate random passwords
def getxt():
    box["text"] = getpsswd()
    
# below is a def that will be used to copy the password to clipboard,
# from the getxt() then display an alert when it is copied
def popup():
    messagebox.showinfo("Alert", "Copied to clipboard")
    root.clipboard_clear()
    root.clipboard_append(box["text"])
    root.update()
    
#create a button
gen = Button(root, text="Generate Password", padx=7, pady=7, fg="green", bg="black", command=getxt) # pad x and y sizes the button, fg and bg are button colors
# button goes on the window that was made
gen.grid(row=0, column=2)
# text box label 
box = Label(root, width=16, height=2, bg="orange")
box.grid(row=3, column=2)
# another button
copiibut = Button(root, text="Copy to Clipboard", padx=7, pady=7, fg="green", bg="black", command=popup)# might have to change the clipboard area to ()
copiibut.grid(row=4, column=2)


root.mainloop()