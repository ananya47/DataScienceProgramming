# This is the first step of the Face Recognition Project where we perform the dataset creation:

import cv2
import os
import datetime
import time

# Here, a folder is created in the working directory with the username given
username = input('Enter Username: ')
username = username.lower()
if not username:

    print("Enter valid username")
    exit()
isExist = os.path.exists(username)
if not isExist:
    os.makedirs(username)

cv2.namedWindow("Image Capture")
file_list = []

# Opens the Video file
cam = cv2.VideoCapture(0)
i = 0

# Here, the cam is opened and captures 150 images for the dataset and names them as img+i in .jpg format
while (cam.isOpened() and i<=100):
    ret, frame = cam.read()
    if ret == False:
        break
    cv2.imwrite('img' + str(i) + '.jpg', frame)
    time.sleep(0.1)
    file_list.append('img' + str(i) + '.jpg')
    i += 1

cam.release()

#cv2.destroyAllWindows()

# Here we are saving all those images in the folder created with the username given
c=0
for i in file_list:
    # Read the input image
    img = cv2.imread(i)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h),
                      (0, 0, 255), 2)

        faces = img[y:y + h, x:x + w]
        #         cv2.imshow("face",faces)
        cv2.imwrite(os.getcwd() + '/' + username + '/'+'img' + str(c) + '.jpg', faces)
    os.remove(os.getcwd() + "/" +i)
    c+=1


exit()