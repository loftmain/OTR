
from flask import Flask, request, render_template, redirect, session
import cv2
import numpy as np
import datetime

image = None

app = Flask(__name__)
app.secret_key = 'app secret key'

###################################################modules



def yellow(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (20,190, 50)
    upper = (30, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst


def darkyellow(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (20,130, 50)
    upper = (30, 190, 255)

    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
    
def red(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (170,110, 110)
    upper= (180, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
def orange(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (0,110, 190)
    upper = (20, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
def green(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (45,110, 110)
    upper= (80, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst


def darkgreen(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (30,110, 50)
    upper= (45, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
    
def blue(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (90,150, 110)
    upper= (110, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
def navy(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (110,110, 110)
    upper= (120, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst
    
def pink(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (160,110, 110)
    upper= (170, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst

def purple(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (130,110, 110)
    upper= (150, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst

def brown(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = (0,80, 80)
    upper= (13, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.medianBlur(mask, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)

    obj = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, obj, 1.0, 0.0)

    return dst


###########################################################apps

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    print(session['counter'])
    return render_template("index.html", ctx={"title":"Over the Rainbow"})


@app.route('/upload', methods=["POST"]) 
def upload():
    global image 
    f = request.files['file1']
    if f.filename == '':
        image = cv2.imread('./static/img/non.png')
        cv2.imwrite("./static/img/result.jpg", image)
        print(image.shape)

        return render_template("imageprocessing.html", ctx={"title": "Over the Rainbow"})


    else:
        filename = "./static/img/" + f.filename

        f.save(filename)
        image = cv2.imread(filename)
        cv2.imwrite("./static/img/result.jpg", image)
        print(image.shape)
    #     session["image"] = image

    # return redirect("/")
        return render_template("imageprocessing.html", ctx={"title":"Over the Rainbow"})

@app.route('/imageprocessing')
def imageprocss():
    global image
    
    method = request.args.get("method")

    if method == "original":
        dst = image
        cv2.imwrite('./static/img/result.jpg', dst)

    if method == "red":
        dst = red(image)
        cv2.imwrite('./static/img/result.jpg', dst)
        
    if method == "orange":
        dst = orange(image)
        cv2.imwrite('./static/img/result.jpg', dst)

    if method == "yellow":
        dst = yellow(image)
        cv2.imwrite('./static/img/result.jpg', dst)
        
    if method == "darkyellow":
        dst = darkyellow(image)
        cv2.imwrite('./static/img/result.jpg', dst)
    
    if method == "green":
        dst = green(image)
        cv2.imwrite('./static/img/result.jpg', dst)
        
    if method == "darkgreen":
        dst = darkgreen(image)
        cv2.imwrite('./static/img/result.jpg', dst)        

    if method == "blue":
        dst = blue(image)
        cv2.imwrite('./static/img/result.jpg', dst) 
    
    if method == "navy":
        dst = navy(image)
        cv2.imwrite('./static/img/result.jpg', dst) 

    if method == "purple":
        dst = purple(image)
        cv2.imwrite('./static/img/result.jpg', dst) 
    
    if method == "pink":
        dst = pink(image)
        cv2.imwrite('./static/img/result.jpg', dst)
        
    if method == "brown":
        dst = brown(image)
        cv2.imwrite('./static/img/result.jpg', dst)
 
           
    return "result"

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
