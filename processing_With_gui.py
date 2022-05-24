from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image
root= Tk()
root.geometry("500x500")

def encrypt():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        Path = file1.name
        key = entry1.get(1.0,END)
        key =int(key)
        print("ENCRypION")
    #if already encrypted dont encrypt again as it will actually decrypt it
        try:
            im = Image.open(Path)
            file = open(Path,'rb')
            image = file.read()
            file.close()
            image2 = bytearray(image)
            for i,j in enumerate(image2):
                image2[i] = j^key 
            file = open(Path,'wb')
            file.write(image2)
            file.close()
        except:
            print("Image is encrypted hence not in displaying format")

def decrypt():
     file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
     if file1 is not None:
        Path = file1.name
        key = entry1.get(1.0,END)
        key =int(key)
        print("DecrypION")
        file = open(Path,'rb')
        image = file.read()
        file.close()
        image2 = bytearray(image)
        for i,j in enumerate(image2):
            image2[i] = j^key 
        file = open(Path,'wb')
        file.write(image2)
        file.close()
        try:
            showit = cv2.imread(Path)
        except:
            print("Image is encrypted hence not in displaying format")
        else:#else if no errors we will show and display image
            print("Image is shown")   
            cv2.imshow('This is Decrypted',showit)
            cv2.waitKey(5000)#this will allow the image to be displayed for 5000 msec
            cv2.destroyAllWindows()# after that it will be destroyed
   
b1 = Button(root,text = 'encrypt',command = encrypt)
b1.place(x=150,y=200)

b2 = Button(root,text = 'Decrypt',command = decrypt)
b2.place(x=250,y=200)

entry1 = Text(root,height=1,width=10)
entry1.place(x=175,y=250)

root.mainloop()