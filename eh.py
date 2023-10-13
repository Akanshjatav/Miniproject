import cv2
import face_recognition

imageElon = face_recognition.load_image_file("C:/Users/akans/Downloads/Files/Images/963852.png")
imageElon = cv2.cvtColor(imageElon, cv2.COLOR_BGR2RGB)

imagetest = face_recognition.load_image_file("C:/Users/akans/Downloads/Files/Images/elon_musk_royal_society.jpg")
imagetest = cv2.cvtColor(imagetest, cv2.COLOR_BGR2RGB)


facloc = face_recognition.face_locations(imageElon)[0]
encodeElon = face_recognition.face_encodings(imageElon)[0]
cv2.rectangle(imageElon, (facloc[3], facloc[0]), (facloc[1],facloc[2]), (100,250,150), 2)

facloc = face_recognition.face_locations(imagetest)[0]
encodetest = face_recognition.face_encodings(imagetest)[0]
cv2.rectangle(imagetest, (facloc[3], facloc[0]), (facloc[1],facloc[2]), (100,250,150), 2)

results = face_recognition.compare_faces([encodeElon], encodetest)
print(results)

facedis = face_recognition.face_distance([encodeElon],encodetest)





cv2.imshow("Train", cv2.resize(imageElon, (0, 0), fx=0.5, fy=0.5))
cv2.imshow("Test", cv2.resize(imagetest, (0, 0), fx=0.5, fy=0.5))

cv2.waitKey(0)
