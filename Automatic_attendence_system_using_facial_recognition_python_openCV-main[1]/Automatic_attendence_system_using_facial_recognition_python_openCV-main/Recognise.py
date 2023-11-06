import cv2
import xlwrite
import time
from playsound import playsound

start = time.time()
period = 8

face_cas = cv2.CascadeClassifier('C:/Users/User/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read('C:/Users/User/Desktop/trainer/trainer.yml')

flag = 0
filename = 'filename'
attendance_dict = {}

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = recognizer.predict(roi_gray)

        if conf < 50:
            if id == 1:
                id = 'Debashis'
                if str(id) not in attendance_dict:
                    filename = xlwrite.output('attendance', 'class1', 1, id, 'yes')
                    attendance_dict[str(id)] = str(id)

            elif id == 2:
                id = 'Bipodtaran'
                if str(id) not in attendance_dict:
                    filename = xlwrite.output('attendance', 'class1', 2, id, 'yes')
                    attendance_dict[str(id)] = str(id)

            elif id == 3:
                id = 'Chandana'
                if str(id) not in attendance_dict:
                    filename = xlwrite.output('attendance', 'class1', 3, id, 'yes')
                    attendance_dict[str(id)] = str(id)

        else:
            id = 'Unknown, cannot recognize'
            flag += 1
            break

        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)

    cv2.imshow('frame', img)

    if flag == 10:
        playsound('transactionSound.mp3')
        print("Transaction Blocked")
        break

    if time.time() > start + period:
        break

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
