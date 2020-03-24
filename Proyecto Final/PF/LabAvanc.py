import cv2
import numpy as np


vid = cv2.VideoCapture(0)

vid.set(3, 1280)
vid.set(4, 720)
upper_left=(2, 898)
bottom_right=(392,548)
while True:

    contadorInvertido=False
    contadorGris=False
    contadorThresh=False
    contadorDerivate=False
    salida=False

    ret, frame = vid.read()
    cropped = frame[50:600, 150:1050]
    print(cropped.shape)

    img_RGB=cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    r,g,b = cv2.split(img_RGB)

    rectangle = cv2.rectangle(cropped,(2, 392), (898,548), (0,0,255), 3)
    rect_img = cropped[392:548, 2:898]
    sketcher_rect=cv2.cvtColor(rect_img, cv2.COLOR_BGR2RGB)
    #sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2BGR)
    cropped[392:548, 2:898] = sketcher_rect
    rectanglemas = cv2.rectangle(cropped,(10, 405), (150,538), (0,255,0), 3)
    rectanglemenos = cv2.rectangle(cropped,(170, 405), (330,538), (0,255,0), 3)
    rectanglefilter = cv2.rectangle(cropped,(350, 405), (510,538), (0,255,0), 3)
    rectanglefilter2 = cv2.rectangle(cropped,(530, 405), (690,538), (0,255,0), 3)
    rectangleq = cv2.rectangle(cropped,(710, 405), (870,538), (0,255,0), 3)

    #--------------Fuentes------------------
    font=cv2.FONT_HERSHEY_COMPLEX
    font_size=4
    font_color=(255,255,255)

    cv2.putText(cropped,"I",(50,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"H",(215,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"T",(400,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"L",(580,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"Q",(750,508), font, font_size, font_color, 2, cv2.LINE_AA)

    #----------------------------------------
    circles = cv2.HoughCircles(g, cv2.HOUGH_GRADIENT, 1, 300, np.array([]), 100, 30, 0, 0)
    circles=np.uint16(np.around(circles))
    print(circles)
    for i in circles[0,:]:
        if i[0] >= 30 and i[0] <=850 and i[1] >= 360 and i[1] <=520:
            cv2.circle(cropped,(i[0], i[1]), i[2], (0,255,0),1)
            cv2.circle(cropped,(i[0], i[1]),2,(0,0,255),3)
        #print(circles)

        if i[0] >= 50 and i[0] <=120 and i[1] >= 420 and i[1] <=510 and i[2]<=60:
            contadorInvertido=True
            print("Invertido")
        if i[0] >= 200 and i[0] <=300 and i[1] >= 420 and i[1] <=510 and i[2]<=60:
            contadorGris=True
            print("HSV")
        if i[0] >= 370 and i[0] <=470 and i[1] >= 420 and i[1] <=510 and i[2]<=60:
            contadorThresh=True
            print("Threshold")
        if i[0] >= 540 and i[0] <=660 and i[1] >= 420 and i[1] <=510 and i[2]<=60:
            contadorDerivate=True
            print("Derivada")
        if i[0] >= 720 and i[0] <=840 and i[1] >= 420 and i[1] <=510 and i[2]<=60:
            salida=True
            print("Salio")

    if contadorInvertido == True:
        cropped=(255-cropped)
        cv2.imshow("Captura", cropped)

    elif contadorGris == True:
        gray=cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
        cv2.imshow("Captura", gray)

    elif contadorThresh == True:
        gray=cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        ret, tresh=cv2.threshold(gray,50,200,cv2.THRESH_BINARY)
        cv2.imshow("Captura", tresh)

    elif contadorDerivate == True:
        gray=cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        kernel=np.array([[1,1,1], [1,-8,1], [1,1,1]], np.float32)
        kernel2=np.array([[1,2,1], [0,0,0], [-1,-2,-1]], np.float32)
        kernel3=np.array([[-1,-2,-1], [0,0,0], [1,2,1]], np.float32)
        kernel4 = np.array([[0,1,0],[1,-4,1],[0,1,0]], np.float32)
        log = cv2.filter2D(gray, -1, kernel)
        cv2.imshow("Captura", log)

    elif  salida == True:
        break
    else:
        cv2.imshow("Captura", cropped)
    #cv2.imshow("Rojo", cropped)
    cv2.waitKey(1)

vid.release()
cv2.destroyAllWindows()
