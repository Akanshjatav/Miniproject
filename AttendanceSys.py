import cv2
import numpy as np
import face_recognition
import os
import imutils as im
path = "C:/Users/akans/Downloads/Files/Images"
images = []
classNames = []
MyList = os.listdir(path)
print(MyList)

for cls in MyList:
    curimg = cv2.imread(f'{path}/{cls}')
    images.append(curimg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListKnown = findEncodings(images)
print('Encodings Complete')

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
facesCurFrame = face_recognition.face_locations(imgS)
encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
matchIndex = np.argmin(faceDis)

if matches[matchIndex]:
    name = className[matchIndex].upper()
    y1,x2,y2,x1=faceLoc
    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList =[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in  line:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            f.writelines(f'n{name},{dt_string}')

if matches[matchIndex]:
    name = classNames[matchIndex].upper()
    #print(name)
    y1,x2,y2,x1 = faceLoc
    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    markAttendance(name)

if faceDis[matchIndex]< 0.50:
    name = classNames[matchIndex].upper()
    markAttendance(name)
else: name = 'Unknown'
#print(name)
y1,x2,y2,x1 = faceLoc
y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

#imageElon = face_recognition.load_image_file("C:/Users/akans/Downloads/Files/Images/963852.png")
#imageElon = cv2.cvtColor(imageElon, cv2.COLOR_BGR2RGB)

#imagetest = face_recognition.load_image_file("C:/Users/akans/Downloads/Files/Images/elon_musk_royal_society.jpg")
#imagetest = cv2.cvtColor(imagetest, cv2.COLOR_BGR2RGB)
