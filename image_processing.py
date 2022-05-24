import cv2
from PIL import Image
from os import path

def enc():
    print("ENCRypION")
    #if already encrypted dont encrypt again as it will actually decrypt it
    try:
        im = Image.open(Path)
        file = open(Path,'rb')
        image = file.read()
        file.close()
        image2 = bytearray(image)
        key = int(input("Enter the Encryption key = "))
        
        for i,j in enumerate(image2):
            image2[i] = j^key
            
        file = open(Path,'wb')
        file.write(image2)
        file.close()
    except:
        print("Image is encrypted hence not in displaying format")
        
    #I just want to display the image or at least not any adrupt stop so I will try a 
    #try catch block 
    
def dec():
    print("DeCRypION")
    file = open(Path,'rb')
    image = file.read()
    file.close()
    image2 = bytearray(image)
    key = int(input("Enter the Encryption key = "))
    
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
   
    
#Enter the path
Path = input('Enter the path:')
if(path.exists(Path)):
    if Path.lower().endswith(('.png', '.jpg', '.jpeg')):
        enc();
        doyou = int(input('Do you wanna decrypt?=(0/1)'))
        if doyou:
            dec();#71
    else:
        print("please provide the image path (jpg,png,jpeg)")
else:
    print("There is not any file at this path")
