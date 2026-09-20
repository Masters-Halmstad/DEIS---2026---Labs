import cv2
cap = cv2.VideoCapture(0)

cv2.namedWindow('Color Feed')
cv2.namedWindow('Edge Detection')

while(True):
    ret, frame = cap.read()
    if(ret):
        img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img2,100,200)
        cv2.imshow('Edge Detection', edges)
        cv2.imshow('Color Feed', frame)
        key=cv2.waitKey(10) & 0xFF
        if key == ord('q'):
            print("Done")
            break
        elif key == ord('s'):
            cv2.imwrite("screenshot_edge.jpg",edges)
            cv2.imwrite("screenshot_color.jpg",frame)
            print("Took a Picture")
    else:
        break

cap.release()
cv2.destroyAllWindows()