import numpy as np
import cv2

def Q2A():
    cap = cv2.VideoCapture('atrium.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('Vid1.avi',fourcc, 30.0, (640,360),0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Otsu's thresholding
            ret2, black_and_white = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Otsu's thresholding after Gaussian filtering
            # blur = cv2.GaussianBlur(gray, (5, 5), 0)
            # ret3, black_and_white = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            out.write(black_and_white)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def Q2B():
    cap = cv2.VideoCapture('atrium.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('gscaleVid.avi', fourcc, 30.0, (640, 360), 0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def Q2C():
    cap = cv2.VideoCapture('atrium.avi')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('Vid3.avi', fourcc, 30.0, (640, 360), 0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Otsu's thresholding
            ret2, black_and_white = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            sobel = cv2.Sobel(black_and_white,cv2.CV_64F, 1, 1, ksize=5)
            sobel = sobel.astype(np.uint8)
            out.write(sobel)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

