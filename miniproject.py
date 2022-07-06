import cv2
import webbrowser
import validators
import pyqrcode

while True:
    def read():
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            img = cv2.resize(img, (1366, 768))
            data, bbox, _ = detector.detectAndDecode(img)
            if bbox is not None:
                if data:
                    print(data)
                    valid = validators.url(data)
                    if valid == True:
                        webbrowser.open("https://google.com/search?q=%s" % data)

                    cv2.putText(img, data, (500, 300), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (0, 0, 0), 6)
            cv2.imshow("qr scanner", img)
            if cv2.waitKey(1) == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

    def generater():
        while True:
            r=input("ENTER")
            #r ="www.geeksforgeeks.org"
            url=pyqrcode.create(r)
            url.show()
            s=input("d to download")
            f=input("filename")
            if s=='d' or s=='D':
                url.png(f+".png", scale=10)


    a=input("G to genreate qr" "   S to scanner qr")
    if a=='G' or a=='g':
        generater()
    elif a=='S'or a=='s':
        read()
    else:
        print("Invalid request")
