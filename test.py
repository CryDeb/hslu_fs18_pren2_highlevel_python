import numpy as np
import cv2
#import time


cap = cv2.VideoCapture("/home/dane/wayne.mp4")
_, frame = cap.read()
_, frame = cap.read()
minSize = 60.0
maxSize = 450000
#time.sleep(3)
print("started")
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    if frame is None:
        break
    height, width = frame.shape[:2]
    # Our operations on the frame come here
    frame = cv2.resize(frame, (int(width/4), int(height/4)))
    #frame2 = cv2.GaussianBlur(frame, (25, 25), 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 102, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4 and cv2.contourArea(c) > minSize and cv2.contourArea(c) < maxSize:
            print("Wayne " + str(cv2.contourArea(c)))
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print("Center: " + str(M["m10"] / M["m00"]))
            #cv2.drawContours(im2, [c], -1, (132, 255, 0), 2)
            #cv2.circle(im2, (cX, cY), 7, (110, 155, 155), -1)
            count += 1
            #cv2.drawContours(im2, [c], -1, (122, 255, 0), 2)
    print(str(count))
    #if count > 0:
    #   time.sleep(0.1)
    # Display the resulting frame
    cv2.imshow('frame',im2)
    #time.sleep(0.1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #if cv2.waitKey(1) & 0xFF == ord('w'):
    #    time.sleep(2)

# When everything done, release the capture
print("end")
cap.release()
#cv2.destroyAllWindows()
