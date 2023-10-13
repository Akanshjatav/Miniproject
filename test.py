import face_recognition
import cv2
import numpy as np


imgElon = face_recognition.load_image_file(f"C:/Users/akans/Downloads/Files/Images/TTHS1VR.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file(f"C:/Users/akans/Downloads/Files/Images/elon_musk_royal_society.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


faceLoc = face_recognition.face_locations(imgElon)
encodeElon = face_recognition.face_encodings(imgElon)
print(faceLoc)
for arr in faceLoc:
    cv2.rectangle(imgElon,(arr[3],arr[0]),(arr[1],arr[2]),(255,0,255),5)

    

faceLocTest = face_recognition.face_locations(imgTest)
print(faceLocTest)
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)
# cv2.putText(imgTest,f'{results} {round(faceDis[0],2)} ',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),3)



#cv2.imshow('Test Image', cv2.resize(imgTest, (0, 0), fx=0.5, fy=0.5))
#cv2.imshow('Train Image', cv2.resize(imgElon, (0, 0), fx=.5, fy=.5))


cv2.waitKey(0)