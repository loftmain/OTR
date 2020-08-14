
from flask import Flask, request, render_template, redirect, session
import cv2
import numpy as np
import datetime

image = None

app = Flask(__name__)

###################################################modules

def red_detector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = (-10,100, 100)
    upper_red = (10, 255, 255)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.GaussianBlur(mask, (9, 9), 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    mask = cv2.dilate(mask, kernel, iterations=1)
    red_object = cv2.bitwise_and(image, image, mask=mask)
    dst = cv2.addWeighted(gray, 0.5, red_object, 1.0, 0.0)
    
    return dst




###########################################################apps

@app.route('/')
def index():
    return render_template("imageprocessing.html", ctx={"title":"Over the Rainbow"})


@app.route('/upload', methods=["POST"]) # post방식이 올때 업로드하려면
def upload():
    global image # 글로벌 변수 선언 이 함수 밖에서도 사용 가능 글로벌 함수는 많이 사용 안하는게 좋다. 남발하면 추적하기 힘듬
    f = request.files['file1']
    filename = "./static/img/" + f.filename
    f.save(filename)
    image = cv2.imread(filename) # 이미지 로딩
    cv2.imwrite("./static/img/result.jpg", image)
    print(image.shape)
#     session["image"] = image

    return redirect("/")


@app.route('/imageprocess')
def imageprocss():
    global image
    method = request.args.get("method")

    
    if method == "red":
        dst = red_detector(image)
        cv2.imwrite('./static/img/result.jpg', dst)
    
        
        
    return "hello~~"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
