from tkinter import *
import sys
import cv2
import pyrebase
from PIL import Image,ImageTk


def close(mywin):
    mywin.withdraw() # if you want to bring it back
    sys.exit()


def newwin(email,passw,path,tflag,dpath):

    dpathcop=dpath
    protopath = dpath[:-1] + '/' + 'MobileNetSSD_deploy.prototxt'
    modelpath=dpathcop[:-1] + '/' + 'MobileNetSSD_deploy.caffemodel'
    labels = ['airplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
              'car', 'cat', 'chair', 'cow', 'dining table', 'dog',
              'horse', 'motorbike', 'person', 'potted plant', 'sheep',
              'sofa', 'train', 'TV or monitor']
    blob_height = 300
    color_scale = 1.0 / 127.5
    average_color = (127.5, 127.5, 127.5)
    confidence_threshold = 0.5

    firebaseConfig = {
        'apiKey': "AIzaSyArzMBQu7zwf0jEqrhGn0FcszxpWasL374",
        'authDomain': "mobilenet-a25e6.firebaseapp.com",
        'databaseURL': "https://mobilenet-a25e6-default-rtdb.firebaseio.com/",
        'projectId': "mobilenet-a25e6",
        'storageBucket': "mobilenet-a25e6.appspot.com",
        'messagingSenderId': "768549213067",
        'appId': "1:768549213067:web:7f369d75a6a3aa6dddd58e"
    }
    firebase_obj = pyrebase.initialize_app(firebaseConfig)
    storage = firebase_obj.storage()
    storage.child("/mobilenet_ssd/MobileNetSSD_deploy.prototxt").download(protopath)
    storage.child("/mobilenet_ssd/MobileNetSSD_deploy.caffemodel").download(modelpath)

    model = cv2.dnn.readNetFromCaffe(protopath,
                                     modelpath)
    print('done')


    auth = firebase_obj.auth()
    if tflag==0:
        auth.create_user_with_email_and_password(email, passw)
    elif tflag==1:
        auth.sign_in_with_email_and_password(email,passw)


    path_str=str(path)
    path_str=path_str[-4:]






    mywin=Tk()
    mytext="Logged in as ",email


    mywin.attributes("-fullscreen", True)
    escape_hint = Label(mywin, text="press escape to exit").place(x=1300, y=30)
    name=Label(mywin,text=mytext,font=("Ariel",13)).place(x=510,y=100)
    if (path_str == '.jpg' or path_str == '.png'):
        img = cv2.imread(path)
        (h, w) = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
        model.setInput(blob)
        det = model.forward()
        for i in det[0, 0]:
            conf = i[2]
            x0, y0, x1, y1 = (i[3:7] * [w, h, w, h]).astype(int)
            id = int(i[1])
            label = labels[id - 1]
            text = '%s (%.1f%%)' % (label, conf * 100.0)
            cv2.putText(img, text, (x0, y0 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.rectangle(img, (x0, y0), (x1, y1), (255, 0, 0), 2)
        cv2.imshow('r',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






    mywin.bind("<Escape>", lambda x: close(mywin))

    mywin.mainloop()