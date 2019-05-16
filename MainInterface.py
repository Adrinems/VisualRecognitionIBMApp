from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import cv2
import VisualRecognitionAPI


initial_image = "/media/adriana/1C5E88DB2130A7CC/maestria/2dosemestre/Seminario/no-image.png"
updated_image = False

WIDTH, HEIGHT = 500, 480


def select_image():
    # grab a reference to the image panels
    global panelLeft, panelB, path, updated_image
    flag = False
    # open a file chooser dialog and allow the user to select an input
    # image
    path = askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        #image = cv2.imread(path)
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        #image = Image.fromarray(image)
        # and then to ImageTk format
        image = Image.open(path).resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        panelLeft.configure(image=image)
        panelLeft.image = image
        updated_image = True


def send_image():
    if updated_image == False:
        messagebox.showerror("ERROR", "You must select an image first!")
    else:
       VisualRecognitionAPI.sendData(path)
       value_class_lbl.configure(text=VisualRecognitionAPI.sel_class)
       value_score_lbl.configure(text=VisualRecognitionAPI.real_score)

        # initialize the window toolkit along with the two image panels



root = Tk()
root.title("Demo Visual Recognition")
root.resizable(False,False)
#root.iconbitmap("")
root.geometry("813x500")

leftside = Label(root, bg="gray")
rightside = Frame(root, bg="black")


leftside.grid(row=0,column=0 )
rightside.grid(row=0, column=1, sticky=N+S+W+E )


panelLeft = None
image = Image.open(initial_image).resize((WIDTH, HEIGHT), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
panelLeft = Label(leftside, image=image)
panelLeft.image = image
panelLeft.pack(side="left", padx=8, pady=8)

#button the GUI
labelfont1 = ('times', 14, 'bold')
reslbl = Label(rightside, text="DEMO \n VISUAL RECOGNITION:", bg="black", fg="white")
reslbl.grid(column=1, row=0)
reslbl.config(font=labelfont1)


btn = Button(rightside, text="Select an image", command=select_image, justify=CENTER)
btn.grid(column=1, row=1, pady=15)
btn2 = Button(rightside, text="Send image", command=send_image, padx=20)
btn2.grid(column=1, row=2, pady=15)
labelfont1 = ('times', 20, 'bold')
reslbl = Label(rightside, text="RESULTS:", bg="black", fg="white", padx=22)
reslbl.grid(column=1, row=3, pady=15)
reslbl.config(font=labelfont1)

labelfont = ('times', 18, 'bold')

classlbl = Label(rightside, text="Class:", bg="black", fg="white" )
classlbl.grid(column=0, row=5)
classlbl.config(font=labelfont)
value_class_lbl = Label(rightside, text="---", bg="black", fg="white")
value_class_lbl.grid(column=1, row=5, padx=20)
value_class_lbl.config(font=labelfont)
scorelbl = Label(rightside, text="Score:", bg="black", fg="white")
scorelbl.grid(column=0, row=6)
scorelbl.config(font=labelfont)
value_score_lbl = Label(rightside, text="0.0", bg="black", fg="white")
value_score_lbl.grid(column=1, row=6)
value_score_lbl.config(font=labelfont)



    # kick off the GUI
root.mainloop()