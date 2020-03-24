import cv2
import numpy as np



vid = cv2.VideoCapture(0)

vid.set(3, 1280)
vid.set(4, 720)
var=0

while True:

    contadorInvertido=False
    contadorHsv=False
    contadorBlur=False
    contadorLab=False
    salida=False

    ret, frame = vid.read()
    frame=cv2.flip(frame, 1)
    cropped = frame[50:600, 150:1050]
    imagen_Crp = frame[400:600,150:1050,:]
    img_RGB=cv2.cvtColor(imagen_Crp, cv2.COLOR_BGR2RGB)
    r,g,b = cv2.split(img_RGB)

    upper_left = (0, 0)
    bottom_right = (899, 392)
    ret1 = cv2.rectangle(cropped, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = cropped[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    sketcher_rect = rect_img

    #-------------Filtros-------------------

    #----------------------------------------

    rectangle = cv2.rectangle(cropped,(2, 392), (898,548), (0,0,255), 3)
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
    cv2.putText(cropped,"B",(400,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"L",(580,515), font, font_size, font_color, 2, cv2.LINE_AA)
    cv2.putText(cropped,"Q",(750,508), font, font_size, font_color, 2, cv2.LINE_AA)

    #----------------------------------------
    circles = cv2.HoughCircles(r, cv2.HOUGH_GRADIENT, 1, 700, np.array([]), 100, 30, 0, 0)
    circles=np.uint16(np.around(circles))
    #print(circles)
    #print("x=" , circles)
    #len1 = len(circles)
    #print("len ", len1)
    if len(circles) > 0:

        for i in circles[0,:]:
            if i[0] >= 30 and i[0] <=860 and i[1] >= 40 and i[1] <=180:
                cv2.circle(imagen_Crp,(i[0], i[1]), i[2], (0,255,0),1)
                cv2.circle(imagen_Crp,(i[0], i[1]),2,(0,0,255),3)
                #print(circles)

                if i[0] >= 50 and i[0] <=140 and i[1] >= 20  and i[1] <=160 and i[2]<=60:
                    var=1
                    contadorInvertido=True
                    print("Invertido")
                elif i[0] >= 200 and i[0] <=300 and i[1] >= 20  and i[1] <=160 and i[2]<=60:

                    contadorHsv=True
                    var=2
                    print("HSV")
                elif i[0] >= 370 and i[0] <=470 and i[1] >= 20  and i[1] <=160 and i[2]<=60:

                    contadorBlur=True
                    print("Blur")
                    var=3
                elif i[0] >= 540 and i[0] <=660 and i[1] >= 20  and i[1] <=160 and i[2]<=60:

                    contadorLab=True
                    print("LAB")
                    var=4
                elif i[0] >= 740 and i[0] <=840 and i[1] >= 20  and i[1] <=160 and i[2]<=60:
                    print("Salio")
                    salida=True

            else:
                cv2.imshow("Captura", cropped)
        if salida==True:
            break
    else:
        cv2.imshow("Captura", cropped)


    if var == 1:
            sketcher_rect=(255-sketcher_rect)
            cropped[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect
            cv2.imshow("Captura", cropped)
    if var == 2:
            sketcher_rect=cv2.cvtColor(sketcher_rect, cv2.COLOR_BGR2HSV)
            cropped[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect
            cv2.imshow("Captura", cropped)
    if var == 3:
            cambio = cv2.GaussianBlur(sketcher_rect, (15,15), 0)
            cropped[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = cambio
            cv2.imshow("Captura", cropped)
    if var == 4:
            sketcher_rect=cv2.cvtColor(sketcher_rect, cv2.COLOR_BGR2LAB)
            cropped[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect
            cv2.imshow("Captura", cropped)

    cv2.waitKey(1)

vid.release()
cv2.destroyAllWindows()
